# STANDARDIZATION 
![image](https://user-images.githubusercontent.com/21141607/201044628-6c509cf1-c3a7-4e89-a138-c7fd5629d657.png)

+ Standardizing is the process of making the mean of the dataset=0 and the std=1 
+ When we substract mean from every variable it is intuitive clear that the new mean shifts towards 0 
## With STD ist more complex 


** First lets definte STD

STD= $\sqrt[2]{VAR[X]}$\

** Variance for discrete **
![image](https://user-images.githubusercontent.com/21141607/201299573-6b13b125-3e73-4482-90f6-b46914bbdbbc.png)
** Variance for continuous**
![image](https://user-images.githubusercontent.com/21141607/201299543-4479a0c7-b0f7-491e-ab0a-808eee6928be.png)


+ Intuitively, for variance we get the squared distance from the mean and sum the weighted average for the squared distance. 
For std - we take the the square root of the weighted average of the squared distance. ()


 +The standardization takes every variables distance from the mean. Then it divides this distance for all the variables with standard deviation  
 +    and divides this with old standard distribution (Average deviation from the mean) 
 +  If we now take every deviation from this mean and divide it by the average deviation and sum it up similiarly. 
 + [Claim with practical example that you can standardize any distribution](https://stats.stackexchange.com/questions/365164/standardization-of-non-normal-features)    
 + [Claims that any distribution can be standardized to have mean 0 and std=1](https://365datascience.com/tutorials/statistics-tutorials/standardization/)
   
