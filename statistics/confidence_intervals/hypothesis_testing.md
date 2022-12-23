# Z TEST

Z=(Sample Mean - Assumed mean)/SE

Where SE is the standard deviation of the means over many samples based on CLT = std/sqrt(n)


![img](https://www.six-sigma-material.com/images/xMeanComparisonTable.jpg.pagespeed.ic.ANRLAM5qed.jpg)


# COMPARING 2 SAMPLES 

+ [Khan Academy tutorial](https://www.khanacademy.org/math/ap-statistics/xfb5d8e68:inference-quantitative-means/two-sample-t-test-means/v/two-sample-t-test-for-difference-of-means)
+ [Coursera "Intro to Stats" Great intro to this topic](https://www.coursera.org/learn/stanford-statistics/lecture/nQB9A/the-two-Tsample-z-test)

+ Often you need to compare 2 samples with each other. E.g. take samples from 2 distributions. Here you need to calculate the difference between 2 means. And see if the difference is likely to happen considering the SE (std) of possible differences. 

![image](https://user-images.githubusercontent.com/21141607/171132178-d7912a9f-e8bf-4a44-aeec-558c281fdabf.png)


**Using pooled vs unpooled std**


+ In the video, the population variances are assumed to be unknown and UNEQUAL. This means we won't be pooling the std-s together to make the SE smaller. 
    + The formula for non-pooled std is $\sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}$
    + Just basically adding up 2 std-s with a geometric sum. 
+ A pooled standard deviation is used when we assumed we don't know the population variances bu we assume they are EQUAL. This helps to get the SE smaller as we estimate the std based on bigger sample. **This formula is however not used too much in practices according to Stanford Stats course**
    + The formula for pooled std is $\sqrt{\frac{(n_1-1)\sigma_1^2 + (n_2-1)\sigma_2^2}{n_1+n_2-2}}$


[CI for Binomial](https://sigmazone.com/binomial-confidence-intervals/)

# T TEST 

 t-test is a special form of Z test that has a small sample size and also if there is no previous information about the standard deviation. I has lower center and wider tails. E.g. when performing significance test, the 95,99 percentile are further from the mean due to potentially wider sample error. 
 
 + [Written Example of t-test](https://www.scribbr.com/statistics/t-distribution/)
 + [Coursera tutorial on t-test](https://www.coursera.org/learn/stanford-statistics/lecture/jYVrt/the-t-test)
