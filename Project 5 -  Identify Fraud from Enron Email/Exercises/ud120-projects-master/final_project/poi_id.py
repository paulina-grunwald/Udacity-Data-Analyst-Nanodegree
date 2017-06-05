#!/usr/bin/python

#import necessary modules
import sys
import pickle
import math
import matplotlib.pyplot as plt

#import sklearn libraries

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from IPython.display import Image
import matplotlib.pyplot as plt
import sys
import pickle
from sklearn import preprocessing
from time import time
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

features_list = ['poi','salary','bonus','total_payments','total_stock_value',
                'to_messages','from_poi_to_this_person',
                'from_messages','from_this_person_to_poi',
                'long_term_incentive']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)



data = featureFormat(data_dict, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

#Task 2: Access the outliers
#2.1. Explore dataset

print "There are ", len(data_dict.keys()), " employees in the Enron Dataset."
#print first 40 names
print "Those are names of the first 40 Enron employees:", data_dict.keys()[:40]
#Print data for one person
print data_dict["METTS MARK"]
print "Number of features is:",(len(data_dict[(next(iter(data_dict)))]))

#Count number of POIs
num_poi = 0
for poi in data_dict.values():
    if poi['poi'] == 1: num_poi += 1

print "Number of POIs is: ", num_poi

#Plot salaries vs. bonuses of people employed by Enron in order to asses the outlier in the data.
### plot features
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
### plot features
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("Salary")
plt.ylabel("Bonus")
plt.show()

##################################################################
### Task 2: Remove outliers
### remove any outliers before proceeding further

features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
### remove NAN's from dataset
outliers = []
for key in data_dict:
    val = data_dict[key]['salary']
    if val == 'NaN':
        continue
    outliers.append((key, int(val)))

outliers_final = (sorted(outliers,key=lambda x:x[1],reverse=True)[:4])
### print top 4 salaries
print outliers_final

#plot with removed outliers
features2 = ["salary", "bonus"]
data2 = featureFormat(data_dict, features2)
### plot features
for point in data2:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()



##############################################
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

# Create features fraction of emails that is from or to POI
for key in data_dict:
    if (data_dict[key]['from_this_person_to_poi']=='NaN') or (data_dict[key]['from_messages']=='NaN'):
      data_dict[key]['from_ratio'] = 0
    else:
      data_dict[key]['from_ratio'] = (1.0*data_dict[key]['from_this_person_to_poi']/data_dict[key]['from_messages'])
    if (data_dict[key]['from_poi_to_this_person']=='NaN') or (data_dict[key]['to_messages']=='NaN'):
      data_dict[key]['to_ratio'] = 0
    else:
      data_dict[key]['to_ratio'] = (1.0*data_dict[key]['from_poi_to_this_person']/data_dict[key]['to_messages'])





### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()





### Task 5: Tune your classifier to achieve better than .3 precision and recall
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info:
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

#dump_classifier_and_data(clf, my_dataset, features_list)
#pickle.dump(clf, open("my_classifier.pkl", "w") )
#pickle.dump(data_dict, open("my_dataset.pkl", "w") )
#pickle.dump(features_list, open("my_feature_list.pkl", "w") )