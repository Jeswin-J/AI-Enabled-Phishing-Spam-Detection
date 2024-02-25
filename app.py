import warnings

from flask import Flask, render_template, request

# from SpamDetector.model import cv
# from SpamDetector.utils import predict_spam

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
    print("##########", url)
    return render_template('results/urlscanresults.html')


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
