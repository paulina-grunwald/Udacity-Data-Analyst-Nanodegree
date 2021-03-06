Design an A/B test by Paulina Grunwald   
========================================================

```{r global_options, include=FALSE}

knitr::opts_chunk$set(fig.width=12, fig.height=8, fig.path='Figs/',
                      echo=FALSE, warning=FALSE, message=FALSE)
```


```{r echo=FALSE,warning=FALSE, message=FALSE}
#Load packages
library(knitr)
library(tibble)
library(tidyr)
library(dplyr)
```



## 1. Experiment Summary

At the time of this experiment, Udacity courses currently have two options on the home page: "start free trial", and "access course materials". If the student clicks "start free trial", they will be asked to enter their credit card information, and then they will be enrolled in a free trial for the paid version of the course. After 14 days, they will automatically be charged unless they cancel first. If the student clicks "access course materials", they will be able to view the videos and take the quizzes for free, but they will not receive coaching support or a verified certificate, and they will not submit their final project for feedback.

In the experiment, Udacity tested a change where if the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated 5 or more hours per week, they would be taken through the checkout process as usual. If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity courses usually require a greater time commitment for successful completion, and suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead. This screenshot shows what the experiment looks like.


The hypothesis was that this might set clearer expectations for students upfront, thus reducing the number of frustrated students who left the free trial because they didn't have enough time-without significantly reducing the number of students to continue past the free trial and eventually complete the course. If this hypothesis held true, Udacity could improve the overall student experience and improve coaches' capacity to support students who are likely to complete the course.

The unit of diversion is a cookie, although if the student enrolls in the free trial, they are tracked by user-id from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.



## 2.Experiment Design

###2.1 Metric Choice

The most important part of any AB test is to identify correct evaluation and invariant metrics. We will come back to evaluate this metric once we get results from out experiment. This will help us do the sanity checks for the experiment. Invariant matrices define the parameters that are not expected to change between the control group and experiment group. The data coming from the invariant metrics should be randomly assigned to the control and experiment groups. Evaluation metric defines the parameters that are expected to change between the control and the experiment group. For my experiment i will choose both invariant and evaluation metric. If the hypothesis is true, the number of user-ids to enroll would be reduced, eliminating the unprepared students, with payments/checkouts not decreasing. The metrics below were considered for this experiment. $d{min}$  is the practical significance boundary for each metric. 

**Number of cookies**: That is, number of unique cookies to view the course overview page. It's a unit of diversion and  it should be randomly assigned to the control and experiment group. ($d{min}$ = 3000)

**Number of user-ids**: That is, number of users who enroll in the free trial. ($d{min}$ = 50)

**Number of clicks**: That is, number of unique cookies to click the "Start free trial" button (which happens before the free trial screener is trigger). The click happens before the person sees the experiment. ($d{min}$ = 240)

**Click-through-probability**: That is, number of unique cookies to click the "Start free trial" button divided by number of unique cookies to view the course overview page. ($d{min}$ = 0.01)

**Gross conversion**: That is, number of user-ids to complete checkout and enroll in the free trial divided by number of unique cookies to click the "Start free trial" button. ($d{min}$ = 0.01)

**Retention**: That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by number of user-ids to complete checkout. ($d{min}$ = 0.01)

**Net conversion**: That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by the number of unique cookies to click the "Start free trial" button. ($d{min}$ = 0.0075) 
 
 
  

####**2.11 Invariant Metric**

I have chosen following metrics as invariant:
**Number of cookies**: The number of unique cookies to view the course overview page. It is a unit of diversion and it will not by affected by the experiment.

**Number of clicks**: The number of unique users/students (unique cookies) that click on the "start free trial" button. Here the button is clicked prior to the free trial screen appearing.

**Click-through-probability**: The number of unique cookies to click on the "start free trail" button divided by the number of unique cookies to view the course overview page.



####**2.12 Evaluation Metric**

Before we start the experiment we need to choose the evaluation metric that we are going to track. We expect to change in them. In case of our test we want to decrease the enrollment of students that can not commit enought time or are unprepeared. This means that the gross conversion should decrease but number of students who complete the free trial and make a payment should not decrease (the net converion should either stay the same or preferably increase).

**Gross conversion**: The number of user-ids that enroll in the free trial divided by the number of unique cookies to click on the "start free trial" button. The number of enrollments can be affected by the experiment and as a result the gross conversion. I will use gross conversion as an evaluation metric. Out hypothesis is that there should be a statisticial significant reduction in enrollment.

**Retention**: The number of user-ids that stayed enrolled past the 14 day free trial (and made a payment for the course) divided by the number of unique cookies that clicked on the "start free trial" button. It is possible that the the retention (number of payments) might by affected by our experiment thus i will choose retention as an evaluation metric.

**Net conversion**: The number of user-ids to remain enrolled past the 14 day free trial (made a payment) divided by the number of unique cookies that clicked on the "start free trial" button. The number of payments can be affected by the experiment and as a result the net conversion, this will be used as an evaluation metric. There should be a statisticial significant increase in payment/continued enrollment after the free trial.

I have decided not to use following metrics in my experiment:

**Number of User-Ids**: The number of users who enrolled in the free trial. This metric can not be consider as invariat metric because it is expected to change between control and experiment group. I have decided not to use this metric because gross conversion already reflects number of id users (as a fraction of unique users not as a count) and I think it would better suit our experiment.

The hypothesis for the experiment is following:
- Since students will be will be informed by the new screener how much time they need to dedicate for the course we would expect that the gross conversion will decrease (less students will start 14 days trail). 
- Net conversion should not decrease. If the net conversion decreases then the experiment should not be launch. If on the other case net conversion stays the same or increases this would mean that we can launch out experiment.
- Retnetion and net conversion should not decrease. If they decreases then the experiment should not be launch. If on the other case net conversion stays the same or increases this would mean that we can launch out experiment.

If our hypothesis is correct we are looking for the following results in order to launch the experiment :
- gross conversion  decreases as students that do not have enought time to study would not join free trial due to the information included in the screener,
- net conversion will stay the same or incease. Many students that joined the course were enought motivated during registration that screener would not change their decision on enrolling in the course after 14 days trial so net conversion would stay the same. There is also chance that the net conversion icreases (additional students who otherwise wouldn't join the course decided to join free trial after seeing the screener) by any chance it would be very positive for our experiment and then we would launch the change on the website.
- retention will stay the same or increase. The situation with retention is exacly the same as with the net conversion. The retention and net conversion measure the same goal. 


Later on we will assess those metric to see if any change occured and if we can confirm the hypothesis.

## 2.2 Measuring Variability (stadard deviation)

Before running the a/b test on Udacity website number of baseline data needs to be gather.The below presented table contains estimates of the baseline values for invariant and evaluation metrics.

```{r , load_data}
setwd("C:/Personal/GitHub/Udacity-Data-Analyst-Nanodegree/Project 7 - Design an AB Test")
baseline_values <- tbl_df(read.csv('baseline_values.csv', header = FALSE, colClasses = "character"))
baseline_values
```

For each evaluation metric i have chosen, I will estimate its standard deviation analytically given a sample size of 5000 cookies visiting the course overview page. The standard deviation is computed using formula $\sigma = \sqrt{\frac{p(1-p)}{n}}$ where p stands for probability and n for number of samples taken.

Sample size of 5000 cookies can be calculated by dividing unique cookies to view the page per day - 40,0000 by 8: 40,000/8 = 5000
Taking this into the consideration we can calculate unique clicks on start free frial per day (assuming 5000 unique page views per day of 40,000):  $\frac{3200}{8}$ = 400

We can use the same method for the enrollents per day: $\frac{660}{8}$ = 82.5

We will use those values for calculating standard devition for the evaluation metric chosen before given a sample size of 5000 cookies visiting the course overview page.
 
 
**1. Gross conversion** 

For calculating standard deviation of gross conversion i will use probabity of enrolling given a click (which is equal to 0.20625). I will first calculate standard deviation for gross conversion corresponding to 3200 unique clicks on start free trial and 40000 unique views of page per day. 
$\sigma_{gc}$ = $\sqrt{0.20625*\frac{(1-0.20625))}{3200}} = 0.00715$  
For 50000 pageviews we can calculate standard deviation in following way:  
$\sigma_{gc}$ = $\sqrt{0.20625*\frac{(1-0.20625))}{400}} = 0.0202$ 
 
 
**2. Retention** 
Now i will calculate standard deviation of retention($\sigma_{r}$). We can recall from the table displayed above that probability of payment given a click is equal to 0.53. 
$\sigma_{r} = \sqrt{\frac{0.53(1-0.53)}{82.5}} = 0.0549$
 
 
**3. Net conversion** 

The last step is calculating standard deviation for net conversion $\sigma_{nc}$. Probability of payment given a click is equal 0.1093125.
$\sigma_{nc} = \sqrt{\frac{0.1093125(1-0.1093125)}{400}} = 0.0156$

The table below shows the summary of calculated standard deviations for evaluation metric:
 
```
| Evaluation Metric     | Calculated $\sigma$| 
|:----------------:|:-------------:| 
| Gross conversion | 0.0202        |        
| Retention        | 0.0549        |
| Net conversion   | 0.0156        | 
```
 
 
Gross Conversion and Net Conversion use number of cookies as denominator, which is also unit of diversion. Since in this case the diversion is equal to unit of analysis, the analytical estimate would be comparable to the emperical variability. This is not the case for the retention. The denominator for the retention variable is users enrolled per day. Since the unit of diversion and unit of analysis are not the same then the empirical and analytical estimates would be different. 

 
 
###3. Sizing

####3.1 Choosing Number of Samples given Power

Using the analytic estimates of variance I will calculate how many pageviews total (across both control and experimental) would be needed to collect to adequately power the experiment. I will use an alpha $\alpha$ of 0.05 and a $\beta$ of 0.2. I will use Evan Miller's (http://www.evanmiller.org/ab-testing/sample-size.html) calculator to calculate required number of pages views for the experiment.

For my calculation I will use:  
- $\alpha$  (significance levek) = 0.05  
- $\beta$ = 0.02 (statistical power (1-$\beta$) = 0.8  
- unique clicks/unique page views: $\frac{3200}{40,000}$ = 0.08  
- enrollments per day/ unique page views = $\frac{660}{40,000}$ = 0.0165  

The minimum difference that we actually care about for our buisness perspective are following: 
- $d_{min(gc)}$ = 0.01  
- $d_{min(r)}$ = 0.01  
- $d_{min(nc)}$ = 0.0075  
 
 
**Gross conversion** 

20.625% base conversion rate and $d_{min(gc)}$ = 0.01  
Samples needed: 25,835  
Total page views needed: $n_{gc}=(\frac{25,835}{0.08})*2$ = 645,875  


**Retention** 

53% base conversion rate and $d_{min(gc)}$ = 0.01  
Samples needed: 39,087  
Total page views needed: $n_{r}=(\frac{39,087}{0.0165})*2$ = 4,737,818.18  


**Net conversion:** 

10.93125% base conversion rate, $d_{min(gc)} = 0.0075$   
Samples needed: 27,413    
Total page views needed: $n_{nc}=(\frac{27,413}{0.08})*2= 685,325$ 

The largest sample size would be required for retention. The number is quite big and if this metric would be choosen for our experiment the test would be very long.




##Choosing Duration vs. Exposure


It's important to determine to translate our ideal size of the experiment into practical terms. For this duration, time of running the experiment and what fraction of the traffic would be send to the experiment. The number of the exposted users to the experiment will be related to the risk that it brings. You want to make sure that user will not get flustrated with the new feature. In case of our experiment the change is rather minor and most likely not bringing a lot of risk. This mean that we can divert majority of our traffic to the experiment.

I will exclude retention as an evaluation metric as it requires too many pages views to complete experiment. The only limitation regarding pageviews in this experiment will be net conversion(685,325 pageviews). If we would divert 100% of traffic to the experiment then it would take approx. 18 days to complete. In my opinion the experiment is not risky. We are not dealing with the sensitive data and nobody can get hurt due to this experiment. I don't mind to divert 100% of trafic to my experiment but i have decided divert 75% of the traffic instead. Divering 75% of traffic it means we will finish our experiment in: 685325/(40,000*0.75) = 23 days.23 days is just over three week times. This would assure that we have at least three weekends and weekdays of three weeks (we would have good grip of comparision of the traffic between weekend and weekdays). The experiment should also be run outside of any holiday days at those affect heavily trafic and user patterns. I trust that 23 days experiment would bring us better view on the data over the course of weekend and weekdays.


##3.Experiment Analysis

Control and Experiment [dataset](https://docs.google.com/spreadsheets/d/1Mu5u9GrybDdska-ljPXyBjTpdZIUev_6i7t4LRDfXM8/edit#gid=0) provided by Udacity and used throughout this section.  


###3.1 Sanity Check

After we're getting the results of the experiment, we can't directly interpret the results. We have to do sanity checks. It can be many things. What we need to do is to check the invariant metric. We can use unit of diversion and population to determine comparable results for both experiment and control. The invariant metric shoulld not change between control and experiment group. After you have running all sanity checking including invariance metric, it only then you can do complex analysis based on the results of your experiment.

First we will look at the comparision of cookies/pageviews between control and experiment group.

**Number of cookies(pageviews)**

Total pageviews in control group: 345,543  
Total pageviews experiment group: 344,660  
Total pageviews (in control and experiment group): 690,203  
$\alpha$ = 0.05  
Z (z score of the confidence level)  = 1.96  
p (probability of diverting cookie in control or experiment group) = 0.5  

SE = $\sqrt{\frac{0.5*(1 - 0.5)}{345543 + 344660}} = 0.006$  
m (margin of error) = SE * 1.96 = 0.0012  
CI (confidence interval) = [0.5-m, 0.5+m] = [0.4988, 0.5012]  
Observed value = $\frac{344,660}{690,203}$ = 0.50  
This invartiant metric passes sanity check.  


**Number of clicks**

Total Control group clicks: 28,378  
Total Experiment group cliks: 28,325  
Total pageview (in control and experiment group): 28378 + 28325 = 56703  
$\alpha$  = 0.05  
z = 1.96  
p =  0.5 (probability of diverting clicks in control or experiment group)  
SE = $\sqrt{\frac{0.5*(1 - 0.5)}{28378 + 28325}} = 0.0021$ 
m = SE*1.96 = 0.0041  
CI = [0.5-m, 0.5+m] = [0.4959, 0.5041]  
Observed value = $\frac{28,378}{56703}$ = 0.5005

This invartiant metric passes sanity check.

**Click through rate** 

$CTR_{c}$ =\frac{28378}{345543} = 0.0821
SE = $\sqrt{\frac{0.0821*(1 - 0.0821)}{344660}} = 0.000468$  
m = SE*1.96 = 1.96 * 0.000468 = 0.00091728
CI = [0.0811, 0.0830]

$CTR_{exp}$ =\frac{28325}{344660} = 0.0822

This metric passes sanity check. The observed value is within the bounds.

We can see that the total number of the unique page views for control and experiment groups are very close to each other. From above performed calculations we can observe that cookie/pageviews and clicks and click through rate pass the sanity check. Moreover the click through probability passes the sanity check.


##4. Result Analysis

In this part of my analysis i will indicate whether each metric is statistically and practically significant  given 95% confidence interval around the difference between the  control and experiment groups.

$\alpha$  = 0.05  
Z = 1.96
 

**Gross Conversion**
 
```
|                  | Control Group | Experiment Group|
|:----------------:|:-------------:| ---------------:|
| Clicks           | 17,293        | 17,260          |
| Enrollments      | 3785          | 3423            |
```

$gc_{c} =\frac{3785}{17,293}$ = 0.21897 

$gc_{exp} =\frac{3423}{17,260}$ = 0.19832 

$\widehat{d}$ = $gc_{exp}$ - $gc_{c}$ = 0.198319815 - 0.218874689 = -0.020554874 

$\widehat{p}_{pool}$:$\frac{3423+3423}{17293+17,260}$ = 0.208607 

$SE_{pool}$ = $\sqrt{0.208607*(1-0.208607)*(\frac{1}{17,293}+\frac{1}{17,260})}$ = 0.004371675 

m (margin of error) = $SE_{pool}$ * 1.95 = 0.004371675 * 1.95 = 0.00852476625 

CI (at 95% confidence) = [-0.020554874 -m, -0.020554874 + m] = [-0.0291, -0.0120] 
The confidence interval doesn't contain 0. It is both statistically and practically significant. 


**Net Conversion**
```
|                  | Control Group | Experiment Group|
| ---------------- | ------------- | --------------- |
| Clicks           | 17,293        | 17,260          |
| Enrollments      | 2033          | 1945            |
```
$nc_{c} =\frac{2033}{17,293}$ = 0.1175620193 

$nc_{exp} =\frac{1945}{17,260}$ = 0.1126882966 

$\widehat{d}$ = $nc_{exp}$ - $nc_{c}$ = 0.1126882966 - 0.1175620193 = -0.0048737227 

$\widehat{p}_{pool}$:$\frac{2033+1945}{17,293+17,260}$ = $\frac{3978}{34,553}$ = 0.1151274853 

$SE_{pool}$ = $\sqrt{0.1151274853*(1-0.1151274853)*(\frac{1}{17,293}+\frac{1}{17,260})}$ = 0.003434133513 

m (margin of error) = $SE_{pool}$ * 1.95 = 0.00673090168548 

CI (at 95% confidence) = [-0.0048737227 -m, -0.0048737227 + m] = [-0.0116,0.0019] 

Net conversion CI: (-0.0116, 0.0018)
- not statistically significant (CI contains zero)
- not practically significant (lower bound of CI interval is - 0.0075)
 
 
  
###4.1 Sign Tests 
 
 
I have conducted binominal sign test. I have compared the values from the experiment to asses the difference between th control and experimental group. The goal was to see if the difference was positive or negative. Positive difference was counted as a sucess and negitve as a failure. The results can be seen in the table below:
 
 
 
```
|                  |Number of success  |Number of trials|Probability|Two-tailed p-value|
|:----------------:|:-----------------:|:--------------:|:---------:|:----------------:|
| Gross Conversion | 4                 | 23             |0.5        |0.0026            |
| Net Conversion   | 10                | 23             |0.5        |0.6776            |
``` 


Gross conversion has p value of 0.0026 which is less than the alpha level of 0.025 This mean that data from our analysis is statistically significant. 
Net conversion has p value of 0.6776 which is much more higher than alpha level of 0.05. This mean that this metric is not statistically significant. 


###4.3 Summary
 
I have decided not to use Bonferroni correction. In general the Bonferroni correction is used to add correction to the experiment whre multiple metrics are tracked but only in the case when some of them need to be significant in order to launch the change.

Our experiment requires ALL metrics (gross conversion and net conversion) to be partically significant in order to decide to implement changes on the website. According to udacity coach Sheng Kung (Udacity forum) "The Bonferroni correction is an easy way to set your decision-making at an appropriate level if you only need one significant metric." So in our case if we would use OR condition on the metrics, then using Bonferroni correction would make sense. If we would use Bonferroni correction then p would be equal to 0.025. 

I believe that adding this correction would be too conservative (we are already quite conservative by requiring both metrics to be significant) due to the fact that the metrics in the test have high correlation. They also both use user-id and cookie (which can be correlated). Moreover, I think that it is better to make decision on introducing the change on the website taking into the consideration significance of rather two than one metric.  

It can be also mentioned that analysis of the results from effect size and sign test showed that gross conversion is statistically significant. This means that the number of students starting 14 days trial was reduced. This is exacly what was the expectation. Assumption was that if the students understand better time commitment required for the course it would discourage students that don't have enought time. The result is in line with our initial hypothesis. 

Looking at the results of the test we can observe that net conversion rate dropped by 0.05% (from 0.1175620193 to 0.1126882966) between control and experiment group. The decrease is not statistically significant at 95% CI (and thus not practically significant). Moreover,the lower end of the CI is below the practical significance threshold which brings us quite some concern. The lower of the CI for net conversion -0.0116 which is relatively close to - 0.0075 but still lower than -0.0075.  The reduction of net conversion is not in line with the initial hypothesis (our hypohesis was that net conversion will will stay the same or increase). The reduced number of students that enrolled in the course after finishing 14 days trialc could have been caused by the fact that students realized that they do not have enought time to continue with the study. They probably understood during the 14 days trial that the estimated time required for the course (that was mentioned in the screener) was accurate. The dropping rate of net conversion (which could have been caused by the screener) is exacly what we did not want. 

###4.4 Recommendation

The goal of the experiment was new message after clicking on "start free trial" was tested. The new message window seem to work to reduce number of students that would start 14 days trial. The number of students enrolling in the trial (gross conversion) was lower as expected.
It is also possible the number of students continuing study after 14 days trial (net conversion) decrased by an amount that would be important for the buisness (the result for net conversion was not statistically significant so we cannot be sure if it was affected negatively in our experiment with statistical certainty). Our hypothesis called for the net conversion to remain the same or increase but the results of the analysis showed that there is possible decrease. The potential decrease of the net conversion is not acceptable. Taking into the consideration I trust that we should not launch the test.


##Follow-Up Experiment

I think in order to increase student motivation and engagment in the course, number of improvements can be added to the website. I think it would be an interesting feature to build into the website pomodoro timer so students can track how much time they spend on various course's parts. Pomodoro technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. I found that measuring time of my studing helped me to be more accontouble for myself and stay more engaged. If Udacity could track in this way (or similar) the time students spend on the courses and assigments, then it would possible to give prompts to the students if they did not spend enough time studing. I trust that it would help students to be more engaged and aware of their own progress. 

My hypothesis that the promts from Udacity tutors together with the time tracker for study progress would motivate students who might otherwise drop out during the 14 day trial. As a unit of divsersion i would choose user-id since students that are enrolled in 14 days trial are tracked by the user-id. The students that are enrolled in 14 days trial could be split into control and experimental group. 

Invariant metric would be user id (unit of diversion is user-id) because the experiment will be performed after the users are logged in. The appropiate evaluation metric would be retention rate. We have to keep into the account that if we choose retention as an evaluation metric the experiment may take quite some time (as showed in my experiment).


##References
- Evan Miller's calculator (%http://www.evanmiller.org/ab-testing/sample-size.html)
- https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
- http://rajivgrover1984.blogspot.nl/2015/11/ab-testing-overview.html
- Udacity A/b test course
- https://en.wikipedia.org/wiki/Bonferroni_correction
- https://stats.stackexchange.com/questions/154542/what-exactly-is-multiple-testing-bonferroni-correction-can-i-use-it-with-a-si


