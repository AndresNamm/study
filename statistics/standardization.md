# STANDARDIZATION 
![image](https://user-images.githubusercontent.com/21141607/201044628-6c509cf1-c3a7-4e89-a138-c7fd5629d657.png)

+ Standardizing is the process of making the mean of the dataset=0 and the std=1 
+ When we substract mean from every variable it is intuitive clear that the new mean shifts towards 0 

## With STD ist more complex 

** First lets definte STD

STD= $\sqrt[2]{VAR[X]}$\      

**Variance for discrete**      
![image](https://user-images.githubusercontent.com/21141607/201299573-6b13b125-3e73-4482-90f6-b46914bbdbbc.png)       
**Variance for continuous**        
![image](https://user-images.githubusercontent.com/21141607/201299543-4479a0c7-b0f7-491e-ab0a-808eee6928be.png)     
** source https://www.statlect.com/glossary/variance-formula

+ Intuitively, for variance we sum the weighted average for the squared distance. 
For std - we take the the square root of the weighted average of the squared distance. **This sort of becomes the average deviation from the mean**

[Side note about this thing](https://github.com/AndresNamm/study/blob/main/calculus/summation_sqrt.md) These are not inverse operations!!! 

+ Why do we use squaring?
![image](https://user-images.githubusercontent.com/21141607/201306101-607179d8-4056-4bbc-881c-a8c35cda1104.png)
** source https://stats.stackexchange.com/questions/118/why-square-the-difference-instead-of-taking-the-absolute-value-in-standard-devia


**Standardization of STD**    


+ **INTUITIVELY** The standardization takes every variables distance from the mean. Then it divides this distance for all the variables with standard deviation which sort of represents the **average deviation from mean**. This is how the new standerd deviation ( **sort of average deviation from the mean**) becomes 1 . In some way we just an inverse operation here when we are divigd
+ **Algebraic example how this makes the new standard deviation go to 1**
![image](https://user-images.githubusercontent.com/21141607/201306556-a1bcba09-a768-4248-919a-6f32bef68f2c.png)



## REFERENCES

+ [Proof for Standardizing leading to std 1 for Discrete distributions](https://math.stackexchange.com/questions/1550194/how-do-i-prove-standardizing-a-normally-distributed-random-variable)
+ [Claim with practical example that you can standardize any distribution](https://stats.stackexchange.com/questions/365164/standardization-of-non-normal-features)    
+ [Claims that any distribution can be standardized to have mean 0 and std=1](https://365datascience.com/tutorials/statistics-tutorials/standardization/)
   
