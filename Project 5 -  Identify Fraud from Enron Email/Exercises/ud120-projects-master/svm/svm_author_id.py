#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

from sklearn.svm import SVC
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
#clf = SVC(kernel='linear')

#Keep the training set size and rbf kernel from the last quiz, but try several values of C (
# say, 10.0, 100., 1000., and 10000.)
# Which one gives the best accuracy?
#1.0 = 62
#10 = 0.62
#100 = 0.62
#1000 = 0.82
#10000 = 0.89
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

#calculate accuracy##

from sklearn.metrics import accuracy_score
accurcy = accuracy_score(labels_test, pred)
#method that you are using is one that is a method of the classifier. In this case, the arguments that it expects are the features and labels,
#and not the predicted value and labels
#accuracy = clf.score(features_test,labels_test)

print "The model accuracy is:",accurcy
