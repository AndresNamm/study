#%% [markdown]
## STANDARDIZATION EXAMPLE 
import numpy as np
degress_of_freedom=10
samples = 100
stds = []
vals=np.random.standard_t(degress_of_freedom,samples)
print("Before Standardization")
print(len(vals))
print(round(vals.mean(),6))
print(vals.std())

print("After Standardization")
restandardized = (vals-vals.mean())/vals.std()
print(len(restandardized))
print(round(restandardized.mean(),6))
print(restandardized.std())
# %%
