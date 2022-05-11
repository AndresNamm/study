# RESEARCH ABOUT CORRELATION 

+ Covariance is essentially a AVERAGE of X * Y for all pairs of data. 
    + This is the largest if we mutliply with each other the closest values possible. 
+ To get the correlation from it, we get the standard deviations of both datasets and replicate these with each other. This gives us a baseline for what the maximum Covariance could be.
    + We can get the Maximum Covariance If we replicate the n-th largest deviation from X and Y for n=0..n=k where k is the index of the largest element. This is because we get the largest multiplication if we multipply with each other the closest elements possible. 
    + If we replicate the n-th largest deviation from X and Y for n=0..n=k where k is the index of the largest element, we will get on average the replication of standard deviations aka the maximum potential Covariante

CORRELATION FORMULA GENERAL     
![image](https://user-images.githubusercontent.com/21141607/166409240-fcd44cb6-a1f3-46c8-accf-0e49aabcb732.png)     
STD      
![image](https://user-images.githubusercontent.com/21141607/167784298-2c5dd4e6-847f-4d01-a2bc-c2dbc5148eda.png)    
CORRELATION FORMULA CALCULATION            
![image](https://user-images.githubusercontent.com/21141607/166409333-7d15f951-0775-4b00-bd30-575dc66bf8bd.png)      


+ The top and bottom of this function in case of high correlation should be equalt to each other. 
  + In the bottom we are taking the sum of deviations squared and then taking the sqrt from it.  This is less than just taking the sum of deviations. 
+ To understand how both functions grow here, look at this https://github.com/AndresNamm/study/blob/main/visualization/corr.ipynb


![image](https://user-images.githubusercontent.com/21141607/166674250-2532729a-461c-43a5-893d-cde051500a3b.png)


# REFS 

https://en.wikipedia.org/wiki/Pearson_correlation_coefficient   
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5816993/   
https://en.wikipedia.org/wiki/Variance   
https://en.wikipedia.org/wiki/Expected_value   
https://www.youtube.com/watch?v=xZ_z8KWkhXE   
https://www.cuemath.com/data/standard-deviation/   
https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/covariance/   

