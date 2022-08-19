# Z TEST

Z=(Sample Mean - Assumed mean)/SE

Where SE is the standard deviation of the means over many samples based on CLT = std/sqrt(n)


![img](https://www.six-sigma-material.com/images/xMeanComparisonTable.jpg.pagespeed.ic.ANRLAM5qed.jpg)


# COMPARING 2 SAMPLES 

https://www.coursera.org/learn/stanford-statistics/lecture/nQB9A/the-two-Tsample-z-test

+ Often you need to compare 2 samples with each other. E.g. take samples from 2 distributions. Here you need to calculate the difference and see if its possible that the difference is likely if the data would come from the same distribution. Here we have to use the pooled standard deviations and assume the sample sizes for both datasets are the same. 

![image](https://user-images.githubusercontent.com/21141607/171132178-d7912a9f-e8bf-4a44-aeec-558c281fdabf.png)

[CI for Binomial](https://sigmazone.com/binomial-confidence-intervals/)

# T TEST 

 t-test is a special form of Z test that has a small sample size and also if there is no previous information about the standard deviation. I has lower center and wider tails. E.g. when performing significance test, the 95,99 percentile are further from the mean due to potentially wider sample error. 
 
 + [Written Example of t-test](https://www.scribbr.com/statistics/t-distribution/)
 + [Coursera tutorial on t-test](https://www.coursera.org/learn/stanford-statistics/lecture/jYVrt/the-t-test)
