import time
from datetime import datetime, timezone, timedelta

from flask import Flask, render_template, request

# from SpamDetector.model import cv
# from SpamDetector.utils import predict_spam

from UrlScanner.url_scanner import *

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
    print("##########", url)
    return render_template('results/phishingresults.html')


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
        # host = host_name(ip_addr)
        location = ip_location_info(ip_addr)

        ip_info = ip_information(ip_addr)
        print(ip_info)

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

        current_time_utc = datetime.now(timezone.utc)
        target_timezone = timezone(timedelta(hours=5, minutes=30))
        current_time_target_timezone = current_time_utc.astimezone(target_timezone)
        current_timestamp = current_time_target_timezone.strftime("%Y-%m-%dT%H:%M:%S%z")

        data = {
            'tld': tld,
            'ip_address': ip_addr,
            # 'host': host,
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

        for key, value in data.items():
            print(f"######{key}: {value}\n")

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
