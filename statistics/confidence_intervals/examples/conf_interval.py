
# %% [markdown]
# # Confidence Intervals
# ## REFERENCES
#
# + [First Tutorial I found](https://towardsdatascience.com/how-to-calculate-confidence-intervals-in-python-a8625a48e62b)
# + [Quick Reference to my fantastic CI tutorial](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/CONFIDENCE%20INTERVALS.pdf)
# %%

import numpy as np 
from scipy.stats import t

# %%

x = np.random.normal(size=100)
m = x.mean()
s = x.std()
dof = len(x)-1
confidence = 0.95 
alpha = 1-confidence

# %% [markdown]
# t_crit now is how many standard deviations we consider the potential sample means 
# could go from the global mean
# # %% 
t_crit = np.abs(t.ppf((alpha)/2,dof))
print(t_crit)

# %%
