# -*- coding: utf-8 -*-
"""Hand Writtennotes

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zijfUCw9VyGO6XD3XAldHgQITF5jB5VL
"""



"""importing basic libraries

"""

import numpy as np
from sklearn.datasets import load_digits

"""Load dataset"""

dataset= load_digits()

"""Summarize dataset"""

print (dataset.data)
print(dataset.target)

print(dataset.data.shape)
print(dataset.images.shape)

dataimageLength = len(dataset.images)
print(dataimageLength)

"""Visualize the Dataset"""

n=1  #No. 1of sampleout of samples total 1797

import matplotlib.pyplot as plt
plt.gray()
plt.matshow(dataset.images[n])
plt.show()

dataset.images[n]

"""segregat Dataset nto X(independent variable) & Y(output/DependentVariable)
Input- pixal | output- Class
"""

x= dataset.images.reshape((dataimageLength,-1))
x

y= dataset.target
y

"""Splitting Dtaset into train & test"""

from sklearn.model_selection import train_test_split
x_train , x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25,random_state = 0)
print(x_train.shape)
print(x_test.shape)

"""Training"""

from sklearn import svm
model = svm.SVC(kernel='linear')
model.fit(x_train,y_train)

"""Prediction, what the digit is from test data"""

n = -9
result = model.predict(dataset.images[n].reshape((1,-1)))
plt.imshow(dataset.images[n], cmap=plt.cm.gray_r, interpolation='nearest')
print(result)
print("\n")
plt.axis('off')
plt.title('%i' %result)
plt.show()

"""prediction for test data"""

y_pred = model.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

"""Evaluate Model - Accuracy Score"""

from sklearn.metrics import accuracy_score
print("Accuracy of the model1: {0}%". format(accuracy_score(y_test, y_pred)*100))

"""Play with the Different Method"""

from sklearn import svm
model1 = svm.SVC(kernel='linear')
model2 = svm.SVC(kernel='rbf')
model3 = svm.SVC(gamma=0.001)
model3 = svm.SVC(gamma=0.001,C=0.1)


model1.fit(x_train,y_train)
model2.fit(x_train,y_train)
model3.fit(x_train,y_train)

y_predmodel1=model1.predict(x_test)
y_predmodel2=model2.predict(x_test)
y_predmodel3=model3.predict(x_test)


print("Accuracy of the model1: {0}%". format(accuracy_score(y_test, y_predmodel1)*100))
print("Accuracy of the model2: {0}%". format(accuracy_score(y_test, y_predmodel2)*100))
print("Accuracy of the model3: {0}%". format(accuracy_score(y_test, y_predmodel3)*100))