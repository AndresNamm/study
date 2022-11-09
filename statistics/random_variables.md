+ [Based on Larry Wasserman book](https://1drv.ms/b/s!ArMHhYJs5BG_jqNpgkG1LsFL-tdGgA?e=OCkjYR)
+ Based on Tõenäosusteooria algkursus, Kalev Pärn



# PROBABILITY SPACE 


![image](https://user-images.githubusercontent.com/21141607/198247389-696be406-ac9c-45b1-9040-2db549328e77.png)


+ Both HH and HT are $w$ ~ (sample outcome/realization/element/elementaarsündmus) in $\Omega$ in the example above. 
+ The event (Sündmus) is now a collection of elements (1 element = $w) \in \Omega$ (Can be continous or discrete) and a subset of $\Omega$. We usually associate a probability with an Event. 
+  $w$ - assumption is that only 1 $w$ can be the result of an experiment. No overlap between diffferent $w$ s is possible
+ F - the event space (sündmuste ruum) - Collection of multiple possible events (Tõenäosusteooria algkurus, Kalev Pärna, lk 29-30)
   + Example 1: Flipping coin. In this case 1 possible F (event space) is { $\Omega$, $\emptyset$, {heads}, {tails} }
   + Example 2: Taking 1 card from a deck. In this case possible F (event space) is with size of  $2^{\Omega}$
   + PS - A member of F is **1 event**. This means a member of F can contain multiple sample outcomes aka multiple $w$.

+   Probability space ( $\Omega$, $P$, F)


# DEFINING THE FUNCTION OF PROBABILITY 

+ Defined with letter P
+ P - assigns every event in F a certain probability 
+ Rules P 
   + $P(\Omega) = 1$
   + $P(\emptyset) = 0$
   + $P(A) >= 0$
   + If A and B are mutually exclusive then $P(A and B)=P(A)+P(B)$


## SOME IMPORTANT DEDUCTIONS BASED ON PROBABILITY RULES 

+  $P(A)=1-P(\overline{A})$

# RANDOM VARIABLE / JUHUSLIK SUURUS

+ Random variable is a function X: $\Omega$ -> $R$
+ Basically we have a collection of $w$ where each $w$ corresponds to certain $x_{i}$ Each $x_{i}$ corresponds to an event $A_{i}$. 
   + **NB**  $x_{i}$ can have multiple w-s that through $X(w)$ become $x_{i}$ but 1 w will always correspond only 1 $x_{i}$
+ As each w has only one corresponding $x_{i}$ the corresponding $A_{i}$ s will from a full system. Where $A_{i}$ $\cap$ $A_{j}$= $\emptyset$     

## SOFT INTRO TO RANDOM VARIABLES

+ [Additional Explanation by Khan Academy](https://www.youtube.com/watch?v=3v9w79NhsfI)

![image](https://user-images.githubusercontent.com/21141607/198245231-64e154ac-9201-4120-9a95-05a285a6f19b.png)

+ [Discrete Random Variables vs Continuous Random varibles by Khan Academy](https://www.youtube.com/watch?v=dOr0NKyD31Q)

![image](https://user-images.githubusercontent.com/21141607/198245997-72a7ee1c-2887-4810-affc-cd279ae45321.png)

# PROBABILITY DISTRIBUTIONS 

## DISCRETE PROBABILITY DISTRIBUTIONS 

+ A combination of ( $p_{i}$, $x_{i}$)

+ Uses PMF - probability **mass** function



## CONTINUOUS PROBABILITY DISTRIBUTIONS

+ [Uses PDF - probability density function](https://www.statlect.com/glossary/probability-density-function)
    + [Characteristics of probability Density Functions](https://www.statlect.com/fundamentals-of-probability/legitimate-probability-density-functions)
      + Positive
      + Integrate to 1 


# WHAT I WANT TO LEARN MORE ABOUT 


+  ~~F - event room~~ 
+ Probability distribution 
+ pdf (probability density function) vs pmf (probability mass function)
   + PMFs are used for Discrete variables . PDFs are used for Continuous random variables.  
+ Cumulative Distribution function
+ Lisaks teen läbi mingi lihtsa tõenäosus ülesande selle kõige pinnalt 


# GENERAL REFERENCE 

+ [Course about probability theory, distibutions, stas, ML](https://www.statlect.com/)
