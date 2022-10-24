
# %% [markdown]
# # Confidence Intervals
# + [Quick Reference to my fantastic CI tutorial](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/CONFIDENCE%20INTERVALS.pdf)
# + [This code is based on this blog post](https://towardsdatascience.com/how-to-calculate-confidence-intervals-in-python-a8625a48e62b)    
#
# As you can see, we are taking the data from Uniform distribution. Due to the Central Limit Theorem (CLT) we can assume that its mean if taken as samples of size N will follow a normal distribution
# with Std of $\frac{\sigma}{\sqrt{n}}$
# %%
import numpy as np 
from scipy.stats import t,norm
import math
import matplotlib.pyplot as plt

x = np.random.uniform(size=100) 
x_positive = x-min(x)
x_scaled = x_positive/max(x_positive)*100
x = x_scaled
m = x.mean()
s = x.std()
sample_size=len(x)
confidence = 0.99 
alpha = 1-confidence

# %% [markdown]
# z_val - Where in the standard normal distribution a value outside the confidence interval would be located. As standard deviation within the standardized normal distribution
# is 1 then z_val tells how many standard deviations in a **standard** normal distribution the value should go away from the mean to not fall inside the range of confidence inteval.
#%%
z_val = np.abs(norm.ppf((alpha)/2))
sample_size=len(x)
confidence = 0.99 
alpha = 1-confidence
ci_std = (s/math.sqrt(sample_size)) # FROM THE CLT
min_b = m - z_val * ci_std
max_b = m + z_val * ci_std

def print_statistics(m:float,s:float,sample_size:int,confidence:float,min_b:float,max_b:float):
    print(f"Median: {m}")
    print(f"Std: {s}")
    print(f"Sample Size: {sample_size}")
    print(f"Confidence: {confidence}")
    print(f"Min boundary {min_b}")   
    print(f"Max boundary {max_b}")
    print(f"Width is {max_b-min_b}" )

print_statistics(m=m,s=s,sample_size=sample_size,confidence=confidence,min_b=min_b,max_b=max_b)
# %% [markdown]
# # T distribution
#     
# We are doing the same thing here as in previous lines but an important note is that in this case we are using a [t distribution](https://www.investopedia.com/terms/t/tdistribution.asp) instead of a normal distribution. 
# Depending on the degrees of freedom (sample size-1). The t-distribution is useful when you have small sample sizes.
# It has heavier tails so it's more likely give out extreme values. This means
# 1. The t-distribution based Confidence Interval is wider. (Less accurate)         
# 2. If t-test are performed with with t-distribution, we will also have to have larger values for results to prove the hypothesis false.
# **When is t-distribution used instead of normal distribution?** 
# Based on [Article 1](https://www.scribbr.com/statistics/t-distribution/),[Article 2](https://knowledgehound.com/data/what-is-the-difference-between-a-t-test-and-a-z-test/) there
# are two important factors. 
# 1. Do we have available the global std? If not the we should use t distribution.
# 2. If the sample size is more than 30 the t distribution closely resembles the normal distribution so you can pretty much use both.  
# Based on this we could have used both the t and the z distribution here. 
#        
# %% [markdown]
# Only things you have to do diffetently when calculating t-distribution
# + Add degrees of freedom variable = sample_size -1
# + t_val = Where in the standard t-distribution a value outside the confidence interval would be located
# %%
degrees_of_freedom = len(x)-1
t_val = np.abs(t.ppf((alpha)/2,degrees_of_freedom))

# %% [markdown]
# sample_size now determines the confidence interval width
# %%
ci_std = (s/math.sqrt(sample_size)) # FROM THE CLT 
t_min_b = m - t_val * ci_std
t_max_b = m + t_val * ci_std


print_statistics(m=m,s=s,sample_size=sample_size,confidence=confidence,min_b=t_min_b,max_b=t_max_b)

#%% [markdown] 
# I will now show an example how Uniform distribution means will follow a normal distribution. 
## Uniform distribution from 100*100 Sample
nr_samples = 100
sample_size = 100
full_dataset = np.empty([1,10])
print(full_dataset)
#%%

for i in range(nr_samples):
    x = np.random.uniform(size=sample_size) 
    x_positive = x-min(x)
    x_scaled = x_positive/max(x_positive)*100
    x = x_scaled





#%% [markdown]
# Comparing t-distribution width with normal distribution width when sample size is 100


#%%

print(f"Normal distribution min boundary {min_b}")
print(f"T-distribution min boundary {t_min_b}")
print(f"Normal distribution max boundary {max_b}")
print(f"T-distribution max boundary {t_max_b}")
print(f"Normal dist width {max_b-min_b}")
print(f"t dist width {t_max_b-t_min_b}")




#%% 





counts, bins = np.histogram(x_scaled)
plt.hist(bins[:-1],len(bins)-1,weights=counts)
plt.axvline(m, color='k', linestyle='dashed', linewidth=1)
plt.axvline(m+s, color='r', linestyle='dashed', linewidth=1)
plt.axvline(m-s, color='r', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(m*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(m)) 
plt.text((m+s)*1.1, max_ylim*0.9, 'Mean+Std: {:.2f}'.format(m+s)) 
plt.text((m-s)*1.1, max_ylim*0.9, 'Mean+Std: {:.2f}'.format(m-s)) 
# Write text on position 1.1 to man an 0.9 to max y 
#plt.text(min_b*0.7, max_ylim*0.8, 'Min boundary: {:.2f}'.format(m)) # Write text on position 1.1 to man an 0.9 to max y 
# %%
len(counts)

# %%
# %% [markdown]
# Lets draw 100 times from uniform distribution
#%%

x = np.random.uniform(size=100) 
x_positive = x-min(x)
x_scaled = x_positive/max(x_positive)*100
x = x_scaled

# %%
all_samples = []
for i in range(100):
    all_samples.append(np.random.uniform(size=100))

x = all_samples[0]
x_positive = x-min(x)
x_scaled = x_positive/max(x_positive)*100
x_scaled
x = x_scaled
m = x.mean()
s = x.std()
degrees_of_freedom = len(x)-1
sample_size=len(x)
confidence = 0.99 
alpha = 1-confidence
t_val = np.abs(t.ppf((alpha)/2,degrees_of_freedom))
min_b = m - t_val * (s/math.sqrt(sample_size))
max_b = m + t_val * (s/math.sqrt(sample_size))

means=np.empty(100)
for item in all_samples:
    means[i]=all




# %% [markdown]
# Now lets try what bootstrapping gives us.
