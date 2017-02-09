
qplot(data = reddit, x = age.range)


#Setting levels of ordered factor solution for income
levels(reddit$income.range)   
reddit$income.range <- factor(reddit$income.range, levels = c("Under $20,000", "$20,000 - $29,999", "setwd("c:/Users/Paulina/Desktop/Udacity-Data-Analyst-Nanodegree/Project 4 - Explore and Sumarize data/Exercises")
reddit <- read.csv("reddit.csv")

table(reddit$employment.status)
summary(reddit)

str(reddit)

levels(reddit$age.range) 

#Setting levels of ordered factor solution for age range
reddit$age.range <- ordered(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"))

#Alternate solution
reddit$age.range <- factor(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"))

#create age.range histogram
library(ggplot2)$30,000 - $39,999", "$40,000 - $49,999", "$50,000 - $69,999", "$70,000 - $99,999", "$100,000 - $149,999", "$150,000 or more"))
             
               
library(ggplot2)
qplot(data = reddit, x = income.range)
