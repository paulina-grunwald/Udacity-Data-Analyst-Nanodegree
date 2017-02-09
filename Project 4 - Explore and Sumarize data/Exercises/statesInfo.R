setwd("c:/Users/Paulina/Desktop/Udacity-Data-Analyst-Nanodegree/Project 4 - Explore and Sumarize data/Exercises")
statesInfo <- read.csv('stateData.csv')

#subset states with state region = 1
subset(statesInfo, state.region == 1)

#subset states with state region = 1 - other possibility
#dataSet[ROWS, COLUMNS]
statesInfo[statesInfo$state.region == 1,]

#You can also save subset to variable
stateSubset <- subset(statesInfo, state.region == 1)
# show header
head(stateSubset,2)
# show dimention
dim(stateSubset)
#------
stateSubsetBracket <- statesInfo[statesInfo$state.region == 1,]
head(stateSubsetBracket,2)
dim(stateSubsetBracket)

#subset murder > 5
stateSubsetMurder <- subset(statesInfo, murder > 5,)
stateSubsetMurder

