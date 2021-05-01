# Imporing pandas and reading dataset
import pandas as pd
covid = pd.read_csv('../datasets/Covid Dataset.csv')

# Importing pickle 
import pickle

# Using scikit learn to transform labes in dataset
from sklearn.preprocessing import LabelEncoder
e=LabelEncoder()

# Transforming dataset
covid['Breathing Problem']=e.fit_transform(covid['Breathing Problem'])
covid['Fever']=e.fit_transform(covid['Fever'])
covid['Dry Cough']=e.fit_transform(covid['Dry Cough'])
covid['Sore throat']=e.fit_transform(covid['Sore throat'])
covid['Running Nose']=e.fit_transform(covid['Running Nose'])
covid['Asthma']=e.fit_transform(covid['Asthma'])
covid['Chronic Lung Disease']=e.fit_transform(covid['Chronic Lung Disease'])
covid['Headache']=e.fit_transform(covid['Headache'])
covid['Heart Disease']=e.fit_transform(covid['Heart Disease'])
covid['Diabetes']=e.fit_transform(covid['Diabetes'])
covid['Hyper Tension']=e.fit_transform(covid['Hyper Tension'])
covid['Abroad travel']=e.fit_transform(covid['Abroad travel'])
covid['Contact with COVID Patient']=e.fit_transform(covid['Contact with COVID Patient'])
covid['Attended Large Gathering']=e.fit_transform(covid['Attended Large Gathering'])
covid['Visited Public Exposed Places']=e.fit_transform(covid['Visited Public Exposed Places'])
covid['Family working in Public Exposed Places']=e.fit_transform(covid['Family working in Public Exposed Places'])
covid['Wearing Masks']=e.fit_transform(covid['Wearing Masks'])
covid['Sanitization from Market']=e.fit_transform(covid['Sanitization from Market'])
covid['Gastrointestinal ']=e.fit_transform(covid['Gastrointestinal '])
covid['Fatigue ']=e.fit_transform(covid['Fatigue '])
covid['COVID-19']=e.fit_transform(covid['COVID-19'])


# Importing ML Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# Clasification of input and output data
x=covid.drop(['Fatigue ','Gastrointestinal ','Sanitization from Market','Wearing Masks','Family working in Public Exposed Places','Visited Public Exposed Places','COVID-19','Asthma','Chronic Lung Disease','Heart Disease','Diabetes','Hyper Tension','Attended Large Gathering',],axis=1)
y=covid['COVID-19']

# Spliting test and traning data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33)

#Fit the model
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

#Accuracy
acc_logreg = model.score(x_test, y_test)*100

# Achieved accuracy of 97.10
print(acc_logreg)


# Writing data to pickle file
pickle.dump(model,open('../pickle files/covid.pkl','wb'))