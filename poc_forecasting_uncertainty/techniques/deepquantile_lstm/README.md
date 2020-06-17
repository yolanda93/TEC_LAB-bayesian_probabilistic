Deep Quantile LSTM

**Implementación**
------

Fixed quantile bins τ0, …, τN

**Solución Naive -  Ajuste independiente de N cuantiles**: Estimación de N cuantiles ajustando un modelo independiente para cada quantile

Desventajas:
 * Implica ajustar N funciones diferentes 
 * Violación de el principio básico de que los cuantiles no se pueden cruzar

**Solución Multi-Output - Predicción Conjunta de N cuantiles**: Estimamos de forma conjunta la media condicionada y N cuantiles en un sólo modelo

Ventajas:
 * Nos permite resolver el problema de cuantiles cruzados




**Hipótesis**
------
Mejora del rendimiento del modelo
H1: Adding quantiles to the overall loss function adds relevant information about the target domain and can induce a regularization effect

**Desventajas**
------
Cuantiles cruzados

   
 
   
**Referencias**
------
Rodrigues, F., & Pereira, F. C. (2020). Beyond Expectation: Deep Joint Mean and Quantile Regression for Spatiotemporal Problems. IEEE Transactions on Neural Networks and Learning Systems, 1–13. https://doi.org/10.1109/tnnls.2020.2966745

Brando, A., Rodríguez-Serrano, J. A., Vitrià, J., & Rubio, A. (2019). Modelling heterogeneous distributions with an Uncountable Mixture of Asymmetric Laplacians. (NeurIPS 2019). Retrieved from http://arxiv.org/abs/1910.12288
