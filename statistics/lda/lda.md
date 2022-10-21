

# GLOSSARY 

+ Dir() - dirichlet distribution

# DESCRIPTION

In LDA the first assumption is that each document is created by drawing words from probability distributions. 


# UNDERSTANDING THE LDA ARTICLE

## FROM ARTICLE

![image](https://user-images.githubusercontent.com/21141607/197138435-2d44c40f-60f7-4f1b-a9ea-6081215ccb5a.png)

## IN MY WORDS
**PHASE 1**

For each document

1. We choose a random N from a some random distribution. This is the number of words in a given documetn
2. We pull a $\theta$ (A vector for K topic probabilities) from Dir( $\alpha$ ) 

  **PHASE 2** / Now having some concrete value for $\theta$ 

  For each word

  1. We pull the given topic $z_{n}$ from the $\theta$
  2. Then we pull a word from $w_{n}$ from P( $w_{n}$ | z_{n} , $\beta$  )  # This means we are pulling a specific word from the word matrix $\beta$ assuming we have chosen topic $z_{n}$


## FROM ARTICLE 

![image](https://user-images.githubusercontent.com/21141607/197141798-736051c9-9bcb-4a80-8704-515bbaf00f74.png)


## MY EXPLANATION 

+ pdf (probability density function) vs pmf (probability mass function)

![image](https://user-images.githubusercontent.com/21141607/197141940-3d0feb02-6a60-478e-bcc6-fd3fa19a56e3.png)



# REFERENCES 

+ [Article about LDA implementation in Python](https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0)
  + [This Github repo implements the LDA](https://github.com/kapadias/mediumposts/tree/master/natural_language_processing/topic_modeling/notebooks)
+ [Original paper about LDA](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)
+ [First answer tells that LDA is clustering with no word belonging to a certain category but a word belonging to a certain category with probability](https://www.quora.com/LDA-Topic-Modelling-output-what-do-the-output-values-represent)
