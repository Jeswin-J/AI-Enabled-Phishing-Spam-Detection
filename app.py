from flask import Flask
from spam_detector.utils import predict_spam
from spam_detector.model import cv

app = Flask(__name__)


@app.route("/predict_spam", methods=["GET", "POST"])
def check_spam():
    input_text = "Dear Sir/Mam, We need Regional Staff store salary 17800/-. Contact HR on https://wa.me/919505335971 Insta Staff"
    prediction_nb, prediction_svm, prediction_lr, prediction_dt = predict_spam(input_text, cv)
    print("Multinomial Naive Bayes Prediction:", prediction_nb)
    print("Support Vector Machine Prediction:", prediction_svm)
    print("Logistic Regression Prediction:", prediction_lr)
    print("Decision Tree Prediction:", prediction_dt)

    spam_score = ((prediction_nb + prediction_svm + prediction_lr + prediction_dt) * 100) / 4

    if  spam_score <= 25:
        return f"The text is not likely SPAM. Spam score: {spam_score}%"
    else:
        return f"The text is likely SPAM with a confidence score of {spam_score}%"



if __name__ == '__main__':
    app.run()
