import io
import string

import pandas as pd
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.ensemble import RandomForestClassifier as RFR
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

try:
    df = pd.read_csv('SpamDetector/dataset/spam_sub.csv', encoding="utf-8")
except UnicodeDecodeError:
    with open('dataset/spam_sub.csv', 'rb') as file:
        binary_content = file.read()

        decoded_content = binary_content.decode("utf-8", errors='ignore')

        file_like_object = io.StringIO(decoded_content)

        df = pd.read_csv(file_like_object)

df.replace({r'\r\n': ' '}, regex=True, inplace=True)


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


cv = CountVectorizer(max_features=42500)
X = cv.fit_transform(df['text']).toarray()
y = df['label_num']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
cl_rf = RFR(n_estimators=100, random_state=42)
cl_rf.fit(X_train, y_train)
