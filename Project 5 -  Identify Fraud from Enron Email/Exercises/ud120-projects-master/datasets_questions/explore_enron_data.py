#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

#load dataset
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of data points in enron dataset:",len(enron_data)


features_list = []

for i in enron_data:
    features_list.append(len(i))
print "Minimum features number:",min(features_list)


for key in enron_data.iterkeys():
    print len(enron_data[key])


##Quiz: Finding POIs In The Enron Data

from collections import Counter
countList = []
for key in enron_data.keys():
    countList.append(enron_data[key]['poi'])

print Counter(countList)

##How Many POIs Exist?
count_Poi = []
for i in enron_data.keys():
    #print counter(enron_data[name]['poi'])
    if enron_data[key]['poi'] == True:
        count_Poi.append(enron_data[key]['poi'])
    else:
        continue
    print len(count_Poi)
    #print name, enron_data[name]['poi']

import pandas as pd
counter = 0
for i in enron_data.values():
	if i['poi'] == True:
		counter+=1
print " # POI is %d " %counter



value_jamesp = enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Total stock value for James Prentice is:", value_jamesp

from_messages_ColwellW = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Messages from Wesley Corwell to POI:", from_messages_ColwellW

stock_value_JeffreyKSkilling = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "Stock value Jeffrey K Skilling:", stock_value_JeffreyKSkilling

max_payment = [[enron_data["LAY KENNETH L"]["total_payments"],"LAY KENNETH L"],
               [enron_data["FASTOW ANDREW S"]["total_payments"],"FASTOW ANDREW S"],
               [enron_data["SKILLING JEFFREY K"]["total_payments"],"SKILLING JEFFREY K"]]
print "Max payment:", max(max_payment),
print max_payment

integers = []
for k,v in enron_data.iteritems():
	if v['salary'] != 'NaN':
		integers.append(v)
print "Number of people that have salary in dataset:",len(integers)


#QUIZ 27
#How many folks in this dataset have a quantified salary? What about a known email address?
emails = []
for k,v in enron_data.iteritems():
	if v['email_address'] != 'NaN':
        #check for non_NaN emails
		emails.append(v)
print "Number of people that have e-mail in dataset:", len(emails)



print "Number of people +10", len(enron_data)+10

print "Number with NaN for total payments +10", sum(1 for person in enron_data.values() if person['total_payments'] == 'NaN')+10
