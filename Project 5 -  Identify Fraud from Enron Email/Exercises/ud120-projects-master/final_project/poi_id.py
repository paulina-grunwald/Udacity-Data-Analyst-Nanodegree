#!/usr/bin/python

#import necessary modules
import sys
import pickle
import math
import matplotlib.pyplot as plt

#import sklearn libraries

import os
os.chdir('c:/Personal/GitHub/Udacity-Data-Analyst-Nanodegree/Project 5 -  Identify Fraud from Enron Email/Exercises/ud120-projects-master/final_project')

from IPython.display import Image
import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit
import sys
import pickle
import pandas
import numpy
from sklearn import preprocessing
from time import time
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
sys.path.append("../tools/")


from feature_format import featureFormat
from feature_format import targetFeatureSplit

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit


#Full feature list
financial_features = ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred',
                      'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other',
                      'long_term_incentive', 'restricted_stock', 'director_fees']

email_features = ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi',
                  'shared_receipt_with_poi']

features_list = ['poi','salary','bonus','total_payments','total_stock_value',
                'to_messages','from_poi_to_this_person',
                'from_messages','from_this_person_to_poi',
                'long_term_incentive']

#########Data Wrangle and cleaning of the dataset#########
#Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

data = featureFormat(data_dict, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

###Explore dataset
print "There are ", len(data_dict.keys()), " employees in the Enron Dataset."
#print first 40 names
print "Those are names of the first 40 Enron employees:", data_dict.keys()[:40]
#Print data for one person
print data_dict["METTS MARK"]
#Print number of features in the dataset
print "Number of features is:",(len(data_dict[(next(iter(data_dict)))]))

###Count number of POIs
num_poi = 0
for poi in data_dict.values():
    if poi['poi'] == 1: num_poi += 1
print "Number of POIs is: ", num_poi

###Count number of POI in  in the E+F dataset
num_poi_EF = 0
for i in range(len(data_dict)):
    a = data_dict.values()
    if a[i]['poi'] == True:
        num_poi_EF = num_poi_EF  + 1
print "Number of POIs in E+F dataset:", num_poi_EF

###Plot salaries vs. bonuses of people employed by Enron in order to asses the outlier in the data.
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
#plot features
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )
plt.xlabel("Salary")
plt.ylabel("Bonus")
plt.show()

###Remove any outliers before proceeding further
outliers = ['TOTAL', 'THE TRAVEL AGENCY IN THE PARK']
for outlier in outliers:
    data_dict.pop(outlier, 0)

###Print 5 highest salaries
enron = []
for key in data_dict:
    val = data_dict[key]['salary']
    if val == 'NaN':
        continue
    enron.append((key, int(val)))
#sort the salary entries in the cleaned dataset
enron = (sorted(enron,key=lambda x:x[1],reverse=True)[:5])
#Print top 4 salaries
print 'First 5 top salaries', enron

###Plot with removed outliers
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
### plot features
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()



#########################Feature processing##################################

features_list = [
                 'poi',
                 'salary',
                 # 'deferral_payments',
                 # 'total_payments',
                 # 'loan_advances',
                 'bonus',
                 'bonus_salary_ratio',
                 # 'restricted_stock_deferred',
                 # 'deferred_income',
                 'total_stock_value',
                 # 'expenses',
                 'exercised_stock_options',
                 # 'other',
                 # 'long_term_incentive',
                 # 'restricted_stock',
                 # 'director_fees',
                 # 'to_messages',
                 # 'from_poi_to_this_person',
                 # 'from_poi_to_this_person_percentage',
                 # 'from_messages',
                 # 'from_this_person_to_poi',
                 'from_this_person_to_poi_percentage',
                 'shared_receipt_with_poi'
                 ]



###Print scatterplot from_poi_to_person vs. "from_this_person_to_poi", marking POIs on red
import numpy as np
import matplotlib.pyplot

data_dict.pop('TOTAL',0)
features = ["total_payments", "total_stock_value", "poi"]
data = featureFormat(data_dict, features)


for point in data:
    payments = point[0]
    stock_value = point[1]
    if point[2] == 1:
        matplotlib.pyplot.scatter( payments, stock_value, color = 'red' )
    else:
        matplotlib.pyplot.scatter( payments, stock_value, color = 'blue' )

matplotlib.pyplot.xlabel("Payments")
matplotlib.pyplot.ylabel("Stock value")
matplotlib.pyplot.show()

###Create features fraction of emails that is from or to POI
### create new features fraction_to_poi_email and fraction_from_poi_email

def dict_to_list(key, normalizer):
    new_list = []

    for i in data_dict:
        if data_dict[i][key] == "NaN" or data_dict[i][normalizer] == "NaN":
            new_list.append(0.)
        elif data_dict[i][key] >= 0:
            new_list.append(float(data_dict[i][key]) / float(data_dict[i][normalizer]))
    return new_list


### create two lists of new features
fraction_from_poi_email = dict_to_list("from_poi_to_this_person", "to_messages")
fraction_to_poi_email = dict_to_list("from_this_person_to_poi", "from_messages")

### insert new features into data_dict
count = 0
for i in data_dict:
    data_dict[i]["fraction_from_poi_email"] = fraction_from_poi_email[count]
    data_dict[i]["fraction_to_poi_email"] = fraction_to_poi_email[count]
    count += 1

features_list = ["poi", "fraction_from_poi_email", "fraction_to_poi_email"]
### store to my_dataset for easy export below
enron_dataset = data_dict

### these two lines extract the features specified in features_list
### and extract them from data_dict, returning a numpy array
data = featureFormat(data_dict, features_list)

### plot new features
for point in data:
    from_poi = point[1]
    to_poi = point[2]
    plt.scatter(from_poi, to_poi)
    if point[0] == 1:
        plt.scatter(from_poi, to_poi, color="r", marker="*")
plt.xlabel("Fraction of emails the person gets from POIs")
plt.ylabel("Fraction of emails the person send to POIs")
plt.show()


### Extract features and labels from dataset for local testing
data = featureFormat(data_dict, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)


################Algorithm Selection###################

from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

#features_list = ["poi", "salary", "bonus", "fraction_from_poi_email", "fraction_to_poi_email",
#                 "deferral_payments", "total_payments", "loan_advances", "restricted_stock_deferred",
#                 "total_stock_value", "expenses", "exercised_stock_options", "deferred_income",
#                 "long_term_incentive", "shared_receipt_with_poi", "restricted_stock", "director_fees"]


features_list = ["poi", "fraction_from_poi_email", "fraction_to_poi_email", 'shared_receipt_with_poi']


#extract features_list from the dataset
data = featureFormat(data_dict, features_list)
#split into labels and features
labels, features = targetFeatureSplit(data)


### Task 5: Tune your classifier to achieve better than .3 precision and recall
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info:
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html


#deploying feature selection
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.1, random_state=42)



#use KFold for split and validate algorithm
from sklearn.cross_validation import KFold
kf=KFold(len(labels),3)
for train_indices, test_indices in kf:
    #make training and testing sets
    features_train= [features[ii] for ii in train_indices]
    features_test= [features[ii] for ii in test_indices]
    labels_train=[labels[ii] for ii in train_indices]
    labels_test=[labels[ii] for ii in test_indices]


#Deploy first (Overfit) POI Identifier
from sklearn.tree import DecisionTreeClassifier
t0 = time()
clf_f1 = DecisionTreeClassifier()
clf_f1.fit(features_train,labels_train)
score = clf_f1.score(features_test,labels_test)
print 'Accuracy before tuning ', score
print "Decision tree algorithm time:", round(time()-t0, 3), "s"


t0 = time()
clf_f = DecisionTreeClassifier(class_weight='balanced', criterion='gini',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=2,
            min_samples_split=6, min_weight_fraction_leaf=0.0,
            presort=False, random_state=None, splitter='best')

clf_f = clf_f.fit(features_train,labels_train)
pred = clf_f.predict(features_test)
print("done in %0.3fs" % (time() - t0))
acccuracy=accuracy_score(labels_test, pred)
print "accuracy after tuning = ", acccuracy
print 'Precision is equal to', precision_score(labels_test,pred)
print 'Recall is equal to', recall_score(labels_test,pred)





### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

### dump your classifier, dataset and features_list so
### anyone can run/check your results
pickle.dump(clf_f, open("my_classifier.pkl", "w") )
pickle.dump(data_dict, open("my_dataset.pkl", "w") )
pickle.dump(features_list, open("my_feature_list.pkl", "w") )