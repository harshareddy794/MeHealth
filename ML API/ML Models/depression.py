#  Import all the libraries for predictive modelling

#create numpy arrays
import numpy as np 
import pandas as pd
import pickle

# Training ML model
url='../datasets/depression.csv'
df = pd.read_csv(url)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
model = LogisticRegression()

train = df.drop(['Name','score','Risk','Age'], axis=1)
train= np.asarray(train, dtype='int64')

test = df[['Risk']]
test= np.asarray(test, dtype='int64')

X_train, X_test, y_train, y_test = train_test_split(train,test, test_size=0.35, random_state=2)


model.fit(X_train, y_train)
pred = model.predict(X_test)
print(model.score(X_test, y_test)*100)  #Accuracy 90.56%

# Writing data to pickle file
pickle.dump(model,open('../pickle files/depression.pkl','wb'))
