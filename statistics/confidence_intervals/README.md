
# REFERENCES

Recommended orded to go through this subtopic:

## Confidence Intervals & T-Tests

+ [_Slide_ summary introduction to Confidence Intervals topic](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/CONFIDENCE%20INTERVALS.pdf)
+ _Tutorial_ introduction to confidence intervals with Video -> On this page below
+ [_Tutorial_  Explanation of Standard Deviation](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/STD_dive.md)
+ [Types of t-tests](https://www.wallstreetmojo.com/t-test/)
+ [_Code_ introduction to the Confidence Interval topic + t test 1 sample](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/examples/conf_interval.ipynb) 
+ [_Tutorial_ comparing 2 samples t-test](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/hypothesis_testing.md)
+ [_Tutorial_ Random Variables](https://github.com/AndresNamm/study/blob/main/statistics/random_variables.md)
+ [_Code_ Bernoulli distribution and Confidence Intervals](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/examples/binary_conf_interval.ipynb)


## Power Analysis

+ [_Tutorial_ Intro](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/power_analysis.md)
+ [_Power Analysis visualization 2 samples_](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/PowerAnalysis.pdf)

# CI EXPLANATION

I have provided some references and short explanations but in general I really recommend you to google your own tutorials that fit the best for the way you understand things. 



# ME GOING OVER THIS TOPIC IN YOUTUBE

+ [First video](https://www.youtube.com/watch?v=yO8x4eyEp6o)
+ [Second video](https://www.youtube.com/watch?v=xIB3rAoWSbE)

# THINGS TO GO THROUGH IN ORDER TO PROPERLY UNDERSTAND THIS TOPIC

## TOPIC_ORDER 

1. Normal Distribution
2. [Standard Deviation](#std)
3. Standard Normal Distribution 
4. Z score, Z value 
5. [Central limit theorem](#clt)
6. [What IS Confidence interval ](https://www.mathsisfun.com/data/confidence-interval.html) [My own explanation](#confidence-interval)
7. [Intuitive explanation of confidence interval which also explains p-value](https://www.youtube.com/watch?v=TqOeMYtOc1w)
8. [Derivation of Confidence interval](https://online.stat.psu.edu/stat415/lesson/2)
# CLT

The proof for central limit theorem is very theoretical and we wont cover it here but the result of CLT is that x samples with Size N point estimates will have a normal distribution around the global mean and standard deviation as (global standard deviation) / sqrt(number of samples) . [Reference to a good explanation](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Probability/BS704_Probability12.html#:~:text=The%20central%20limit%20theorem%20states,will%20be%20approximately%20normally%20distributed.)

![img](CLT.png)


# STD 

![img](STD.png)

# Confidence Interval

With a confidence interval we have a lower bound L and upper bound U and we claim that we are X percent sure that the global estimate lies in this bound. [look at the example here](https://www.mathsisfun.com/data/confidence-interval.html)


I also suggest to look [Coursera statistics course confidence intervals topic](https://www.coursera.org/learn/stanford-statistics/home/week/5)


+ N = number of samples / This is rather a theoretical construct. When it goes to infinity, the means of those N samples will converge to **global** mean
+ n = sample sizee

The main idea is that due to CLT we can say that the N sample means with size will surround the global mean in a normal distribution. This result that we can use the empirical rule to derive confidence levels that say for example that 95 % of the means of samples with size n will be around the global mean. In this case the STD for those means would be  
(global standard deviation) / sqrt(n)      
![image](https://user-images.githubusercontent.com/21141607/146001843-b7d525f0-2c7f-462b-8780-873ee839861f.png)

![image](https://user-images.githubusercontent.com/21141607/144257774-adfb2ec2-cf78-415c-a7fa-f8f5ef77681e.png)



