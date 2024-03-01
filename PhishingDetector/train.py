#importing basic packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Loading the data
data0 = pd.read_csv('dataset/urldata.csv')

data = data0.drop(['Domain'], axis = 1).copy()
data =data.drop(['Web_Traffic'],axis=1)
#checking the data for null or missing values
data.isnull().sum()

data = data.sample(frac=1).reset_index(drop=True)


# Sepratating & assigning features and target columns to X & y
y = data['Label']
X = data.drop('Label',axis=1)



# Splitting the dataset into train and test sets: 80-20 split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.2, random_state = 12)

#importing packages
from sklearn.metrics import accuracy_score

#XGBoost Classification model
from xgboost import XGBClassifier

# instantiate the model
xgb = XGBClassifier(learning_rate=0.4,max_depth=7)
#fit the model
xgb.fit(X_train, y_train)


#predicting the target value from the model for the samples
y_test_xgb = xgb.predict(X_test)
y_train_xgb = xgb.predict(X_train)

#computing the accuracy of the model performance
acc_train_xgb = accuracy_score(y_train,y_train_xgb)
acc_test_xgb = accuracy_score(y_test,y_test_xgb)

print("XGBoost: Accuracy on training Data: {:.3f}".format(acc_train_xgb))
print("XGBoost : Accuracy on test Data: {:.3f}".format(acc_test_xgb))

# save XGBoost model to file
import pickle
pickle.dump(xgb, open("ml_model/XGBoostClassifier.pickle.dat", "wb"))
