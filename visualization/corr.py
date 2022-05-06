#%%

from cProfile import label
from statistics import covariance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sympy import im
import math
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

def calculateAdditionSquared(t):
    sum1 = 0 
    for i in range(t):
        sum1 += i*i
    sum2 = 0 

    for i in range(t):
        sum2 += i*i
    return math.sqrt(sum1)*math.sqrt(sum2)

#%%
start=0
finish=5
x = np.arange(start, finish, 1)

y = np.array([calculateSum(i) for i in range(start,finish)])
y2 = np.array([calculateAddition(i) for i in range(start,finish)])
y3 = np.array([calculateAdditionSquared(i) for i in range(start,finish)])
overlapping = 0.150
print('Values of x: ', x)
print('Values of y: ', y)
plt.plot(x, y,label = "Corr Top", linewidth=8)
plt.plot(x, y3,label = "Corr Bottom Squared",linewidth=5)
plt.plot(x, y2,label = "Corr Bottom",linewidth=6)

plt.title("Correlation")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.legend()
plt.show()

# %%
icecream = pd.read_csv('corr_data.csv')
icecream.corr()

# %%

icecream

# %%

x = icecream["AVG temp C"]
y = icecream["Ice Cream production"]

top=sum((x-x.mean())*(y-y.mean()))
bottom=(sum((x-x.mean())**2))**0.5 * (sum((y-y.mean())**2))**0.5 
corr = top/bottom
corr

# %%
start=0
finish=5
x = np.arange(start, finish, 1)
y = np.array([math.sqrt(i) for i in range(start,finish)])
print('Values of x: ', x)
print('Values of y: ', y)
plt.plot(x, y,label = "Corr Top", linewidth=8)
plt.title("Root Function Growth")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.legend()
plt.show()


# %%
start=1
finish=100
x = np.arange(start, finish, 1)
y = np.array([0.5*i**-0.5 for i in range(start,finish)])
print('Values of x: ', x)
print('Values of y: ', y)
plt.plot(x, y,label = "Corr Top", linewidth=8)
plt.title("Derivative of Square root Growth") # https://www.wikihow.com/Differentiate-the-Square-Root-of-X
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.legend()
plt.show()
# %%
