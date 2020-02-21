# Uncertainty Estimation

<de qué va todo esto>
<hablar de la estimación de la incertidumbre>
Ejemplo:
https://github.com/beeva/TEC_LAB-ai_watermarking/edit/master/README.md

Table of contents
=================

-   [Introducción [DONE]](#introduccion)
    -   [State-of-Art](#state-of-art)
    -   [Uncertainty Estimation](#state-of-art)
    -   [Scope](#scope)
    -   [Punto de partida: técnicas tradicionales](#traditional-techniques)
-   [Framework: Validación de las medidas de incertidumbre](#Framework)
    -   [State-of-Art](#state-of-art)
    -   [Experimentos](#experimentos)
    -   [Conclusiones](#conclusiones)
-   [Técnica: Exp.I - Estimacion de la varianza al vuelo [DONE]](#exp_I)
    -   [Motivación](#exp_I_motivacion)
    -   [Validación exp.original](#exp_I_tecnica-intro)
    -   [Experimentos y conclusiones](#exp_I_exp-conclusiones)
    -   [Conclusiones](#exp_I_final-conclusiones)
-   [Redes de densidad mixta [DONE]](#mdn)
    -   [Motivación](#mdn_motivacion)
    -   [Validación exp.original](#mdn_tecnica-intro)
    -   [Experimentos y conclusiones](#mdn_exp-conclusiones)
    -   [Conclusiones](#mdn_final-conclusiones)
-   [Semáforos](#semaforos)
    -   [Motivación](#semaforos_motivacion)
    -   [Validación exp.original](#semaforos_tecnica-intro)
    -   [Experimentos y conclusiones](#semaforos_exp-conclusiones)
    -   [conclusiones](#semaforos_final-conclusiones)
-   [MonteCarlo Dropout](#monte_carlo)
    -   [Motivación](#monte_carlo_motivacion)
    -   [Validación exp.original](#monte_carlo_tecnica-intro)
    -   [Experimentos y conclusiones](#monte_carlo_exp-conclusiones)
    -   [Conclusiones](#monte_carlo_final-conclusiones)    
-   [Loss Function [DONE]](#loss)
    -   [Motivación](#loss_motivacion)
    -   [Validación exp.original](#loss_tecnica-intro)
    -   [Experimentos y conclusiones](#loss_exp-conclusiones)
    -   [Conclusiones](#loss_final-conclusiones)
-   [Librerías de soporte](#librerias)
-   [Transferencia](#transferencia)


## Documentation
* [Applications](applications.md)


## Experiments

### V4.3.0-traffic_lights
* DATE: ---
* DESCRIPTION: 
* RESOURCES:
  * [Notebook](.ipynb)
  
### V3.0.0-mixture_density_networks
* DATE: 14/01/2019
* EXPERIMENT-TECHNIQUE: Mixture Density Networks
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Validate the Mixture Density Networks with the synthetic data used for Exp.I
   * EXPERIMENT GOAL: Compare of MDN with Exp.I
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V3.0.0-mixture_density_networks)
  
### V2.2.0-umal
* DATE: 04/01/2019
* EXPERIMENT-TECHNIQUE: Mixture Density Networks
* DATASET DESCRIPTION: Synthetic data generated in areas with different distribution within each area
* DESCRIPTION: UMAL is the technique presented by Axel Brando (BBVA-Data) in BBVA - IA Conference
   * EXPERIMENT GOAL: Understand the work of Axel Brando. Why does he use mixture density networks?
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V2.2.0-umal)
  
### V0.1.6-real_datasets
* DATE: 30/12/2019
* EXPERIMENT-TECHNIQUE: On fly variance estimation - EXP.I 
* DATASET DESCRIPTION: Boston housing dataset - scikit-learn toy datasets
* DESCRIPTION: Play with real datasets in regression problems
   * EXPERIMENT GOAL:  Validation with real datasets 
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V0.1.6-real_datasets)
  
### V0.0.5-prior_loss_distributions
* DATE: 30/12/2019
* EXPERIMENT-TECHNIQUE: Loss Function - On fly variance estimation - EXP.I 
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Play with different non gaussian error distirbutions and adapt the loss functions accordingly
   * EXPERIMENT GOAL: Do we improve results if the prior is satisfied?
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V0.0.5-prior_loss_distributions)
  
### V0.0.4-loss_function_frameworks
* DATE: 27/12/2019
* EXPERIMENT-TECHNIQUE: Loss Function - On fly variance estimation - EXP.I 
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Implementation in different deep learning frameworks: pytorch, tensorflow
   * EXPERIMENT GOAL: Tests compatibility of the experiment-technique with different deep learning frameworks
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V0.0.4-loss_function_frameworks)
  
### V0.0.3-loss_function_customization
* DATE: 24/12/2019
* EXPERIMENT-TECHNIQUE: Loss Function - On fly variance estimation - EXP.I 
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Play with the loss functions using different custom losses
    * EXPERIMENT GOAL: Understand how is propagated both errors (y and sigma losses)
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V0.0.3-loss_function_customization)
  
### V0.0.2-data_faraway_original
* DATE: 11/12/2019
* EXPERIMENT-TECHNIQUE: On fly variance estimation - EXP.I 
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Added data in both training and validation far away from the original dataset distribution 
    * EXPERIMENT GOAL: We would like to test if the uncertainty estimation increases in that points
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V0.0.2-data_faraway_original)
  
### V0.0.1-nongaussian_noise
* DATE: 11/12/2019
* EXPERIMENT-TECHNIQUE: On fly variance estimation - EXP.I 
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: add non gaussian noise to the original process
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V0.0.1-nongaussian_noise)
  
### V1.0.0-nonbayesian_techniques
* DATE: 03/12/2019
* EXPERIMENT-TECHNIQUE: Non bayesian techniques for uncertainty estimation in ML
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Explore other non bayesian and standard approches commonly applied in ML
    * EXPERIMENT GOAL: Understand its limitations. Why should be use a bayesian approach?
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V1.0.0-nonbayesian_techniques)
  
### V0.0.0-initial_validation
* DATE: 28/11/2019
* EXPERIMENT-TECHNIQUE: On fly variance estimation - EXP.I 
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Validation of the original experiment - no modification added
    * EXPERIMENT GOAL: Validate the implementation of the original experiment 
* RESOURCES:
  * [Notebooks](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V0.0.0-initial_validation)
---

## First Experiment: Synthetic data
This experiments are based on this release:
https://github.com/sthorn/deep-learning-explorations/blob/master/predicting-uncertainty.ipynb

The claiming of that release is that model can learn to predict and offers a value of predict uncertainty at the same time with a simple model.
It uses random data generate on the fly.

It uses the "variance" as error function, but actually it is not the variance, it is the difference between real y and predicted y.
The implicit dataset for training is a three column dataset with (x,y and error function), being the values of error function calculated on the fly.

The bayesian prior probability is set by using the error function as a variance, since it defines implicitly the error as a gaussian.


### 01-syntheticData-PredictionWihtoutVariance
This experiment makes predictions with a model predicting values and variance and other model predicting only values.
Hypothesis: Adding variance prediction may slow down predicting values, so accuracy me be penalized.
Result: Accuracy is almost the same for both values (a difference of 0.00002 in r2_score).

### 01-syntheticData-AddedDataFarAwayFromOriginal
This experiment add data with the same distribution far away from original data.
There is training data at (0,1) and (800,801).
Hypothesis: Variance should be low where there is training data and high far from known data.
Result: Model learn to predict low variance at any point, when the expected result is that variance increase far from known data.

### 01-syntheticData-addednongaussiannoise
This experiment add non gaussian noise at a low variance zone of original data.
Hypothesis: Noise should only affects to that low variance zone, increasing variance, but other low variance zones should not be affected.
Result: The expected result, variance increse and decrease gradually in that zone and others zones are almost not being affected.


### 01-syntheticData-predictedFarAwayFromData
This experiment train with original data for (0,1) region, but it predicts for several values to 1000.
Hypothesis: Model can learn the generative function and predicts values far away from data. Variance should increase as long as the value is far from known data.
Result: The expected result, values follows almost the generative function and the variance increase as long as prediction is far from known data.
