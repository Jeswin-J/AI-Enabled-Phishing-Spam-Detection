
import requests
from flask import Flask, render_template, request
from Utils.utils import *

# from SpamDetector.model import cv
# from SpamDetector.utils import predict_spam

from UrlScanner.url_scanner import *
from PhishingDetector.url_features import *
from PhishingDetector.website_features import *

app = Flask(__name__)


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


@app.route('/api/detectspam', methods=['POST'])
def check_spam():
    message = request.form.get('message')
    phone = request.form.get('phone')
    email = request.form.get('email')
    print("##########", message, phone, email)
    return render_template('results/spamresults.html')


@app.route('/api/detectphishing', methods=['POST'])
def check_phishing():
    url = request.form.get('url')
    if is_valid_url(url):

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
        }

        risk_score = calc_phishing_score(features)
        print(risk_score)

        return render_template('results/phishingresults.html')
    return "INVALID"


@app.route('/api/trace', methods=['POST'])
def trace():
    phone = request.form.get('phone')
    print("##########", phone)
    return render_template('results/tracecallresults.html')


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

        return render_template('results/urlscanresults.html', data=data)
    return render_template('error/invalid.html')


# @app.route("/predict_spam", methods=["GET"])
# def check_spam():
#     input_text = ("Dear Sir/Mam, We need Regional Staff store salary 17800/-. Contact HR on "
#                   "https://wa.me/919505335971 Insta Staff")
#     prediction_nb, prediction_svm, prediction_lr, prediction_dt = predict_spam(input_text, cv)
#     print("Multinomial Naive Bayes Prediction:", prediction_nb)
#     print("Support Vector Machine Prediction:", prediction_svm)
#     print("Logistic Regression Prediction:", prediction_lr)
#     print("Decision Tree Prediction:", prediction_dt)
#
#     spam_score = ((prediction_nb + prediction_svm + prediction_lr + prediction_dt) * 100) / 4
#
#     if spam_score <= 25:
#         return f"The text is not likely SPAM. Spam score: {spam_score}%"
#     else:
#         return f"The text is likely SPAM with a confidence score of {spam_score}%"


if __name__ == '__main__':
    app.run()
