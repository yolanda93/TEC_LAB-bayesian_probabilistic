<h2 id="prox">Proximos pasos </h2>

*Monte Carlo Dropout*
  
Respecto a la clasificación con BDL, se revisó el [experimento que utilizaba Montecarlo dropout](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V4.3.0-traffic_lights), pero no se pudo profundizar suficiente para entender su comportamiento. Tras realizar una revisión del estado del arte se vió que este método estaba ampliamente aceptado en la comunidad científica y se utilizaba como baseline en distintos benchmarks.

En este caso, estamos interesados en la distribución posterior de los pesos de la red dados unos datos observados. Con ello, intentamos estimar la distribucción predictiva de la sálida y* para un nuevo xi [¿QUE ES UN XI AQUÍ?]. Es decir, dado un input x queremos obtener la distribucción sobre mi predicción. Así, muestreamos los pesos de la red sobre la distribucción posterior, que sería parecido a aproximar esta distribucción sumando las inferencias de N redes con N pesos deterministas cada una de ellas o el ensamble de estas.

No obstante, se entrará en profundiad llegado el momento.


*Metodología y/o Framework de Validación*

El enfoque de validación de estos experimentos ha ido guiado por la generación de datos sintéticos para modelizar distintos escenarios. Dentro de este metodología se ha visto que para comprobar la robustez del modelo es importante validar en casos extremos cambiando el proceso de generación de datos para que se ajuste a distintas distribuciones. Revisando posteriormente el estado del arte se vió que en muchas publicaciones cientificas utilizaban la generación de ejemplos adversarios en un espacio de N-dimensiones como generador de banco de pruebas.

*Aplicaciones*

Dentro de otras aplicaciones interesantes que podría ofrecer esta técnica se han destacado las siguientes relacionadas con la exploración de otras formas de entrenamiento de los modelos:
- Active Learning
- Continual Learning

----- Notas personales [Borrador - Yolanda proximos pasos] ----------------------------------------------------------------------------

**Pruning Deep Learning**
Aplicación en la reducción del tamaño del modelo

**Quantile Reinforcement Learning**

Hipotesis:
*For QR-DQN, instead of estimating a single value for each state-action pair, we learn a distribution of values. Knowing the distribution, rather than just the average, can improve the policy*

---
so the the policy estimates a 90% chance of getting a reward of at least 1, 70% chance of at least 4, 50% chance of at least 7, 30% chance of at least 10, and 10% chance of at least 56.
Reference: https://medium.com/@fuller.evan/quantile-reinforcement-learning-56f8b3c3f134


**Datasets**

- Darle la vuelta al problema, es decir, ser capaces de medir la incertidumbre del humano (en los datos) --> Sesgos?

- Estimación de la incertidumbre con dataset de alta dimensionalidad  


Hipotesis:

La incertidumbre también se podría modelar con modelos no paramétricos (e.g. KDE) --> Muy inestables, la asunción paramétrica no me parece un problema
Al final los modelos paramétricos hacen la asuncion de que el problema se puede modelar como una función con un número finito de parámetros.


Opinión personal

--- La incertidumbre está muy ligada al concepto de entropia
