'''
Created on Apr 12, 2018

@author: M FARHAAN SHAIKH
'''

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import numpy as np

TRAIN_END = 140
TEST_END = 150

np.random.seed(7)

dataset = np.loadtxt("pid.csv", delimiter=",")

X = dataset[0:TEST_END,1:41]
Y = dataset[0:TEST_END,42]
print (X)
print (Y)

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

print (dummy_y)
num_of_attribute=len(dummy_y[0].tolist())

X_train=X[:TRAIN_END,0:40] 
Y_train=dummy_y[:TRAIN_END]
print (X_train)
X_test=X[TRAIN_END-20:TRAIN_END,0:40]
Y_test=dummy_y[TRAIN_END-20:TRAIN_END]


model = Sequential()
model.add(Dense(100, input_dim=40, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(num_of_attribute, activation='softmax'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=150, batch_size=2)

scores = model.evaluate(X_test, Y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
input("press enter")
predictions = model.predict(X_test)
predictions = predictions.tolist()
# round predictions
rounded = [x.index(max(x)) for x in predictions]
actual_val = [x.index(max(x)) for x in Y_test.tolist()]
print("prediction : ",predictions)
print ("rounded     : ",rounded)
print("actual value : ",actual_val)