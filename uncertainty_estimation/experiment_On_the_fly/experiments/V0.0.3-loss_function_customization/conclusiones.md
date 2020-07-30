
Experiment 0 (original - single loss error) vs. Experiment 1 (common usage - multi loss error)
------
``H1: Es posible utilizar un tensor de varias dimensiones como función de pérdida con las herramientas habituales de deep learning``

- Conclusión:

En el modelado de la función de pérdida al parecer no es muy común utilizar un mismo tensor con N dimensiones cuando se tienen varias (N) salidas. 
Por compatibilidad con Tensorflow se recomienda el método B mejor que el método A [1]. Se ha comprobado que ambos métodos dan los mismos resultados. La función de MSE de Pytorch hace un reduce_mean de ambas dimensiones para quedarse con un error escalar que es el que usará en backpropagation

- Experiment 0 (original - single loss error): 1 tensor de salida de 2 dimensiones  (2dim: [y, sigma])
- Experiment 1 (common usage - multi loss error): 1 loss function que agregue el error de ambos (loss_yhat + loss_sigma) 


*Referencias: https://towardsdatascience.com/converting-a-deep-learning-model-with-multiple-outputs-from-pytorch-to-tensorflow-a2d27a8e44f4*

Experiment 3 (multi loss error - different weights)
----
``H2: ¿Cual es el efecto de cada error de pérdida (y y sigma) al actualizar los pesos de la red?``

- Conclusión:  Se suma un factor al error de cada componente (y y sigma). Sólo se necesita propagar una pequeña proporción de sigma. Un factor de 0.5 en sigma mantiene aproximadamente  los mismos resultados de predicción. 
 
Experiment 2 (single Loss Error - only y error)
------
``H3: ¿Qué sucede si sólo propagamos el error de y mientras mantenemos actualizada la sigma al vuelo?``

- Conclusión: Las predicciones de sigma no varían con los datos de entrada.
