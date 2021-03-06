
#### Author: Paulina Grunwald

Date: 14/06/2017

# Udacity Data Analyst Nanodegree: Technical Interview Practice

For each of the questions below, answer as if you were in an interview, explaining and justifying your answer with two to three paragraphs as you see fit. For coding answers, explain the relevant choices you made writing the code.

### Question 1: Describe a data project you worked on recently.

Recently, I have been working on various projects which were assignments In my Udacity Data Analyst Nanodegree. One of them was performing data analytic on white wine dataset for which I have used R programming language. The goal was to asses which wine properties have influence on it’s quality. The dataset contained 13 variables which were representing white wine properties e.g alcohol content, acidity, quality, sweetness. I have used various R packages for my project. Most of the plots were done using ggplot. I have created bar plots, scatter plots, boxplots and histograms. I applied different techniques to get bettet insights from my plots: adding jitter, adjusting axes (limits, log10 etc.), remove top and bottom 1% of the outliers. As a first step of I have done univariate analysis. i have have looked at every white wine property separately by creating histogram to asses if the variable has normal distribution or not and if the outliers are present. In bivariate section of my project I looked at correlation between two different white wine properties. Using ggpairs and corrplot I have create correlation plots. The last part of my analysis consisted of multivariate plot section. Using ggplot I plotted 3 different wine properties on one scatter plot. To adjust colours of the plots I used RColorBrewer package. I have also created a model with lm function but unfortunate it did not result in a good prediction for white wine quality

Analyzing the data I have observed that most frequent quality value of white wine are 5 and 6. Alcohol seem to be a main factor correlated to the wine quality. The data strongly suggest that the higher the alcohol content the better wine quality. When alcohol percentage increases, density decreases. Moreover, the residual suger content increases with increase of density and decrease of alcohol content. I also observed that high quality wines have high content of alcohol and are either dry or medium dry (wine sweetness). I believe the quality score given by the jugdges is linked with their personnal perference or i could depend on other variables which were not provided in white wine datas

I also found the relationship between sugar, density, and alcohol to be interesting and I explored that in detail. The suprising thing for me was that the high quality wines can be characterized by two types of sweetness: medium dry and dry. Actually it's also suprizing in the end that alcohol is very well correlated with wine quality. I would expect that not all the wines with high content of alcohole would be high quality wines. Since the wine quality jugment can be very personal it is possible that juges that gave the scores for the wine in this dataset enjoyed white wines with higher content of alcohol.

This project made me quite interested in the wine quality. I would be very interested to do similar experiment either with red wine dataset or beer dataset.

### Question 2: You are given a ten piece box of chocolate truffles. You know based on the label that six of the pieces have an orange cream filling and four of the pieces have a coconut filling. If you were to eat four pieces in a row, what is the probability that the first two pieces you eat have an orange cream filling and the last two have a coconut filling?

Total number of truffles: 10
6 - cream orange filling
4 - coconut filling
Instruction: eat 4 pieces in a row choosing random truffles 

At the start we are given 10 truffles. 6 of them have orange filling and 4 coconut filling. The probability of selecting cream orange truffle first is 6/10. Now, we have remaining 9 truffles. The probability of selecting 2nd cream orange truffle in a row is 5/9 (there are 5 cream orange truffles and 4 coconut filling truffles left. So, we are left with 8 truffles: 4 that have cream orange filling and 4 that have coconut filling. The probability of selecting truffle with coconut filling is now 4/8. Now we remain only with 7 truffles and probability of selecting another coconut filling truffle is 3/7.
 
(6/10)*(5/9)*(4/8)*(3/7) = 0.0714


Follow-up question: If you were given an identical box of chocolates and again eat four pieces in a row, what is the probability that exactly two contain coconut filling?

There are 14 various combinations of coconut and orange truffes. I will have a lookk now how many variations of set with 2 coconut truffles are possible
O - orange
C - coconut
1: C C O O
2: C O C O
3: C O O C
4: O C C O
5: O C O C
6. O O C C

There are 6 possible combinations of drafting set of 4 truffles with exacly two coconut truffles. The probability of drafting 4 truffles from which exacly two have coconut filling would be 6/14 = 0.42857


### Question 3: Given the table users
  Table "users"
+-------------+-----------+
| Column      | Type      |
+-------------+-----------+
| id          | integer   |
| username    | character |
| email       | character |
| city        | character |
| state       | character |
| zip         | integer   |
| active      | boolean   |
+-------------+-----------+
### construct a query to find the top 5 states with the highest number of active users. Include the number for each state in the query result. Example result:
+------------+------------------+
| state      | num_active_users |
+------------+------------------+
| New Mexico | 502              |
| Alabama    | 495              |
| California | 300              |
| Maine      | 201              |
| Texas      | 189              |
+------------+------------------+Solution for the problem:

SELECT state, sum(active) as num_active_users 
FROM users
GROUP BY state
ORDER BY sum(active) DESC
LIMIT 5
### Question 4: Define a function first_unique that takes a string as input and returns the first non-repeated (unique) character in the input string. If there are no unique characters return None. Note: Your code should be in Python.


```python
def first_unique(string):
    while string != "":
        #assign lenght of string to new variable
        string_len0 = len(string)
        #assign first character of the string to new variable ch
        ch = string[0]
        string = string.replace(ch, "")
        string_len1 = len(string)
        if string_len1 == string_len0-1:
            return ch
            break;
    else:
        return "No answer"

#Test of the algorithm:
#Expected answer p
print first_unique("paaul")
#Expected answer c
print first_unique("aaabbc")
```

    p
    c
    

### Question 5: What are underfitting and overfitting in the context of Machine Learning? How might you balance them?

Overfitting and underfitting are the two biggest causes for poor performance of machine learning algorithms. Overfitting occurs when a statistical model or machine learning algorithm captures the noise of the data and the algorithm fits the data too well. It often happens when the model or algorithm shows low bias but high variance. Overfitting can be prevented by fitting multiple models and using validation or cross-validation to compare their predictive accuracies on test data. Using simpler models with less parameters to tune would also prevent from overfitting. It is also possible to use techniques specific related to models in order to account for overfitting. As an example when linear model is used, regularization can be used to balance overfitting. 

Underfitting occurs when the model or algorithm cannot capture the underlying trend of the data thus fit enought data points. 
Undefited model would have very poor performance in training of the data. To avoid undefitting the number of features should be increased. This includes making new features from existing features.



### Question 6: If you were to start your data analyst position today, what would be your goals a year from now?

I would like to apply for following data analyst position in oil&gas industry:

###### DATA ANALYST in oil&gas industry

Overview

This position is part of an internal data science consulting team responsible for the delivery and support of analytic capabilities for Chevron upstream, midstream, and downstream. The function of this role is to partner with the business to identify opportunities to apply analytic tools and data science to achieve business value. This will include requirements gathering, execution and deployment of new functionality; while providing operational support (troubleshooting, enhancements, bug fixes, etc.) for existing solutions. The successful candidate that fills this position will have the skills to design, prototype, create, and support analytical solutions and insights.
Responsibilities for this position may include but are not limited to:
Builds and maintains strong working relationships with business partners; meeting regularly to understand their business problems and potential analytic needs for solving those problems.
Frames business problems, identify alternatives, and collaborate on solutions with other business analysts, architects, and stakeholders. May include other activities as required, such as development, training, etc.
Applies data science and analytic techniques.
Have working knowledge of tools and concepts in the Hadoop ecosystem
Identifies and frames opportunities to apply advanced analytics, modeling, and related technologies to data, in order to help the business gain insight and improve decision-making, workflow, and automation.

Stays abreast of the Chevron Modeling & Analytics Center of Excellence guidelines and coordinate activities accordingly.
Follows documented processes, standards and guidelines, and make suggestions for improvements and simplifications where needed.

Required Qualifications:

- Bachelor’s degree in Mathematics, Statistics, Analytics, Engineering, Computer Science, or related field
- Minimum of 3 years of directly related experience.
- Demonstrated depth in advanced analytics technologies (e.g., data science, operations research, statistics, data mining).
- Experience implementing advanced analytics projects.
- Proficiency in R, Python, or similar tools.
- Understanding of database design and ability to read and write basic to intermediate SQL.
- Experience in and working knowledge of Oil & Gas industry.
- Ability to learn and understand business workflows and value drivers; then apply technical design and solutions to meet business needs.
- Proven ability to effectively collaborate within the team, across teams, and with business users.
- Ability to engage business and technical experts at all organizational levels and assess opportunities to apply data science and analytics.
- Ability to communicate in a clear, concise, and understandable manner both orally and in writing.
- Ability to listen carefully and asks questions to understand the views, concerns, and comments of others.

Preferred Qualifications:

- Master’s Degree or higher in same areas

If I would start in this data analyst position today, my main goal would be to develop data analytics skills (knowledge of python and R) as well as apply my extensive Oil&Gas expertise (including offshore experience) in solving various industry problems using data analytics and machine learning tools. My goal would be to apply analytic tools and data science to achieve business value and contribute to safety of operations (as safety is number one priority in Oil&Gas industry).

Goals for the first 6 months:
- learn about the company and its assets
- learn what problems company is facing with producing wells in order to find ways optimize producion using data analytics and machine learning
- access if data analytics can be used to improve efficency of wells that will be drilled in future
- learn about company data base system and use SQL to extract and manipulate the data

Goals for next 1-2 years:
- develop hadoop competencies
- code fluently in Python to develop new innovative evaluation metrics for drilling activities,
- Query database and create assumption using offset well data for predictions of pore pressure for newly drilled wells
- perform data wrangling as well as create prective models using machine learning techniques.
- I would like to create predictive maintance models for various offshore platform equipment. The goal of the model would be to predict when the particular piece of equipment needs maintance or adjustment. You need to keep in mind that any offshore intervention or performed maintatance is very costly and normally it is done in predefined periods of times - even if it's not strictly required. I trust that the predictive maitanance model would help to access when the maitanance is required to assure that the equipment is working properly and it would also help to save the costs. As one of the tools in my work I would use Jupter notebook. It can be an excellent solution for a quick evaluation of the status, data processing and sharing of information with other collegues.
- Create predictive modeling that would access future production gas/oil rate using well head pressure and well head temp (and other variables if available) in order to optimize and predict future oil/gas flow rates.




### Reference

- https://stackoverflow.com/questions/15495731/best-way-to-find-first-non-repeating-character-in-a-string
- http://machinelearningmastery.com/overfitting-and-underfitting-with-machine-learning-algorithms/
- http://www.analyticbridge.datasciencecentral.com/profiles/blogs/underfitting-overfitting-problem-in-m-c-learning
- https://en.wikipedia.org/wiki/Overfitting
