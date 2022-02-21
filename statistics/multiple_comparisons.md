# [Bonferroni Correction explanation](https://toptipbio.com/bonferroni-correction-method/)


If we have alpha lets say = 0.05. This means we reject the null hypothesis whenever we see a result that would happen in 5 % samples when sampling from data where the H0 is true. In this case we can calmly say that as the probability of this happening is small we consider that actually H1 is true. 

Now what happens if we do multiple experiments with this data? 
In this case the likelyhood of getting some observation that is in this 5 % is getting bigger. To avoid that we divide tha alpha with the number of experiments conducted. 


# [FDR - False discovery rate](https://www.youtube.com/watch?v=4AytJuNkeSM)




False discovery rate Example 





![image](https://user-images.githubusercontent.com/21141607/153624570-e9e66bc9-3bed-4538-89bb-936a6586fbd4.png)

In this example we have a dataset where we actually know what the correct t-test would produce. In real life this would not happen but lets assume this happens for us. 
In this example we know that 900 cases the H0 is true and for 100 cases H1 is true. 
+ If we know the H0 is true in 900 cases and know the alpha is 0.05 we know that in 5 % of the cases we would have this situation 




[Benjamin Hochbers method](https://www.youtube.com/watch?v=rZKa4tW2NKs) and general info about FDR https://www.youtube.com/watch?v=-oIkIdhSNeU  - Example of calculating this in Excel. https://www.youtube.com/watch?v=S-F_R_WKNfQ
