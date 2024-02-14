import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib


# Preprocess input text
def preprocess_input(input_text):
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    input_text = re.sub('[^A-Za-z]', ' ', input_text.lower())
    words = word_tokenize(input_text)
    stemmed_words = [stemmer.stem(word) for word in words if word not in stop_words]
    processed_input = ' '.join(stemmed_words)
    return processed_input

# Vectorize input text
def vectorize_input(processed_input, cv):
    input_features = cv.transform([processed_input])
    return input_features.toarray()

# Load models
def load_models():
    model_nb = joblib.load('./spam_detection_models/model_nb.pkl')
    model_svm = joblib.load('./spam_detection_models/model_svm.pkl')
    model_lr = joblib.load('./spam_detection_models/model_lr.pkl')
    model_dt = joblib.load('./spam_detection_models/model_dt.pkl')
    return model_nb, model_svm, model_lr, model_dt

# Predict using models
def predict_spam(input_text, cv):
    processed_input = preprocess_input(input_text)
    input_features = vectorize_input(processed_input, cv)
    model_nb, model_svm, model_lr, model_dt = load_models()
    prediction_nb = model_nb.predict(input_features)[0]
    prediction_svm = model_svm.predict(input_features)[0]
    prediction_lr = model_lr.predict(input_features)[0]
    prediction_dt = model_dt.predict(input_features)[0]
    return prediction_nb, prediction_svm, prediction_lr, prediction_dt
