import io
import os

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import nltk
import string

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as RFR
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

try:
    df = pd.read_csv('dataset/spam_sub.csv', encoding="utf-8")
except UnicodeDecodeError:
    # Handle encoding error by opening the file in binary mode
    with open('dataset/spam_sub.csv', 'rb') as file:
        # Read the binary content of the file
        binary_content = file.read()

        # Decode the binary content using utf-8 encoding with errors='ignore'
        decoded_content = binary_content.decode("utf-8", errors='ignore')

        # Create a StringIO object to mimic file-like object
        file_like_object = io.StringIO(decoded_content)

        # Create DataFrame from the StringIO object
        df = pd.read_csv(file_like_object)

df.replace({r'\r\n': ' '}, regex=True, inplace=True)

print(df.head())


def preprocess_text(text):
    ps = PorterStemmer()
    all_stop_words = set(stopwords.words('english'))
    all_stop_words.remove('not')
    text = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    text = [ps.stem(word) for word in text if word not in all_stop_words]
    return ' '.join(text)


def analyse_subject(subject):
    subject_processed = preprocess_text(subject)
    X_subject = cv.transform([subject_processed]).toarray()
    prediction = cl_rf.predict(X_subject)
    if prediction[0] == 1:
        return 1
    else:
        return 0


# df.rename(columns={'v2': 'text'}, inplace=True)

cv = CountVectorizer(max_features=42500)
X = cv.fit_transform(df['text']).toarray()
y = df['label_num']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
cl_rf = RFR(n_estimators=100, random_state=42)
cl_rf.fit(X_train, y_train)
