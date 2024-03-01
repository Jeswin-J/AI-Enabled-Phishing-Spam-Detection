import pickle

import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS

#from PhishingDetector.feat import FeatureExtraction
from PhishingDetector.features import feature_extraction
from PhishingDetector.url_features import *
from PhishingDetector.website_features import *
from SpamDetector.msg_classification_model import cv
from SpamDetector.sub_classification_model import analyse_subject
from SpamDetector.utils import predict_spam
from TraceCall.trace_call import *
from UrlScanner.url_scanner import *
from Utils.utils import *

from PhishingDetector.URLFeatureExtraction import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spamdetector')
def spam_detector():
    return render_template('spamdetector.html')


@app.route('/phishingdetector')
def phishing_detector():
    return render_template('phishingdetector.html')


@app.route('/tracecall')
def trace_call():
    return render_template('tracecall.html')


@app.route('/urlscanner')
def url_scanner():
    return render_template('urlscanner.html')


@app.route('/api/detectphishing', methods=['POST'])
def check_phishing():
    url = request.form.get('url')
    if is_valid_url(url):
        response = requests.get(url)

        recommendation = read_json("Database/do_and_dont_phishing.json")

        data = {
            "protocol": "",
            "src_url": url,
            "redir_url": "--",
            "status": "",
            "phishing_score": "",
            "redir_count": "--",
            "is_homograph": "",
            "shortened": "",
            "current_timestamp": get_timestamp(),
            "do": {
                "do_1": get_random_recommend(recommendation, 'do'),
                "do_2": get_random_recommend(recommendation, 'do'),
                "do_3": get_random_recommend(recommendation, 'do'),
            },
            "do_not": {
                "dont_1": get_random_recommend(recommendation, 'dont'),
                "dont_2": get_random_recommend(recommendation, 'dont'),
                "dont_3": get_random_recommend(recommendation, 'dont')
            },
            "condition": False
        }

        features = {
            "protocol": check_url_protocol(url),
            "at_sign": check_at_sign(url),
            "ip_in_domain": have_ip_addr(url),
            "url_length": check_url_length(url),
            "redirection": have_redirection(url),
            "https_in_domain": check_https_domain(url),
            "dash": have_dash(url),
            "upper_case": is_domain_upper(url),
            "homograph": check_homograph(url),
            "short": check_tiny_url(url),
            "iframe": have_iframe(response),
            "forward": forwarding(response),
            "r_click": right_click(response),
            "m_over": mouse_over(response),
            "head_script": check_head_script(response),
            "num_domain": have_num(url),
            "favicon": check_favicon(response, url),
        }

        if features["protocol"]:
            data["protocol"] = "http"
        else:
            data["protocol"] = "https"

        risk_score = calc_phishing_score(features)

        data["phishing_score"] = risk_score

        if risk_score >= 50:
            data["status"] = "Phishing"
        elif 50 > risk_score >= 20:
            data["status"] = "Suspicious"
        else:
            data["status"] = "Legitimate"
            data["condition"] = True

        if features["homograph"]:
            data["is_homograph"] = "Yes"
        else:
            data["is_homograph"] = "No"

        if features["short"]:
            data["shortened"] = "Yes"
        else:
            data["shortened"] = "No"

        url_features = feature_extraction(url)
        print(url_features)


        return render_template('results/phishingresults.html', data=data)
    return render_template('error/invalid.html')


@app.route('/api/trace', methods=['POST'])
def trace():
    phone = request.form.get('phone')

    try:
        parsed_phone = phonenumbers.parse(phone, None)
        is_valid = phonenumbers.is_valid_number(parsed_phone)
        if is_valid:
            data = process_number(phone)
            location = data["region"]
            lat_long = get_approx_coordinates(location)
            data["lat_long"] = lat_long

            return render_template('results/tracecallresults.html', data=data)
    except Exception as e:
        return render_template('error/invalid.html')


@app.route('/api/scanurl', methods=['POST'])
def scan_url():
    url = request.form.get('url')
    if is_valid_url(url):
        tld = url_tld(url)
        ip_addr = ip_address(url)
        location = ip_location_info(ip_addr)

        ip_info = ip_information(ip_addr)

        entity = ip_info['entities'][0]

        email = ip_info['objects'][entity]['contact']['email']

        if email:
            email_id = email[0]['value']
        else:
            email_id = '--'

        phone = ip_info['objects'][entity]['contact']['phone']

        if phone:
            phone_no = phone[0]['value']
        else:
            phone_no = '--'

        current_timestamp = get_timestamp()

        data = {
            'tld': tld,
            'ip_address': ip_addr,
            'host': host_name(ip_addr),
            'location': location,
            'asn': ip_info['asn'],
            'asn_registry': ip_info['asn_registry'],
            'asn_cidr': ip_info['asn_cidr'],
            'asn_date': ip_info['asn_date'],
            'asn_description': ip_info['asn_description'],
            'country_code': ip_info['asn_country_code'],
            'network_handle': ip_info['network']['handle'],
            'network_status': ip_info['network']['status'][0],
            'last_changed': ip_info['network']['events'][0]['timestamp'],
            'registration_time': ip_info['network']['events'][1]['timestamp'],
            'ip_version': ip_info['network']['ip_version'],
            'address_name': ip_info['objects'][entity]['contact']['name'],
            'address_info': ip_info['objects'][entity]['contact']['address'][0]['value'],
            'email': email_id,
            'phone': phone_no,
            'current_timestamp': current_timestamp,
            'source_url': url,
            'is_phishing': '--',
            'phishing_score': '--',
        }

        print(data['location'])

        return render_template('results/urlscanresults.html', data=data)
    return render_template('error/invalid.html')


@app.route('/api/detectspam', methods=['POST'])
def check_spam():
    message = request.form.get('message')
    phone = request.form.get('phone')
    subject = request.form.get('subject')
    email = request.form.get('email')
    if message:
        prediction_nb, prediction_svm, prediction_lr, prediction_dt = predict_spam(message, cv)
        print("Multinomial Naive Bayes Prediction:", prediction_nb)
        print("Support Vector Machine Prediction:", prediction_svm)
        print("Logistic Regression Prediction:", prediction_lr)
        print("Decision Tree Prediction:", prediction_dt)

        subject = "Special discount offer!"

        sub_analysis = analyse_subject(subject)

        spam_score = ((prediction_nb + prediction_svm + prediction_lr + prediction_dt + sub_analysis) * 100) / 5

        recommendation = read_json("Database/do_and_dont_spam.json")

        data = {
            "input_msg": message,
            "spam_score": spam_score,
            "vector": "",
            "sender": "",
            "status": "",
            "current_timestamp": get_timestamp(),
            "do": {
                "do_1": get_random_recommend(recommendation, 'do'),
                "do_2": get_random_recommend(recommendation, 'do'),
                "do_3": get_random_recommend(recommendation, 'do'),
            },
            "do_not": {
                "dont_1": get_random_recommend(recommendation, 'dont'),
                "dont_2": get_random_recommend(recommendation, 'dont'),
                "dont_3": get_random_recommend(recommendation, 'dont')
            },
            "condition": False

        }

        if phone:
            data["vector"] = "Phone"
            data["sender"] = phone
        elif email:
            data["vector"] = "Email"
            data["sender"] = email

        if spam_score < 25:
            data["status"] = "Not Spam"
            data["condition"] = True
        elif 25 <= spam_score <= 50:
            data["status"] = "Less likely to be Spam"
        elif 50 <= spam_score <= 75:
            data["status"] = "More likely to be Spam"
        else:
            data["status"] = "Spam"

        return render_template('results/spamresults.html', data=data)

    return render_template('error/invalid.html')


# @app.route('/extn/detect', methods=['POST'])
# def detect_spam_and_phishing():
#     data = request.json
#     url = data.get('url')
#     print(url)

#     response = requests.get(url)

#     features = {
#         "protocol": check_url_protocol(url),
#         "at_sign": check_at_sign(url),
#         "ip_in_domain": have_ip_addr(url),
#         "url_length": check_url_length(url),
#         "redirection": have_redirection(url),
#         "https_in_domain": check_https_domain(url),
#         "dash": have_dash(url),
#         "upper_case": is_domain_upper(url),
#         "homograph": check_homograph(url),
#         "short": check_tiny_url(url),
#         "iframe": have_iframe(response),
#         "forward": forwarding(response),
#         "r_click": right_click(response),
#         "m_over": mouse_over(response),
#         "head_script": check_head_script(response),
#         "num_domain": have_num(url),
#         "favicon": check_favicon(response, url),
#     }

#     risk_score = calc_phishing_score(features)

#     if risk_score >= 50:
#         status = "Phishing"
#     elif 50 > risk_score >= 20:
#         status = "Suspicious"
#     else:0
#         status = "Legitimate"

#     print(status)

#     return jsonify({'status': status, 'risk_score': risk_score}), 200



@app.route('/extn/detect', methods=['POST'])
def detect_spam_and_phishing():
    data = request.json
    url = data.get('url')
    print(url)

    model = pickle.load(open("PhishingDetector/ml_model/XGBoostClassifier.pickle.dat", "rb"))

    url_features = featureExtraction(url)

    data_frame = [url_features]
    prediction = model.predict(data_frame)

    
    response = requests.get(url)

    features = {
        "protocol": check_url_protocol(url),
        "at_sign": check_at_sign(url),
        "ip_in_domain": have_ip_addr(url),
        "url_length": check_url_length(url),
        "redirection": have_redirection(url),
        "https_in_domain": check_https_domain(url),
        "dash": have_dash(url),
        "upper_case": is_domain_upper(url),
        "homograph": check_homograph(url),
        "short": check_tiny_url(url),
        "iframe": have_iframe(response),
        "forward": forwarding(response),
        "r_click": right_click(response),
        "m_over": mouse_over(response),
        "head_script": check_head_script(response),
        "num_domain": have_num(url),
        "favicon": check_favicon(response, url),
    }

    risk_score = calc_phishing_score(features)

    risk_score = round(risk_score, 2)
    
    if prediction[0] == 0 and risk_score > 20:
        status = "Phishing"
    else:
        status = "Legitimate"

    return jsonify({'status': status, 'risk_score': risk_score}), 200
    #return jsonify({}), 200


@app.route('/analyze_email', methods=['POST'])
def analyze_email():
    # Check if 'email_header' is in the POST request data
    if 'email_header' not in request.form:
        return jsonify({"error": "No email header provided"})

    email_header = request.form['email_header']

    # Analyze the email header
    analysis_result = {}
    try:
        # Assuming parse_email takes the email header as a string
        analysis_result = parse_email(email_header, doall=True)
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify(analysis_result)
    


if __name__ == '__main__':
    app.run(debug=True)
