
+ [Multiple good examples on doing Power Analysis on Confidence Intervals and Hypothesis tests](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_power/bs704_power_print.html)  
   + [Same but in HTML](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Power/) 
+ [Statistical Power](https://www.youtube.com/watch?v=Rsc5znwR5FA)
+ [Power Analysis, Clearly Explained](https://www.youtube.com/watch?v=VX_M3tIyiYk&t=50s)
+ [Pretty good article about effect size](https://github.com/AndresNamm/study/blob/main/statistics/effect_size.md)


# COMMENTS ON DOING POWER ANALYSIS ON HYPOTHESIS TESTING - CALCULATING EFFECT


The aim of Power Analysis is to determine the necessary sample size to reject false H0 with probability 1-Beta. 1-Beta is otherwise referred to as **Power** 
You set the Beta and it means the probability of making Type II error. Type II error is when you dont reject H0 when it is false. 
1-Beta is something you set. Usually it is set to be 80% e.g. I want to detect H0 being false with probability 80 %. 

 + General Formula for calculating the sample size for hypothesis testing     
![image](https://user-images.githubusercontent.com/21141607/159645046-edadc1f9-1b0b-4a4c-8bdb-cf2b95b77da8.png)     

ES = Effect Size You can think of this as what size effect IN REGARDS TO standard deviations you would like to be able to detect with set Power. 
Often (mean1-mean2)/std is used. Std from the examples I have seen can be taken from literature or it can be pooled between 2 std from different groups.
[I have written more about this here](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/effect_size.md)


**NB** One important thing to note there is a **difference** 

+ STD over sample means = std / sqrt(n)    
+ STD for data itself = std   - To calculate effect size we are using the std for the data. This can be from control group or found from literature. 

For power analysis we are using the STD of data. We could not use the STD over saple means as n is what we are trying to determine.

STD over samples gets smaller as the sample size grows. std for data remains the same as data itself varies.

![image](https://user-images.githubusercontent.com/21141607/159644887-9cff4f53-fae9-4f7a-8b78-bdef8e6c5420.png)

For me the effect part became a bit complicated here. In general it was recommended to use this formula to get effect:
![image](https://user-images.githubusercontent.com/21141607/159643951-47053734-cd6b-4486-93df-11b118d71796.png)

However as Power Analysis is done before conducting the test, calculating the effect based on this formula is not super obvious. There is a chance to use ofcourse data from previous research. Another thing that was recommended is to use some known meanigful effect in the field from some domain knowledge. This seems to make more sense because the aim of Power Analysis is to conduct your experiment so that you will not make type 2 error. If you overestimate your effect in the Power Analysis you will get smaller sample size which means you might **get a type 2 error in your Actual Test**


[Also look at the visual example of how power analysis works](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/VisualExplain.pdf)

