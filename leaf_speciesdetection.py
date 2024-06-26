# -*- coding: utf-8 -*-
"""leaf_speciesDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vtVeULvLGYSQK-Bm0_bjapfU-wLPgrib

Import Libraries
"""

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

"""Load Dataset"""

dataset = load_iris()

"""Summarize Dataset"""

print(dataset.data)
print(dataset.target)

print(dataset.data.shape)

"""segrigate dataset into X(inpot/independent variable) & Y(output/Dependent valiable"""

x = pd.DataFrame(dataset.data,columns=dataset.feature_names)
x

y= dataset.target
y

"""Splitting Dtaset into train & test"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.25,random_state=0)
print(x_train.shape)
print(x_test.shape)

"""Finding best max_depth value"""

accuracy = []
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

for i in range(1, 10):
  model = DecisionTreeClassifier(max_depth = i, random_state= 0)
  model.fit(x_train, y_train)
  pred = model.predict(x_test)
  score = accuracy_score(y_test, pred)
  accuracy.append(score)


plt.figure(figsize=(12, 6))
plt.plot(range(1, 10), accuracy, color='red', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)
plt.title('finding best max_Depth')
plt.xlabel('pred')
plt.ylabel('score')

"""Training"""

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion = 'entropy', max_depth = 3,random_state= 0)
model.fit(x_train,y_train)

"""Pridicton"""

y_pred = model.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

"""Accuracy Score"""

from sklearn.metrics import accuracy_score
print("Accuracy of the model: {0}%",format(accuracy_score(y_test, y_pred)*100))

