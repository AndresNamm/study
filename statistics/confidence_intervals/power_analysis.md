# MAIN REFERENCES

+ Power Analysis Playlist with my own explanations - [Video](https://www.youtube.com/playlist?list=PLlH7A2i7EAO4sU3DGhJKQUVF4W1_nKEdf)
+ Overview slides created by me - [Slides](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/PowerAnalysis.pdf)
+ Multiple good examples on doing Power Analysis on Confidence Intervals and Hypothesis tests - [External Tutorial](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_power/bs704_power_print.html)  
   + [Same but in HTML](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Power/) 
+ Effect Size - [Tutorial](https://github.com/AndresNamm/study/blob/main/statistics/effect_size.md)
+ Comments about Power analysis - [Tutorial below](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/power_analysis.md)


# ADDITIONAL MATERIALS

+ [Statistical Power](https://www.youtube.com/watch?v=Rsc5znwR5FA)
+ [Power Analysis, Clearly Explained](https://www.youtube.com/watch?v=VX_M3tIyiYk&t=50s)


![image](https://user-images.githubusercontent.com/21141607/210966970-30c40f7a-c02c-4af6-a0f5-758da1c8ddb7.png)


# COMMENTS ON DOING POWER ANALYSIS ON HYPOTHESIS TESTING - CALCULATING EFFECT


The aim of Power Analysis is to determine the necessary sample size to reject false H0 with probability 1-Beta. 1-Beta is otherwise referred to as **Power** 
You set the Beta and it means the probability of making Type II error. Type II error is when you dont reject H0 when it is false. 
1-Beta is something you set. Usually it is set to be 80% e.g. I want to detect H0 being false with probability 80 %. 

 + General Formula for calculating the sample size for hypothesis testing     
![image](https://user-images.githubusercontent.com/21141607/159645046-edadc1f9-1b0b-4a4c-8bdb-cf2b95b77da8.png)     


ES = Effect Size You can think of this as what size effect IN REGARDS TO standard deviations you would like to be able to detect with set Power. 
Most of the cases  $\frac{\mu_1-\mu_2}{\sigma}$ is used [Read more about Effect Size here](https://github.com/AndresNamm/study/blob/main/statistics/confidence_intervals/effect_size.md)   For power analysis we are using the STD of data. We could not use the STD over sample means as n is what we are trying to determine.

