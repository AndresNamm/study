

# GLOSSARY 

+ Dir() - dirichlet distribution

# DESCRIPTION

In LDA the first assumption is that each document is created by drawing words from probability distributions. 


## PROCESS


**PHASE 1**

For each document


1. We choose a random N from a some random distribution. This is the number of words in a given documetn
2. We pull a $\theta$ (A vector for K topic probabilities) from Dir( $\alpha$ ) 

  **PHASE 2** / Now having some concrete value for $\theta$ 

  For each word

  1. We pull the given topic $z_{n}$ from the $\theta$
  2. Then we pull a word from $w_{n}$ from P( $w_{n}$ | z_{n} , $\beta$  )  # This means we are pulling a specific word from the word matrix $\beta$ assuming we have chosen topic $z_{n}$

# REFERENCES 


+ [Original paper about LDA](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)
