# Loss Function Experiments

The goal of these experiments is to better understand how we can model the loss function and its effect in the predicted results.
Each set of experiments have the following:

  - Notebooks
  - Hypothesis 
  - Conclusions: Advantages & limitations

### Index

* [Loss Error Experiments](#LossError) 

<h2 id="LossError">Loss Error Experiments</h2> 

##### :star: Notebooks

[Loss Error Experiments](./loss_error_experiments.ipynb)

##### :star: Hypothesis

*H1: Do we have the same result if we change the loss function from case a to case b?*

a) - Proposed Exp.1 - 1 input tensor: (2dim: [y_hat, sigma]) and 1 loss error
b) - Common Usage* - 2 input tensors: [y_hat], [sigma] and 1 loss error (loss_yhat + loss_sigma)
Validated with experiments: Experiment 0 (original - single loss error) | Experiment 1 (common usage - muli loss error)

*H2: What is the effect of each loss error (sigma and y) in updating the weights of the network?*

Validated with experiments: Experiment 3 (multi loss error - different weights)

*H3: What happens if we only propagate the y error while keeping updating the sigma on the fly?*

Validated with experiment: Experiment 2 (single Loss Error - only y error)

*NOTE: After doing some research case b) seems to be the common method when we have multiouput target

##### :star: Conclusions

**H1**:
We get exactly the same results.
So, we can validate that it is possible to model two separate tensors for y and sigma and add the error of each of them

Advantages:
It seems that not all the deep learning frameworks work using a tensor of two components for the loss function. Pytorch applies a reduction method on the whole tensor as default
This alternative represent a good solution for tensorflow or keras

**H2**:
We have add a factor to the error of each component (y and sigma)
Only a small proportion of the sigma error need to be propagated.
A factor of 0.5 in sigma keeps more or less the same prediction results

**H3**:
The sigma predictions do not vary with the input data 


