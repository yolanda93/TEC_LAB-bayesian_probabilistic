# Estadística bayesiana y Deep Learning

## Introducción a estadística bayesiana y su relación con deep learning

- [La estadística bayesiana y la incertidumbre](#la-estadistica-bayesiana-y-la-incertidumbre)
  - [Teorema de Bayes](#Teorema-de-bayes)
- [Introducción a Deep Learning Bayesiano](#introduccion-a-deep-learning-bayesiano)
  - [Ventajas de esta técnica para obtener la incertidumbre](#ventajas-de-esta-tecnica-para-obtener-la-incertidumbre)


### La estadística bayesiana y la incertidumbre

La **estadística bayesiana** es un subconjunto del campo de la estadística en la que la evidencia sobre el verdadero estado del mundo se expresa **en términos de grados de creencia, es decir, trata la modelización de la incertidumbre**.

Con este enfoque podemos estimar la 'probabilidad de que una hipótesis sea cierta' (incertidumbre de la hipótesis), que llevado al campo de ML nos permite representar un modelo ML como el conjunto de asunciones o hipótesis que realiza y la probabilidad de que esas asunciones se acerquen a la realidad.

Sin embargo, esta incertidumbre actualmente no se modela ya que **los modelos de ML se basan más en estadística frequenstita** que a diferencia de la bayesiana realiza inferencias sin expresar esta incertidumbre al respecto, evaluando las hipótesis en términos absolutos usando las evidencias disponibles y de acuerdo a unos ciertos umbrales de aceptación de tal hipótesis (p-values, CI, etc)

Cómo resultado de aplicar este enfoque podríamos obtener la distribución (posterior) de los parámetros del modelo y no sólo puntos de estimación como se puede observar en la siguiente fórmula:

#### Teorema de Bayes

La formulación matemática del enfoque bayesiano utiliza [el teorema de bayes](https://es.wikipedia.org/wiki/Teorema_de_Bayes), descrito mediante la siguiente fórmula:

<p align="center">
  <img src="/docs/assets/formula_bayes.png" />
</p>

En la fórmula matemática anterior podemos ver un ejemplo de cómo calcular estas probabilidades, usando el teorema de bayes. Este teorema por definición trata de calcular las probabilidades subjetivas que puede tomar un determinado suceso cuando hemos recibido algún tipo de información previa. Para ello, se calcula la probabilidad a posteriori P(A|B), en base a las probabilidades a priori o P(A) y la probabilidad de que se dé el suceso B si la hipótesis A es cierta, P(B|A). [1]


### Introducción a Deep Learning Bayesiano
El *Deep Learning Bayesiano* es una técnica que ofrece este enfoque bayesiano, respecto al enfoque convencional frequentista, para estimar la incertidumbre de las inferencias de los modelos de Deep Learning

Esta técnica nos permite estimar además la fiabilidad del modelo, no sólo con los datos disponibles, sino también en tiempo de inferencia y para cada una de las predicciones lo que nos ofrece unas [propiedades muy ventajosas](#why_tecnica)

#### Bayesian Deep Learning

La técnica de *Deep Learning Bayesiano* utiliza el enfoque bayesiano para remplazar los pesos deterministicos de una red con distribucciones sobre estos parámetros. Es decir, en vez de optimizar los pesos de la red directamente, se optimiza sobre la distribucción de los posibles valores que estos parámetros pueden tomar, aplicando lo que se conoce como marginalización*

* *NOTA: Esta distribucción de parámetros inicial junto con la selección de la arquitectura de red y los datos disponibles forman parte de nuestras hipótesis iniciales en el teorema de bayes*

La marginalización u optimización de la distribución de los pesos de la red, nos permite estimar a su vez la distribución de posibles valores en cada inferencia realizada. 

<p align="center">
  <img src="/docs/assets/bayes/bdl.png" width="300" height="300"/>
</p>


Por tanto, el Deep Learning Bayesiano tiene 2 puntos clave:
* Parámetros del modelo probabilisticos y no deterministicos
* Una sálida del modelo que es una distribución de probabilidad y no un punto de estimación

#### Ventajas de esta técnica para obtener la incertidumbre

La técnica de *Deep Learning Bayesiano* permite estimar la variación del error de cada una de las predicciones

Esto es importante por los siguientes aspectos:

- **Estimar en tiempo real el rendimiento del modelo**. Normalmente cuando se quiere cuantificar el rendimiento (o variación del error) en las inferencias de los modelos se utilizan técnicas de sampleo (bootstrapping, cross-validation, etc) sobre los datos disponibles utilizando métricas cómo  precisión, recall, etc. Sin embargo, esta metodología de evaluación sólo utiliza el conjunto de datos disponibles extrapolando esta medida a los datos reales (no disponibles) cuya distribucción puede variar significativamente. Estas posibles variaciones del rendimiento del modelo sobre los datos no disponibles es lo que permite estimar esta técnica. (ver [Terminologia](#conceptos_clave))

- **Obtener una medida de incertidumbre fiable e interpretable**. Este caso se da con la probabilidad resultado de la operación softmax en clasificación.

    - En un problema de clasificación cuando una imagen no corresponde a ninguna de las características de las imagenes con etiquetas del dataset de entrenamiento el resultado de clasificación binaria sería (50/50), sin embargo la probabilidad obtenida tras la operación softmax devuelve cualquier cosa entre (0/100)-(100/0). Por ejemplo, pongamos una imagen de un pájaro, respecto a el conjunto de entrenamiento que contiene imágenes de gatos y perros. El resultado esperado sería obtener la máxima incertidumbre, es decir, 50% probabilidad de ser perro y 50% de ser gato, sin embargo podría dar perfectamente un alto grado de confianza sobre gato 80% y 20% en perro. 

- **Estimación de la incertidumbre de cada inferencia**. Adicionalmente las técnicas convencionales calculan una distribucción del error de las predicciones sobre el conjunto de datos no por cada una de las inferencias, construyendo lo que se conoce como intervalos de confianza. Es decir con esto somos capaces de obtener la probabilidad de obtener una precisión mayor o igual a un CI o umbral de intervalo pero no la probabilidad de 'acierto' de una estimación concreta

### Referencias

[1] https://www.bbvanexttechnologies.com/bayesianos-viendo-la-inteligencia-artificial-desde-otro-prisma/
    
