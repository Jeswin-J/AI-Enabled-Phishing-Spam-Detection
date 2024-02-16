from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

from utils import featureExtraction, load_dataset

import joblib

data = load_dataset('C:/Users/Jeswin Joseph J/SRM Police Hackathon/AI-Enabled-Phishing-Spam-Detection/dataset/5.urldata.csv')


data = data.drop(['Domain'], axis = 1).copy()


#checking the data for null or missing values
data.isnull().sum()

# shuffling the rows in the dataset so that when splitting the train and test set are equally distributed
data = data.sample(frac=1).reset_index(drop=True)
data.head()

# Sepratating & assigning features and target columns to X & y
y = data['Label']
X = data.drop('Label',axis=1)
X.shape, y.shape

# Splitting the dataset into train and test sets: 80-20 split

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.2, random_state = 12)
X_train.shape, X_test.shape

    # Decision Tree
tree = DecisionTreeClassifier(max_depth=5)
tree.fit(X_train, y_train)
joblib.dump(tree, '../phishing_detection_models/model_tree.pkl')

# Random Forest
forest = RandomForestClassifier(max_depth=5)
forest.fit(X_train, y_train)
joblib.dump(forest, '../phishing_detection_models/model_forest.pkl')

# Multilayer Perceptrons
mlp = MLPClassifier(alpha=0.001, hidden_layer_sizes=(100, 100, 100))
mlp.fit(X_train, y_train)
joblib.dump(mlp, '../phishing_detection_models/model_mlp.pkl')

# XGBoost
xgb = XGBClassifier(learning_rate=0.4, max_depth=7)
xgb.fit(X_train, y_train)
joblib.dump(xgb, '../phishing_detection_models/model_xgb.pkl')

# SVM
svm = SVC(kernel='linear', C=1.0, random_state=12)
svm.fit(X_train, y_train)
joblib.dump(tree, '../phishing_detection_models/model_svm.pkl')



feature_names = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection', 'https_Domain',
                 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 'Domain_Age',
                 'Domain_End', 'iFrame', 'Mouse_Over', 'Right_Click', 'Web_Forwards']


# Load the trained models
model_tree = joblib.load('../phishing_detection_models/model_tree.pkl')
model_forest = joblib.load('../phishing_detection_models/model_forest.pkl')
model_mlp = joblib.load('../phishing_detection_models/model_mlp.pkl')
model_xgb = joblib.load('../phishing_detection_models/model_xgb.pkl')
model_svm = joblib.load('../phishing_detection_models/model_svm.pkl')

# Create a dictionary of models
models = {
    'Decision Tree': model_tree,
    'Random Forest': model_forest,
    'MLP': model_mlp,
    'XGBoost': model_xgb,
    'SVM': model_svm
}

# Function to predict phishing with models
def predict_phishing(models, test_data):
    predictions = {}
    for name, model in models.items():
        y_pred = model.predict(test_data)
        predictions[name] = y_pred
    return predictions

# Test URL
test_url = 'https://www.example.com'

# Extract features from the test URL
test_features = featureExtraction(test_url)

# Create a DataFrame for the test data
test_data = pd.DataFrame([test_features], columns=feature_names)

# Predict phishing with the models
results = predict_phishing(models, test_data)

# Display the results
for model_name, prediction in results.items():
    print(f'Model: {model_name}, Prediction: {prediction}')
