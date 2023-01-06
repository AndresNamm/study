# ES = $\frac{\mu_1-\mu_2}{\sigma}$


ES = Effect Size You can think of this as what size effect IN REGARDS TO standard deviations exists between $\mu_1$ and $\mu_2$. Std from the examples I have seen can be taken from literature or it can be pooled between 2 std from different groups.

**NB** One important thing to note there is a **difference** 

+ STD over sample means = $\frac{\sigma}{\sqrt{n}}$    
+ STD for data itself = std   - To calculate effect size we are using the std for the data. This can be from control group or found from literature. 

For power analysis we are using the STD of data. We could not use the STD over saple means as n is what we are trying to determine.
STD over samples gets smaller as the sample size grows. std for data remains the same as data itself varies.


For me the effect part became a bit complicated here. In general it was recommended to use this formula to get effect:
![image](https://user-images.githubusercontent.com/21141607/159643951-47053734-cd6b-4486-93df-11b118d71796.png)

However as Power Analysis is done before conducting the test, calculating the effect based on this formula is not super obvious. There is a chance to use ofcourse data from previous research. Another thing that was recommended is to use some known meanigful effect in the field from some domain knowledge. This seems to make more sense because the aim of Power Analysis is to conduct your experiment so that you will not make TYPE 2 error. If you overestimate your effect in the Power Analysis you will get smaller sample size which means you might **get a type 2 error in your Actual Test**

# EFFECT EXPLANATION

![image](https://user-images.githubusercontent.com/21141607/159644887-9cff4f53-fae9-4f7a-8b78-bdef8e6c5420.png)


![image](https://user-images.githubusercontent.com/21141607/163121061-7fcee4a1-fcec-45ee-8b28-0538953cfff4.png)     
+ The standard deviation we are using here is the regular data standard deviation. Often a combined dataset standard deviation is used. er

![image](https://user-images.githubusercontent.com/21141607/163121095-26ff6cd4-c2b2-4732-9073-4d2c0cdf5d19.png)    

+ Think of percent of overlap as the part of the area covered by both distributions that is not overlapped. You can calculate this by substracting the Integral from the other on each part of the linear scale. 
+ Taking one mean as the Percentile of the other mean is another interesting thing to look at from the datas standpoint. 



# REFS 


+ [Pretty good article about effect size](https://meera.snre.umich.edu/power-analysis-statistical-significance-effect-size)
+ [Good explanation of Effect Size](https://www.youtube.com/watch?app=desktop&v=tTgouKMz-eI)
+ [More thorough paper on Effect Size](http://www.bwgriffin.com/gsu/courses/edur9131/content/EffectSizeBecker.pdf)
+ [Cohens D book limited access](https://onedrive.live.com/?cid=BF11E46C828507B3&id=BF11E46C828507B3%21232838&parId=BF11E46C828507B3%21232837&o=OneUp)
   + pp 21-22       
