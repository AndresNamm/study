
# %% [markdown]
# # Confidence Intervals
# + [Quick Reference to my fantastic CI tutorial](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/CONFIDENCE%20INTERVALS.pdf)
# + [This code is based on this blog post](https://towardsdatascience.com/how-to-calculate-confidence-intervals-in-python-a8625a48e62b)    
#
# We are taking the data from Uniform distribution. 
# According to the Central Limit Theorem (CLT). Means of any distribution will follow a normal distribution.
# with std of $\frac{\sigma}{\sqrt{n}}$ where n is the sample size and $\sigma$ is the global std which usually is estimated by sample std. 
# If we can say (based on CLT) that the sample means center around the global mean with std $\frac{\sigma}{\sqrt{n}}$ then based on the characteristics of normal distribution
# we can also say that that 66 % percent of the means are +/- 1 std away from the global mean. ~95 % is ~2 std away from the global mean and ~99% means is 3 std away from global mean.
# Thus if we have the sample mean and based on the sample size and sample std, the std for the sample means, we can now say the interval where (66%,95%,99%) of the means should be located. 


# %%
import numpy as np 
from scipy.stats import t,norm
import math
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class ConfidenceInterval:
    mean:float
    lower_bound:float
    upper_bound:float
    test_type:str 
    extremum_val:float
    def get_size(self)->float:
        return self.upper_bound-self.lower_bound
    def print_statistics(self):
        print(f"Test type: {self.test_type}")
        print(f"Median: {self.mean}")
        print(f"Min boundary {self.lower_bound}")   
        print(f"Max boundary {self.upper_bound}")
        print(f"{self.test_type} val: {self.extremum_val}")
        print(f"Width is {self.get_size()}" )

def calculate_confidence_interval(sample_mean,sample_std,sample_size,confidence,test_type)->ConfidenceInterval:
    alpha=1-confidence    
    # Only thing that is different for t and z confidence intervale is the extremum value
    if test_type == "t":
        degrees_of_freedom=sample_size-1
        extremum_val=float(np.abs(t.ppf(alpha/2,degrees_of_freedom))) # t_val - based on confidence we have chosen, how many standard distributions is the ci width. If Confidence is 95%, then std is  ~2
    elif test_type == "z":
        extremum_val=float(np.abs(norm.ppf(alpha/2))) # z_val - based on confidence we have chosen, how many standard distributions is the ci width. If Confidence is 95%, then std is ~2.  
    else:
        raise Exception("Wrong test type provided")
    
    clt_based_std = sample_std / math.sqrt(sample_size) # The std for sample means. Calculated based on CLT 
    max_expected_difference = extremum_val *  clt_based_std # std * (how many stds based on chosen confidence interval size)
    return ConfidenceInterval(mean=sample_mean,lower_bound=sample_mean-max_expected_difference,upper_bound=sample_mean+max_expected_difference,test_type=test_type,extremum_val=extremum_val)



def perform_comparison(sample_size:int, confidence:float):
    # Generate sample data from uniform distritubution on the range 0..100
    x = np.random.uniform(size=sample_size) 
    x_positive = x-min(x)
    x_scaled = x_positive/max(x_positive)*100
    x = x_scaled
    # Calculate confidence intervals based on both Normal distribution (Z val) and t distribution (t val)
    ci_z=calculate_confidence_interval(sample_mean=x.mean(),sample_std=x.std(),sample_size=sample_size,confidence=confidence,test_type='z')
    ci_t=calculate_confidence_interval(sample_mean=x.mean(),sample_std=x.std(),sample_size=sample_size,confidence=confidence,test_type='t')
    return x, ci_z, ci_t



#%% [markdown] Lets perform 1 sample experiment with data generated from Uniform distribution. 

#%%
SAMPLE_SIZE=5
CONFIDENCE=0.99
x, ci_z, ci_t = perform_comparison(sample_size=SAMPLE_SIZE,confidence=0.95)
print(f"Sample size: {SAMPLE_SIZE}, Sample std: {x.std()}, Confidence {CONFIDENCE}, Max value {max(x)}, Min value: {min(x)}")


# plt.text((m+s)*1.1, max_ylim*0.9, 'Mean+Std: {:.2f}'.format(m+s)) 
# plt.text((m-s)*1.1, max_ylim*0.9, 'Mean+Std: {:.2f}'.format(m-s)) 

ci_z.print_statistics()
ci_t.print_statistics()
print(f"Differences in CI size ci_t-ci_z {ci_t.get_size()-ci_z.get_size()}")

# PLOT THE GENERATED DISTRIBUTION X

def plot_default_histogram(x,bins=40,start=0,end=100):
    counts, bins = np.histogram(x,bins=bins)
    plt.hist(bins[:-1],len(bins)-1,weights=counts,range=(start,end))
    plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=1)
    # plt.axvline(m+s, color='r', linestyle='dashed', linewidth=1)
    # plt.axvline(m-s, color='r', linestyle='dashed', linewidth=1)
    min_ylim, max_ylim = plt.ylim()
    plt.text(x.mean()*1.01, max_ylim*0.95, 'Mean: {:.2f}'.format(x.mean())) 

plot_default_histogram(x)

# %% [markdown]
# Now we perform this experiment 1000 times and see how the distribution of means will look like. E.g. we take the sample with size sample_size (set above) and we do this 1000 times. 
# Then we plot the means of these 1000 samples. Based on the Central Limit Theorem (CLT) this distribution should now be a normal distribution with ~ global mean and the standard distribution 
# $\frac{\sigma}{\sqrt{n}}$ where $\sigma$= Global STD (Can be estimated by sample std/Bootstrapping)  and n is sample size for 1 sample. 
# **PS! In reality we almost always limit our experiment with taking 1 sample only. The 1000 sample setup only aims to showcase 
# how Central Limit Theorem turns any distribution (in this case Uniform) into Normal Distribution (With smaller samples t distribution) with sample mean as the global mean and std $\frac{\sigma}{\sqrt{n}}$ **


# %% 
means = []
for i in range(1000):
    x, ci_z, ci_t = perform_comparison(sample_size=SAMPLE_SIZE,confidence=0.95)
    means.append(x.mean())

means = np.asarray(means)
plot_default_histogram(means,bins=50,start=30,end=70)
#%% [markdown]    
# Lets now take a few additional  samples to show how we derive the confidence interval from 1 sample. 
# **Run this cell at least 5 times to see how the confidence intervals are generated for each sample**
# **ADDITIONAL SAMPLE 1 COMPARED TO MEAN**

# %% 
def take_sample_and_show(means):
    x_sample, sample_ci_z, sample_ci_t = perform_comparison(sample_size=SAMPLE_SIZE,confidence=0.95)
    plot_default_histogram(means,bins=50,start=30,end=70)

    # ADD THE SAMPLE 
    plt.axvline(x_sample.mean(), color='r', linewidth=1)
    min_ylim, max_ylim = plt.ylim()
    plt.text(x_sample.mean()*1.01,max_ylim*0.85, 'Sample Mean: {:.2f}'.format(x_sample.mean()),color='r')  

    print(f"Sample size: {len(x_sample)}, Sample std: {x_sample.std()}, Confidence {CONFIDENCE}, Max value {max(x_sample)}, Min value: {min(x_sample)}")

    # PLOT CI INFOR FOR Z TESTS
    z_color='m'
    plt.axvline(sample_ci_z.upper_bound, color=z_color, linestyle='dashed', linewidth=1)
    plt.axvline(sample_ci_z.lower_bound, color=z_color, linestyle='dashed', linewidth=1)
    plt.text(sample_ci_z.upper_bound*1.01, max_ylim*0.8, 'z',color=z_color) 
    plt.text(sample_ci_z.lower_bound*1.01, max_ylim*0.8, 'z',color=z_color) 
    sample_ci_z.print_statistics()

    # PLOT CI INFO FOR T TESTS
    t_color='g'
    plt.axvline(sample_ci_t.upper_bound, color=t_color, linestyle='dashed', linewidth=1)
    plt.axvline(sample_ci_t.lower_bound, color=t_color, linestyle='dashed', linewidth=1)
    plt.text(sample_ci_t.upper_bound*1.01, max_ylim*0.7, 't',color=t_color) 
    plt.text(sample_ci_t.lower_bound*1.01, max_ylim*0.7, 't',color=t_color) 
    sample_ci_t.print_statistics()
    print("t distribution has wider confidence intervals compared to z distribution")
    print(f"t.width-z.width {sample_ci_t.get_size()-sample_ci_z.get_size()} ")


take_sample_and_show(means)


#%% [markdown]
# **ADDITIONAL SAMPLE 2 COMPARED TO MEAN**
take_sample_and_show(means)


#%% [markdown]
# **ADDITIONAL SAMPLE 3 COMPARED TO MEAN**
take_sample_and_show(means)



#%% [markdown]
# # Theroy - Shape Difference between t-distribution and normal distribution
# Additional note. In this experiment we are showcasing Normal Distribution based confidence intervals and T-Distribution based confidence intervals.
# Based on CLT we are assuming in general a normal distribution to the means of data, however when the sample sizes are small its better to assume a variant 
# of normal distribution that has wider tails (t-distribution). 
# the t-distribution has wider tails with smaller sample sizes. With sample sizes 30 t-distribution starts to follow the normal distribution. 
# The distribution assumption for the mean data is important because based on that we calculate the extremum values (t/z). 
# For Normal distribution we assume the 66% of data to be within 1 std from mean, 95 % data to be wtihin ~2 std from mean, 99% of data to be within ~2.3 std from the mean.
# For t-distribution the amount of standard distributions we need for any of (66%,95%,99%) are wider based on the sample size. In t-distribution we call this "degrees of freedom"