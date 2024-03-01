import warnings

import pandas as pd
from sklearn import metrics

warnings.filterwarnings('ignore')

data = pd.read_csv("dataset/phishing.csv")
data.head()

data = data.drop(['Index'], axis=1)

X = data.drop(["class"], axis=1)
y = data["class"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
models = []
accuracy = []
f1_score = []
recall = []
precision = []

from sklearn.ensemble import GradientBoostingClassifier

# Instantiate the model
GBC = GradientBoostingClassifier(max_depth=4, learning_rate=0.7)

# Fit the model
GBC.fit(X_train, y_train)

y_train_gbc = GBC.predict(X_train)
y_test_gbc = GBC.predict(X_test)

# Computing the accuracy, f1_score, Recall, precision of the model performance

acc_train_gbc = metrics.accuracy_score(y_train, y_train_gbc)
acc_test_gbc = metrics.accuracy_score(y_test, y_test_gbc)
print("Gradient Boosting Classifier : Accuracy on training Data: {:.3f}".format(acc_train_gbc))
print("Gradient Boosting Classifier : Accuracy on test Data: {:.3f}".format(acc_test_gbc))
print()

f1_score_train_gbc = metrics.f1_score(y_train, y_train_gbc)
f1_score_test_gbc = metrics.f1_score(y_test, y_test_gbc)
print("Gradient Boosting Classifier : f1_score on training Data: {:.3f}".format(f1_score_train_gbc))
print("Gradient Boosting Classifier : f1_score on test Data: {:.3f}".format(f1_score_test_gbc))
print()

recall_score_train_gbc = metrics.recall_score(y_train, y_train_gbc)
recall_score_test_gbc = metrics.recall_score(y_test, y_test_gbc)
print("Gradient Boosting Classifier : Recall on training Data: {:.3f}".format(recall_score_train_gbc))
print("Gradient Boosting Classifier : Recall on test Data: {:.3f}".format(recall_score_test_gbc))
print()

precision_score_train_gbc = metrics.precision_score(y_train, y_train_gbc)
precision_score_test_gbc = metrics.precision_score(y_test, y_test_gbc)
print("Gradient Boosting Classifier : precision on training Data: {:.3f}".format(precision_score_train_gbc))
print("Gradient Boosting Classifier : precision on test Data: {:.3f}".format(precision_score_test_gbc))

# Computing the classification report of the model
print(metrics.classification_report(y_test, y_test_gbc))

training_accuracy = []
test_accuracy = []
# try learning_rate from 0.1 to 0.9
depth = range(1, 10, 1)
for n in depth:
    gbc_test = GradientBoostingClassifier(max_depth=n, learning_rate=0.7)

    gbc_test.fit(X_train, y_train)
    # Record training set accuracy
    training_accuracy.append(gbc_test.score(X_train, y_train))
    # Record generalization accuracy
    test_accuracy.append(gbc_test.score(X_test, y_test))

import joblib

# Save the model to disk
filename = 'ml_model/model.joblib'
joblib.dump(GBC, filename)
