

Taking a confidence interval for mean is taking a sample of Random Variables X and then taking a mean of that sample. This mean based on CLT will have the globl mean $\mu$ and standard deviation $\frac{\overline{\sigma}}{\sqrt{n}}$ where $\overline{\sigma}$ can be the standard deviation from literature review, a bootstrapped example or some other estimation. 

# BINOMIAL CASE 

In the case of binomial data the Random variable X is the number of successes (usually denoted as k) in n trials. Does this then mean that our sample is then multiple such experiments?

Lets say I try to generate a confidence interval for the how many of the covid test results in each day were positive. In this case
+ Tests done is n
+ Number of positive tests is k
+ Assume that ${\overline{\sigma}}$ we have from previous literature review

Do I then calculate the confidence interval so that 

CI=sample_mean +/- Z * $\frac{\overline{\sigma}}{\sqrt{n}}$

+ In this case I can take the n as the size of each experiment. But I think this goes against the logic of CLT as in this case actually the sample should be over Random variables X..Aka many different experiments. Which means I would need to take n as the number of experiments. For example over consecutive days. 

# BERNOULLI CASE 

+ For bernoulli case the X can be 0 and 1 
+ I can take a sample with size 100000 and then continue with the sample size N =100 
+ CI is still=sample_mean +/- Z * $\frac{\overline{\sigma}}{\sqrt{n}}$



# REFERENCES

+ https://stats.stackexchange.com/questions/82720/confidence-interval-around-binomial-estimate-of-0-or-1
+ https://projecteuclid.org/journals/statistical-science/volume-16/issue-2/Interval-Estimation-for-a-Binomial-Proportion/10.1214/ss/1009213286.full