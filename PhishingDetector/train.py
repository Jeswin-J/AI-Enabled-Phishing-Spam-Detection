import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import joblib

# Load dataset
data0 = pd.read_csv('dataset/dataset.csv')

# Data preprocessing
data = data0.sample(frac=1).reset_index(drop=True)
y = data['phishing']
X = data.drop('phishing', axis=1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

# Model training
xgb = XGBClassifier(learning_rate=0.4, max_depth=7)
xgb.fit(X_train, y_train)

# Model evaluation
y_test_xgb = xgb.predict(X_test)
y_train_xgb = xgb.predict(X_train)
acc_train_xgb = accuracy_score(y_train, y_train_xgb)
acc_test_xgb = accuracy_score(y_test, y_test_xgb)

# Print accuracy
print("XGBoost: Accuracy on training Data: {:.3f}".format(acc_train_xgb))
print("XGBoost: Accuracy on test Data: {:.3f}".format(acc_test_xgb))

# Save the trained model
filename = 'ml_model/xgboost_model.joblib'
joblib.dump(xgb, filename)
