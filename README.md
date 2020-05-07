# Estimación de la Incertidumbre - Bayesian Probabilistic

## Documentacion complementaria
* [Experimentos](/BDL/uncertainty_estimation)
* [Presentation](https://docs.google.com/presentation/d/1mRkL54FNAwC0YNSKmbeWWg-IJNR2ch6oCLktIXDMjfc)

## Aprendizajes 

-   [Contexto en la industria](#contexto)
-   [Introducción general a la técnica](#intro_bdl)
-   [Terminología](#conceptos_clave)
-   [Estado del arte y pasos iniciales](#scope)
-   [Aprendizajes de Experimentos](/BDL/uncertainty_estimation/doc/aprendizajes.md)
-   [Conclusiones](#conclusiones)
-   [Proximos pasos](#prox)
-   [Documentos de referencia](#doc_ref)


<h3 id="contexto">Contexto en la industria</h3>

La técnica de *deep learning bayesiano* se seleccionó con la intención de obtener conocimiento de técnicas de inteligencia artificial que, además de realizar su cometido, ofreciesen una medida de fiabilidad de lo bueno que era su resultado. Esta solución es de especial importancia de acuerdo a las directrices publicadas por comisión europea en 2018 de [Inteligencia Artificial Confiable](https://github.com/beeva/TEC_LAB-Trustworthy_AI) que responde a la necesidad de la industria en construir IA con una visión 'human-centric'

En particular, se ha visto que esta técnica ofrece las siguientes ventajas:

* [**Interpretabilidad**](https://github.com/beeva/TEC_LAB-Trustworthy_AI/blob/master/pages/areas/transparencia.md): Ofrece una medida de incertidumbre y/o confianza que permita entender las variaciones en el comportamiento del modelo o cuantificar/acotar el riesgo de las predicciones

    -   **Precisión vs. Explicabilidad**: [Dentro de este reto](https://github.com/beeva/TEC_LAB-Trustworthy_AI/blob/master/pages/retos/precision-explicabilidad.md), es importante destacar, que en particular los modelos de deep learning, tiene la desventaja de ser *modelos de caja-negra*, es decir, las inferencias suelen ser más precisas pero a la vez también son más dificiles de explicar. Está técnica nos permite mejorar la explicabilidad de los modelos Deep Learning sin penalizar su rendimiento.

* [**Robustez**](https://github.com/beeva/TEC_LAB-Trustworthy_AI/blob/master/pages/areas/robustez.md): Mejorar la respuesta del modelo ante situaciones adversas. Esta técnica nos podría *filtrar predicciones con un nivel de incertidumbre alto o baja confianza*. Estos son los casos en los que no se tenga mucha confianza en las predicciones (e.g. se sospecha que el modelo está sobre-ajustado, sistemas con comportamientos variables, falta de datos o desconocimiento del problema a modelar).

* [**Ética y responsabilidad**](https://github.com/beeva/TEC_LAB-Trustworthy_AI/blob/master/pages/areas/sesgo.md): Al no ser posible cuantificar la incertdumbre o el grado de certeza de las inferencias de los modelos, se podrían *tomar decisiones automatizadas erroneas sin ser incluso capaces de cuantificar los daños*, en el caso de que no se comportará de la forma esperada. De esta manera, esta técnica, nos permitiría detectar estos casos y no realizar una toma de decisiones automatizada trasladando esta responsabilidad al humano. 

<h3 id="intro_bdl">Introducción general a la técnica</h3>

#### ¿Cómo funciona?

#### Introducción 
El *Deep Learning Bayesiano* es una técnica que da un enfoque bayesiano, respecto al enfoque convencional basado en estadística frequentista, para estimar la incertidumbre de las inferencias de modelos de Deep Learning

La estadística bayesiana a diferencia de la estadística frequentista (o técnicas convencionales) permite estimar la 'probabilidad de que una hipótesis sea cierta' (incertidumbre de la hipótesis), es decir, interpreta un modelo como el conjunto de asunciones o hipótesis que realiza y la probabilidad de que esas asunciones se acerquen a la realidad. Sin embargo, en el caso de la estadística frequentista se utiliza un enfoque determinista en el que se evalua la concordancia de las hipótesis en terminos absolutos usando las evidencias disponibles y de acuerdo a unos ciertos umbrales de aceptación de tal hipótesis (p-values, CI, etc) sin expresar la incertidumbre al respecto

La formulación matemática de este enfoque utiliza [el teorema de bayes](https://es.wikipedia.org/wiki/Teorema_de_Bayes), descrito mediante la siguiente fórmula:

<img src="https://render.githubusercontent.com/render/math?math=P(H|D) = \frac{ P(D|H)P(H)}{P(D)}">


#### Bayesian Deep Learning

La técnica de *Deep Learning Bayesiano* utiliza el enfoque bayesiano para remplazar los pesos deterministicos de una red con distribucciones sobre estos parámetros. Es decir, en vez de optimizar los pesos de la red directamente, se optimiza sobre la distribucción de los posibles valores que estos parámetros pueden tomar, aplicando lo que se conoce como marginalización*

* *NOTA: Esta distribucción de parámetros inicial junto con la selección de la arquitectura de red y los datos disponibles forman parte de nuestras hipótesis iniciales en el teorema de bayes*

La marginalización u optimización de la distribución de los pesos de la red, nos permite estimar a su vez la distribución de posibles valores en cada inferencia realizada. 

<p align="center">
  <img src="assets/bdl.png" width="300" height="300"/>
</p>

#### ¿Por qué es importante?

La técnica de *Deep Learning Bayesiano* permite estimar la variación del error de cada una de las predicciones

Esto es importante por los siguientes aspectos:

- **Estimar en tiempo real el rendimiento del modelo**. Normalmente cuando se quiere cuantificar el rendimiento (o variación del error) en las inferencias de los modelos se utilizan técnicas de sampleo (bootstrapping, cross-validation, etc) sobre los datos disponibles utilizando métricas cómo  precisión, recall, etc. Sin embargo, esta metodología de evaluación sólo utiliza el conjunto de datos disponibles extrapolando esta medida a los datos reales (no disponibles) cuya distribucción puede variar significativamente. Estas posibles variaciones del rendimiento del modelo sobre los datos no disponibles es lo que permite estimar esta técnica. (ver [Terminologia](#conceptos_clave))

- **Obtener una medida de incertidumbre fiable e interpretable**. Este caso se da con la probabilidad resultado de la operación softmax en clasificación.

    - En un problema de clasificación cuando una imagen no corresponde a ninguna de las características de las imagenes con etiquetas del dataset de entrenamiento el resultado de clasificación binaria sería (50/50), sin embargo la probabilidad obtenida tras la operación softmax devuelve cualquier cosa entre (0/100)-(100/0). Por ejemplo, pongamos una imagen de un pájaro, respecto a el conjunto de entrenamiento que contiene imágenes de gatos y perros. El resultado esperado sería obtener la máxima incertidumbre, es decir, 50% probabilidad de ser perro y 50% de ser gato, sin embargo podría dar perfectamente un alto grado de confianza sobre gato 80% y 20% en perro. 

- **Estimación de la incertidumbre de cada inferencia**. Adicionalmente las técnicas convencionales calculan una distribucción del error de las predicciones sobre el conjunto de datos no por cada una de las inferencias, construyendo lo que se conoce como intervalos de confianza. Es decir con esto somos capaces de obtener la probabilidad de obtener una precisión mayor o igual a un CI o umbral de intervalo pero no la probabilidad de 'acierto' de una estimación concreta. 
    
<h3 id="conceptos_clave">Terminología</h2>

Dentro de este reto se estudiaron los siguientes conceptos clave:

* **Homocedasticidad**: Todas las muestras tienen el mismo error de medición. Es decir, la varianza de este error se mantiene más o menos constante u homogénera
* **Heterocedasticidad**: Las muestras tienen diferentes errores de medición (no todas son igual de fiables). En este caso el valor de la varianza de las predicciones varía a lo largo del tiempo.

* **Incertidumbre epistémica**: Los datos no representan completamente el problema a modelar. También está relacionado con la correcta calibración del modelo. *Esto es importante en datasets pequeños y dispersos y en aplicaciones críticas*
* **Incertidumbre aleatoria**: Los datos tienen una variabilidad asociada intrínseca que no se ajusta al error esperado. *Importante en aplicaciones en tiempo real con mucho ruído., e.g. stock market*

<h3 id="scope">Estado del Arte y pasos iniciales</h2>

El interés en este campo se inició tras conversaciones con universidades y otros expertos en IA sobre las áreas más candentes dentro de las técnicas bayesianas

Inicialmente se realizó un [estado del arte de las técnicas existentes](https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit). De este informe se destacaron tres posibles experimentos por los que empezar:
* Aprendizaje al vuelo (a.k.a experimento uno)
* Clasificación con BDL (Bayesian Deep Learning) (a.k.a semáforos)
* MonteCarlo Dropout

<h2 id="prox">Proximos pasos </h2>

*Monte Carlo Dropout*
  
Respecto a la clasificación con BDL, se revisó el [experimento que utilizaba Montecarlo dropout](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V4.3.0-traffic_lights), pero no se pudo profundizar suficiente para entender su comportamiento. Tras realizar una revisión del estado del arte se vió que este método estaba ampliamente aceptado en la comunidad científica y se utilizaba como baseline en distintos benchmarks.

*Metodología y/o Framework de Validación*

El enfoque de validación de estos experimentos ha ido guiado por la generación de datos sintéticos para modelizar distintos escenarios. Dentro de este metodología se ha visto que para comprobar la robustez del modelo es importante validar en casos extremos cambiando el proceso de generación de datos para que se ajuste a distintas distribuciones. Revisando posteriormente el estado del arte se vió que en muchas publicaciones cientificas utilizaban la generación de ejemplos adversarios en un espacio de N-dimensiones como generador de banco de pruebas.

*Aplicaciones*

Dentro de otras aplicaciones interesantes que podría ofrecer esta técnica se han destacado las siguientes relacionadas con la exploración de otras formas de entrenamiento de los modelos:
- Active Learning
- Continual Learning

<h2 id="doc_ref">Documentos de referencia </h2>

- **Estado del Arte**:
https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit

- **Sprint [27 de Nov - 11 de Dec] 2019**
https://docs.google.com/document/d/1bp_Rl6-gARMsEufxQt622elKwv38dIKmtIs2tWVcrOc/edit#heading=h.et9co8t7x85v

- **Sprint 4Q7S - 2019 - Validación de métodos de estimación con incertidumbre**
https://docs.google.com/document/d/1DkcUwaWw3lTW_1ylt3POmfGURaD08xCuaUBYcRnc_5U/edit

- **Sprint 1Q2S - 2020 - Estimación de la Incertidumbre - Validación - Scoring**
https://docs.google.com/document/d/110_gQ9yhVaELgoZJfjLxlWeL_D8YyORFrRyxF1da4UM/edit
