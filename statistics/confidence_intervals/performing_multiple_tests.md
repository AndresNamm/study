# Bonferroni Correction 


[explanation](https://toptipbio.com/bonferroni-correction-method/)

## BACKGROUND - T TESTS

If we have alpha lets say = 0.05. This means we reject the null hypothesis whenever we see a result that under the normal curve falls so far from expected that it has only a 5 % chance of happening assuming H0 is true. 

## BONFERRONI CORRECTION

Now what happens if we do multiple experiments with this data? In this case the likelyhood of getting some observation that is in this 5 % is getting bigger. To avoid that we divide tha alpha with the number of experiments conducted. 

# FDR (False Discovery Ratio)

Main aim is to keep the FDP (False Discovery Percentage as Small as Possible)

+ **before you dive into the topic** These videos are going to talk about P value distribution. This question answer from [Stefan explains how this works](https://stats.stackexchange.com/questions/10613/why-are-p-values-uniformly-distributed-under-the-null-hypothesis/481843#481843?newreg=081171011c3e48a293391a012ef9fab5) 
+ [Good tutorial 1 ](https://www.youtube.com/watch?v=rZKa4tW2NKs&t=33s)
+ [Good tutorial 2](https://www.youtube.com/watch?v=K8LQSvtjcEo)
+ FDP = False Discoveries / Total Discoveries (False Discoveries + True Discoveris)
+ More Or less The idea for FDR is that we set a linear function as the boundary for p-values. This linear function based on alpha will have an average value less then alpha. Which means that the p-values will be distributed so that False Discovery ratio will be on average less than alpha . Somethin like that. Read mor about function average values [here](https://www.khanacademy.org/math/ap-calculus-ab/ab-applications-of-integration-new/ab-8-1/v/calculating-function-average-over-interval)



## EXAMPLE 

![image](https://user-images.githubusercontent.com/21141607/155094467-2428f9e7-003a-4bba-8ca3-7deee7529ba4.png)
*The above image might be a bit confusing

In the example above we have 
+ 1000 tests 
+ 900 times H0 is correct
+ 100 times H1 is correct 
+ We do true discoveries 80 times - In real life we can't really get this number but we can get the number of total discoveries.  
+ We do false discoveries 41 times - **Based on how many tests we do we should be able to approximate this.** 


For example if we conduct 1000 tests with alpha=0.05 we can be sure arount 50 of those tests will have an outcome that rejects H0 even if its correct. Now if get in total 141 rejections we can be assume 50 (or in this case 41) of those discoveries are false.    

Thus **FDP=41/121**


Benjamin Hochber method tries to keep FDP under control when doing multiple tests

![image](https://user-images.githubusercontent.com/21141607/155096527-fbb0260b-80cb-462c-a06c-81af388c782e.png)


+ Example of calculating FDR values in Excel. https://www.youtube.com/watch?v=S-F_R_WKNfQ

## P-VALUE DISTRIBUTION QUESTIONS 

+ http://varianceexplained.org/statistics/interpreting-pvalue-histogram/
+ https://stats.stackexchange.com/questions/10613/why-are-p-values-uniformly-distributed-under-the-null-hypothesis/481843#481843?newreg=081171011c3e48a293391a012ef9fab5