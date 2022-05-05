#%%

from cProfile import label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

#%%

def calculateSum(t):
    sum = 0 
    for i in range(t):
        sum += i*i
    return sum


def calculateAddition(t):
    sum1 = 0 
    for i in range(t):
        sum1 += i
    sum2 = 0 

    for i in range(t):
        sum2 += i

    return sum1*sum2




#%%
start=0
finish=11
x = np.arange(start, finish, 1)
a = 2
b = 9
c = 10
y = np.array([calculateSum(i) for i in range(start,finish)])
y2 = np.array([calculateAddition(i) for i in range(start,finish)])
print('Values of x: ', x)
print('Values of y: ', y)
plt.plot(x, y, label = "Corr Top")
plt.plot(x, y2,label = "Corr Bottom")

plt.title("Quadratic Function")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.legend()
plt.show()
# %%
