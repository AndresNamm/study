
# %% [markdown]
# # Confidence Intervals
# ## REFERENCES
#
# + [First Tutorial I found](https://towardsdatascience.com/how-to-calculate-confidence-intervals-in-python-a8625a48e62b)
# + [Quick Reference to my fantastic CI tutorial](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/CONFIDENCE%20INTERVALS.pdf)
# %%

import numpy as np 
from scipy.stats import t
import math

# %%



# %% [markdown]
# z_val now is how many standard deviations we consider the potential sample means 
# could go from the global mean
# # %% 

#%%

x = np.random.normal(size=100)
m = x.mean()
s = x.std()
sample_size = len(x)-1
confidence = 0.99 
alpha = 1-confidence
number_of_stds = np.abs(t.ppf((alpha)/2,sample_size))
print(number_of_stds)

print(x)
min_b = m - number_of_stds * (s/math.sqrt(sample_size))
max_b = m + number_of_stds * (s/math.sqrt(sample_size))

print(f"Confidence interval is {min_b}..{m}..{max_b}" )
print(f"Width is {max_b-min_b}" )



# %%
