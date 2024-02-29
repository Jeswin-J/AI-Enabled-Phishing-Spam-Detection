import re

import joblib
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
# nltk.download ("stopwords")
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def preprocess_data(dataset_path):
    dataset = pd.read_csv(dataset_path, encoding='latin-1')
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    processed_sentences = []

    for sen in dataset['v2']:
        senti = re.sub('[^A-Za-z]', ' ', sen.lower())
        words = word_tokenize(senti)
        words = [stemmer.stem(word) for word in words if word not in stop_words]
        senti = ' '.join(words)
        processed_sentences.append(senti)

    return processed_sentences, dataset['v1']


# Train and save models
def train_models(processed_sentences, labels):
    cv = CountVectorizer(max_features=5000)
    features = cv.fit_transform(processed_sentences)
    features = features.toarray()
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)

    # Multinomial Naive Bayes
    model_nb = MultinomialNB()
    model_nb.fit(features, labels_encoded)
    joblib.dump(model_nb, 'SpamDetector/spam_detection_models/model_nb.pkl')

    # Support Vector Machine
    model_svm = SVC(kernel='linear')
    model_svm.fit(features, labels_encoded)
    joblib.dump(model_svm, 'SpamDetector/spam_detection_models/model_svm.pkl')

    # Logistic Regression
    model_lr = LogisticRegression()
    model_lr.fit(features, labels_encoded)
    joblib.dump(model_lr, 'SpamDetector/spam_detection_models/model_lr.pkl')

    # Decision Tree
    model_dt = DecisionTreeClassifier()
    model_dt.fit(features, labels_encoded)
    joblib.dump(model_dt, 'SpamDetector/spam_detection_models/model_dt.pkl')

    return cv, label_encoder


# Main function
# def main():
processed_sentences, labels = preprocess_data('SpamDetector/dataset/spam.csv')
cv, label_encoder = train_models(processed_sentences, labels)

# if __name__ == "__main__":
# main()
