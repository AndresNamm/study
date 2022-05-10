# RESEARCH ABOUT CORRELATION 

+ Covariance is essentially a AVERAGE of X * Y for all pairs of data.  
+ To get the correlation from it, we get the standard deviations of both datasets and replicate these standard deviations of X and Y with each other. This gives us a baseline for what the maximum Covariance could be. 
+ In Covariance You can think of each part of the summation as an individual Standard Deviation replication pairwise that can also have a negative value. If correlation is one the average of pairwise deviations multiplications should be the same as the multiplication of average deviation of the whole dataset.
+ My question is still, how we can get the Covariance to be the same as replication of STDs with perfect correlationa

https://en.wikipedia.org/wiki/Pearson_correlation_coefficient   
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5816993/   
![image](https://user-images.githubusercontent.com/21141607/166409240-fcd44cb6-a1f3-46c8-accf-0e49aabcb732.png)   
![image](https://user-images.githubusercontent.com/21141607/166409333-7d15f951-0775-4b00-bd30-575dc66bf8bd.png)   

+ The top and bottom of this function in case of high correlation should be equalt to each other. 
  + 
  + In the bottom we are taking the sum of deviations squared and then taking the sqrt from it.  
+ To understand how both functions grow here, look at this https://github.com/AndresNamm/study/blob/main/visualization/corr.py 


![image](https://user-images.githubusercontent.com/21141607/166674250-2532729a-461c-43a5-893d-cde051500a3b.png)

https://en.wikipedia.org/wiki/Variance   
https://en.wikipedia.org/wiki/Expected_value   
https://www.youtube.com/watch?v=xZ_z8KWkhXE   
https://www.cuemath.com/data/standard-deviation/   
https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/covariance/   
