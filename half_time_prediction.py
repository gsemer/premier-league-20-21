import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from xgboost import XGBClassifier


# 5-fold cross validation
fold = StratifiedKFold(n_splits=5)


# Initialize the train and test data
df = pd.read_csv('datasets/train.csv')
test_df = pd.read_csv('datasets/test.csv')
  

# Drop all target columns from train and test csv file respectively
X = df.drop(['Id', 'FT', 'HT', 'TG'], 1)
Y = test_df.drop(['Id'], 1)


# Transform the type of each column to string
for column in X.columns:
    X[column] = X[column].astype(str)


# Train data which will be used to train model
X_train = ''
for column in X.columns:
    X_train = X_train + ' ' + X[column]


# Test data which will be fed into the model
X_test = ''
for column in Y.columns:
    X_test = X_test + ' ' + Y[column]


# Target data (Half Time) which will be used to train the model 
y_train = df['HT']


# Transform tha data into vectors according to TF-IDF feature
vocabulary = TfidfVectorizer()
train = vocabulary.fit_transform(X_train)
test = vocabulary.transform(X_test)
   
    
# Give a unique label to target data
encoder = LabelEncoder()
target_train = encoder.fit_transform(y_train)
    
    
# Initialize the model
model = SVC()
model.fit(train, target_train)
    

# Calculate the performance of the model on following evaluation metrics 
scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
scores = cross_validate(model, train, target_train, scoring=scoring, cv=fold)
accuracy = str(round(scores['test_accuracy'].mean(), 3))
precision = str(round(scores['test_precision_macro'].mean(), 3))
recall = str(round(scores['test_recall_macro'].mean(), 3))
f_measure = str(round(scores['test_f1_macro'].mean(), 3))    
print('Accuracy : {}'.format(accuracy))
print('Precision: {}'.format(precision))
print('Recall   : {}'.format(recall))
print('F-Measure: {}'.format(f_measure))


# Make the predictions on test set 
predict = model.predict(test)
predictions = encoder.inverse_transform(predict)


# Show the predictions on a dataframe 
predict_table = pd.DataFrame({'HomeTeam': test_df['HomeTeam'], 'AwayTeam': test_df['AwayTeam'], 'Predicted': predictions})
print(predict_table) 

