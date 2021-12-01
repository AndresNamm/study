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

+ The main idea is that due to CLT we can say that the samples will surround the global mean in a normal distribution. Means that we can use the empirical rules to derive confidence levels that say for example that 95 % of the samples will be around the global mean with SE  (global standard deviation) / sqrt(number of samples)
![image](https://user-images.githubusercontent.com/21141607/144257774-adfb2ec2-cf78-415c-a7fa-f8f5ef77681e.png)



