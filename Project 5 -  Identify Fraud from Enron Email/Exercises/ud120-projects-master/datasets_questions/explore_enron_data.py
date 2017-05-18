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

################################
#create features list
features_list = []
for i in enron_data:
    features_list.append(len(i))
print "Minimum features number:",min(features_list)

################################

##print strucutre of the data
#for key in enron_data.iterkeys():
#    print key
#    print enron_data[key]

#Count number of features


################################

print "Number of features is:",(len(enron_data[(next(iter(enron_data)))]))

################################
#Quiz: Finding POIs In The Enron Data

from collections import Counter
countList = []
for key in enron_data.keys():
    countList.append(enron_data[key]['poi'])

print Counter(countList)

################################

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

################################
#Calculate stock value for three people of intrest
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
################################

#QUIZ 27
#How many folks in this dataset have a quantified salary? What about a known email address?

integers = []
for k,v in enron_data.iteritems():
	if v['salary'] != 'NaN':
		integers.append(v)
print "Number of people that have salary in dataset:",len(integers)

emails = []
for k,v in enron_data.iteritems():
	if v['email_address'] != 'NaN':
        #check for non_NaN emails
		emails.append(v)
print "Number of people that have e-mail in dataset:", len(emails)
################################

###Quiz 29: what percentage of people in the dataset have "NaN" for their total payments?
num_NAN = len(enron_data)
print "Number of people +10 is:", num_NAN
num_NAN_total = ((sum(1 for person in enron_data.values() if person['total_payments'] == 'NaN')))
print "Number with NaN for total payments is:", num_NAN_total

print "...."

count = 0
for i in enron_data:
    if enron_data[i]['total_payments'] == 'NaN':
        count+=1
print "Number of people with total payments NaN:", count

percent = count/float(len(enron_data))
print "Percent of people who have NaN as total_payment", percent

################################

#Quiz 30: What percentage of POIs in the dataset have "NaN for their total payments?
count = 0
for k in enron_data:
    if enron_data[k]['poi'] is True and enron_data[k]['total_payments'] == "NaN":
        count += 1
print count
#this code prints 0! check!!

################################

#Quiz 31: If a machine learning algorithm were to use total_payments as a feature,
# would you expect it to associate a “NaN” value with POIs or non-POIs?
#No training points would have "NaN" for total_payments when the class label is "POI"

################################

### QUIZ: Stock Option Range
#(NB: if you look at finance_features, there are some "NaN" values that have been cleaned away and replaced with zeroes--
# so while those might look like the minima, it's a bit deceptive because they're more like points for
# which we don't have information, and just have to put in a number. So for this question, go back to data_dict
# and look for the maximum and minimum numbers that show up there, ignoring all the "NaN" entries.)

max_value = float("-inf")

min_value = float("inf")

for k, v in data_dict.iteritems():
    if v["exercised_stock_options"] != "NaN":
        if v["exercised_stock_options"] > max_value:
            max_value = v["exercised_stock_options"]
        if v["exercised_stock_options"] < min_value:
            min_value = v["exercised_stock_options"]

print "max_value exercised_stock_options: ",max_value
print "min_value exercised_stock_options: ",min_value
