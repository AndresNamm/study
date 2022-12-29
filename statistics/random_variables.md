+ [Based on Larry Wasserman book](https://1drv.ms/b/s!ArMHhYJs5BG_jqNpgkG1LsFL-tdGgA?e=OCkjYR)
+ Based on Tõenäosusteooria algkursus, Kalev Pärn



# PROBABILITY SPACE 


![image](https://user-images.githubusercontent.com/21141607/198247389-696be406-ac9c-45b1-9040-2db549328e77.png)


+ Both HH and HT are $w$ ~ (sample outcome/realization/element/elementaarsündmus) in $\Omega$ in the example above. 
+ The event (Sündmus) is now a collection of elements (1 element = $w) \in \Omega$ (Can be continous or discrete) and a subset of $\Omega$. We usually associate a probability with an Event. 
+  $w$ - assumption is that only 1 $w$ can be the result of an experiment. No overlap between diffferent $w$ s is possible
+ F - the event space (sündmuste ruum) - Collection of multiple possible events (Tõenäosusteooria algkurus, Kalev Pärna, lk 29-30)
   + Example 1: Flipping coin. In this case 1 possible F (event space) is { $\Omega$, $\emptyset$, {heads}, {tails} }
   + Example 2: Taking 1 card from a deck. In this case possible F (event space) is with size of  $2^{\Omega}$ _think of the latter as whether element exists or exists not in subset_
      + **PS** - A member of F is **1 event**. This means a member of F can contain multiple sample outcomes aka multiple $w$.

+  Probability space ( $\Omega$, $P$, F)


# DEFINING THE FUNCTION OF PROBABILITY 

+ Defined with letter P
+ P - assigns every event in F a certain probability 
+ Rules P 
   + $P(\Omega) = 1$
   + $P(\emptyset) = 0$
   + $P(A) >= 0$
   + If A and B are mutually exclusive then $P(A \cup B)=P(A)+P(B)$



# RANDOM VARIABLE / JUHUSLIK SUURUS

## DISCRETE CASE 

+ Random variable is a function X: $\Omega$ -> $R$
+ Each Random Variable has a certain probability of happening - this forms a distribution over Random Variables.
+ Basically we have a collection of $w$ where each $w$ corresponds to certain $x_{i}$ Each $x_{i}$ corresponds to an event $A_{i}$. 
   + **NB**  $x_{i}$ can have multiple w-s that through $X(w)$ become $x_{i}$ but 1 w will always correspond only 1 $x_{i}$
+ As each w has only one corresponding $x_{i}$ the corresponding $A_{i}$ s will from a full system.Where $A_{i}$ $\cap$ $A_{j}$= $\emptyset$.


### **HOW DO WE GET A SAMPLE**    

+ [Ref](https://www.probabilitycourse.com/chapter8/8_1_1_random_sampling.php)
    + The collection of random variables X1, X2, X3, ..., Xn is said to be a random sample of size n if they are independent and identically distributed (i.i.d.), .

+ A sample is a collection of **experiment results**, **events** or **X**'s. 
+ From this sample, based on the X values we get, we can derive some estimate (Usually a Mean or STD)  
+ This means for a specific distribution, a collection of X results is a sample and sample size is the count of X results. 


#### **BERNOULLI DISTRIBUTION**

**PS** - _Using words experiment/trial here interchangeably._

If we look a the data Bernoulli distributon 

+ The bernoulli experiment has 2 potential opposing results.
+ Trial outcome is whethere something happened or something did not happen - **example** coin flip. 
+ The experiment outcome is mapped to X to values [0,1] -
+ a sample is collection of multiple experiments, events, X. 

**An example of a sample**

~~~python
[1,1,0,1,0,0,1]=['x1','x2','x3','x4','x5','x6','x7']
~~~
This Sample has size of 7

#### **BINOMIAL DISTRIBUTION** 

For Binomial distribution
+ The sample measures how many positive results we got when doing the bernoulli experiment **n** times. 
+ The basic outcome of an sample is the the collection of **n** bernoulli experiments
+ The experiment outcome is mapped to X .We have function X where we take a result of experiment (for example trial_result=[1,1,0,1,0,0,1]) with certain amount of trials and X(trial_result)=k , aka how many times there was success in one experiment. In this case X.s could be in range [0,1,2,3,4,5,6,7,....]. Each experiment in this case becomes 1 element in the sample.


**Sample example**
~~~python
[X(experiment1=[1,1,0,1,0,0,1]),....,X(experiment_N=[1,1,0,0,0,1,1])].
~~~
This sample now has a sample size of N. 


## SOFT INTRO TO RANDOM VARIABLES

+ [Additional Explanation by Khan Academy](https://www.youtube.com/watch?v=3v9w79NhsfI)

![image](https://user-images.githubusercontent.com/21141607/198245231-64e154ac-9201-4120-9a95-05a285a6f19b.png)

+ [Discrete Random Variables vs Continuous Random varibles by Khan Academy](https://www.youtube.com/watch?v=dOr0NKyD31Q)

![image](https://user-images.githubusercontent.com/21141607/198245997-72a7ee1c-2887-4810-affc-cd279ae45321.png)

# PROBABILITY DISTRIBUTIONS 

## DISCRETE PROBABILITY DISTRIBUTIONS 

+ A combination of ( $p_{i}$, $x_{i}$)

+ Uses PMF - probability **mass** function

+ Variance ![image](https://user-images.githubusercontent.com/21141607/200790086-79cbaa07-4cbd-43b8-8919-f7e412e1d885.png) 
+ [More info about variance - look into Discrete Random Variables part](https://www.statlect.com/glossary/variance-formula)


## CONTINUOUS PROBABILITY DISTRIBUTIONS

+ [Uses PDF - probability density function](https://www.statlect.com/glossary/probability-density-function)
    + [Characteristics of probability Density Functions](https://www.statlect.com/fundamentals-of-probability/legitimate-probability-density-functions)
      + Positive
      + Integrate to 1 

+ Variance ![image](https://user-images.githubusercontent.com/21141607/200790442-32f4180d-0fe4-44c3-8ac9-905d2e876b73.png)
+ [More info about variance - look into continuous Random Variables part](https://www.statlect.com/glossary/variance-formula)



# WHAT I WANT TO LEARN MORE ABOUT 


+  ~~F - event room~~ 
+ Probability distribution 
+ pdf (probability density function) vs pmf (probability mass function)
   + PMFs are used for Discrete variables . PDFs are used for Continuous random variables.  
+ Cumulative Distribution function
+ Lisaks teen läbi mingi lihtsa tõenäosus ülesande selle kõige pinnalt 


# GENERAL REFERENCE 

+ [Course about probability theory, distibutions, stas, ML](https://www.statlect.com/)
