# Non-bayesian (frequentist) approaches for measuring uncertainty in Machine Learning

The goal of these series of notebooks is to provide a context of other techniques used for measuring uncertainty in machine learning (parametric models). It is specially important to understand the limitations of these methods before going through probabilistic approaches. Thus, the notebooks will focus on the following: 

  - Experiment Notebook
  - Technique definition
  - Types of uncertainty that it cover (Epistemic vs. Aleatoric)
  - Conclusions: Advantages & limitations

### Techniques

* [Bootstrapping](#Bootstrapping) - Building confidence intervals with bootstrapping
* [Mean Variance Estimation](#MVE)
* [The Delta Method](#DeltaMethod)


<h2 id="Bootstrapping">Bootstrapping </h2> 

##### :star: [Experiment Notebook](./boostrapping_confidence_intervals.ipynb)

##### :star: [Technique definition](https://machinelearningmastery.com/calculate-bootstrap-confidence-intervals-machine-learning-results-python/)

##### :star: Types of uncertainty that it cover (Epistemic vs. Aleatoric)
 
- *Epistemic*: It helps to measure the effect of training a model where particular data have not been included. However, it assumes a gaussian distribution and it does not measure the effect of having a non-representative training set (e.g. non-gaussian observations)
 
- *Aleatoric Homoskedastic*: It assumes the error component constant across the input space

##### :star: Conclusions: Advantages & limitations

Advantages

This method could help us to measure the epistemic uncertainty of our model. It is commonly used for data scientists with two main purposes:
- We can explain to the client relationships extracted from data using confidence intervals. This is specially useful in cases where we know that our training data is not representative enough of the real population distribution (parameters) but we assume a normal distribution
- We can identify when we should choose for a more complex model (we look for the narrower confidence interval). High variance may suggest to go towards a more complex model
- It could highlight the effects of excluding relevant information (we could condition the resampling method to exclude or include some particular data)

Limitations

- It is unfeasible to run this technique for measuring the uncertainty in complex models with more variables and high number of parameters. (e.g deep neural networks, large datasets)

- It's not good for estimating the error of a single prediction (single point-of-estimation)

- The confidence intervals of the prediction residuals obtained here are assumed to be normally distributed, have the same variance and be independent. 

### References


[1] [High-Quality Prediction Intervals for Deep Learning:
A Distribution-Free, Ensembled Approach](https://arxiv.org/pdf/1802.07167.pdf)