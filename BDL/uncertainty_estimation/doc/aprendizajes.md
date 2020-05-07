# Estimación de la incertidumbre - Aprendizajes

Tabla de Contenidos
=================

-   [Introducción](#introduccion)
    -   [Contexto en la industria](#contexto)
    -   [Introducción general a la técnica](#intro_bdl)
    -   [Terminología](#conceptos_clave)
    -   [Estado del arte y pasos iniciales](#scope)
-   [Framework: Validación de las medidas de incertidumbre](#Framework)
    -   [State-of-Art](#state-of-art)
    -   [Experimentos](#experimentos)
-   [Técnicas No Bayesianas](#non_bay)
-   [Técnica: Exp.I - Estimacion de la varianza al vuelo](#exp_I)
    -   [Experimentos - Validación inicial de estimación de incertidumbre](#experimentos_1)
    -   [Experimentos - Validación de la interpretación de incertidumbre](#experimentos_2)
    -   [Experimentos - Compatibilidad de frameworks](#experimentos_3)
    -   [Experimentos - Validación ruido no gausiano](#experimentos_4)
    -   [Experimentos - Validación datasets reales](#experimentos_5)
    -   [Conclusiones](#conclusiones)
-   [Redes de densidad mixta](#mdn)
    -   [Motivación](#mdn_motivacion)
    -   [Experimentos y conclusiones](#mdn_exp-conclusiones)
-   [Proximos pasos](#prox)
-   [Documentos de referencia](#doc_ref)
---

# Aprendizajes
<h2 id="introduccion">Introducción</h2>


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

<h2 id="exp_I">Técnicas No Bayesianas</h2>

<h2 id="exp_I">Técnica: Exp.I - Estimacion de la varianza al vuelo</h2>

Para comenzar con el modelo más simple, se seleccionó el enfoque de aprendizaje al vuelo, donde el modelo va aprendiendo del error de sus propias predicciones durante el entrenamiento. No obstante, este método es una técnica aislada que se encontró, por lo que había duda sobre su validez o si los resultados se debían a como estaba diseñado el experimento.

<h3 id="experimentos_1">Experimentos Iniciales - Validación de la estimación de incertidumbre</h3>

Tras una replicación inicial, se plantearon las siguientes hipótesis:

* [¿Sigue funcionando si se introduce ruido no gausiano?](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.1-nongaussian_noise/predicting-uncertainty-addedNonGaussianNoise.ipynb) El resultado fue que el algoritmo mantenía su comportamiento.

* [Si se predice lejos de los datos existentes ¿aumenta la incertidumbre como es de esperar?](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.2-data_faraway_original/predicting-uncertainty-PredictionFarAwayFromSignal.ipynb) El resultado fue que la incertidumbre aumentaba linealmente a medida que se alejaba de los datos conocidos.
* [Si se añaden muestras lejos de los datos existentes ¿Se reduce la incertidumbre en la zona con datos como es de esperar?](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.2-data_faraway_original/predicting-uncertainty-AddedDataFarAwayFromOriginal.ipynb) En este caso, la varianza no aumentaba entre los datos, por lo que el comportamiento no era el esperado.

* [Añadir la varianza durante el entrenamiento ¿hace que el modelo prediga peor?](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.3-loss_function_customization/predicting-uncertainty-withoutvar.ipynb) El resultado fue que la diferencia en el error era despreciable.

**Conclusiones finales**

Estos experimentos sirvieron para hacer una validación inicial de que el valor de la estimación de la varianza o incertidumbre era correcto en aquellos casos (extremos) donde se espera que el nivel de incertidumbre sea alto. **Estos experimentos por tanto nos permitieron aceptar está técnica para modelar la incertidumbre epistémica**

<h3 id="experimentos_2">Experimentos - Validación de la interpretación de incertidumbre </h3>

Dado que el modelo aprende la incertidumbre de la predicción y la predicción a la vez, se plantearon las hipótesis relacionadas con la implementación y modelización de la técnica:

* H1: ¿Se comporta igual si se entrenan por separado las dos variables que si se tratan de forma conjunta? (Exp.2. Single Loss Error)
* H2: ¿Cual es el efecto de cada error al actualizar los pesos de la red?
* H3: ¿Qué ocurre si sólo propagamos el error de la predicción mientras mantenemos al vuelo el error de la incertidumbre?
* H4: En la implementación de esta técnica se utilizan 1 tensor que agrega 2 variables objetivo (y, sigma) (2 errores distintos a propagar). ¿Es este el método común o la mejor manera de aproximar el problema?

[Estos experimentos](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.3-loss_function_customization/loss_error_experiments.ipynb) llevaron a una serie de [conclusiones](https://docs.google.com/document/d/1DkcUwaWw3lTW_1ylt3POmfGURaD08xCuaUBYcRnc_5U/edit#) que se pueden resumir en las siguientes:

* H1: Es posible, incluso recomendable, entrenar la red para ajustando la variable 'y' y posteriormente ajustar la varianza con esta red ya pre-entrenada.
* H2: Se han realizado experimentos sumando un factor al error de cada componente (y y sigma). Sólo se necesita propagar una pequeña proporción de sigma. Un factor de 0.5 en sigma mantiene aproximadamente los mismos resultados de predicción.
* H3: Las predicciones de sigma no varían con los datos de entrada. Por tanto, no se aprende un error heteroscedastico.
* H4: Revisando distintas implementaciones por compatibilidad se recomienda tener 2 tensores en el que se haga la media de los errores. Sin embargo, se ha comprobado que la función de Keras hace esta agregación internamente al calcular el MSE.

Finalmente tras estos experimentos se extrayeron las siguientes conclusiones y/o limitaciones de la técnica:

* Datos con distribuciones de entrada aproximables a una monomodal (la arquitectura de red optimiza a la media)
* Se ha probado en problemas de predicción. Para clasificación sería necesario cambiar la función de pérdida.
* La función de incertidumbre debe poder ser usada como función de pérdida en el entrenamiento.
* Este método se basa en que existe una covarianza entre la distribución de las predicciones y el error de las predicciones. Aprende cómo varía el error a medida que varía la predicción.
* Este método está pensado para usarse sobre una red ya entrenada y con buena precisión en los valores de predicción. La distribución del error de las predicciones en entrenamiento tiene que ser muy parecida a la distribución del error en validación. De este modo, el error de las predicciones con respecto a los datos de entrenamiento ofrece información sobre la incertidumbre de las predicciones.

<h3 id="experimentos_3">Experimentos - Compatibilidad de Frameworks</h3>

Para intentar utilizar bibliotecas estándar con este método en lugar de código realizado por nosotros se intentó [reimplementar utilizando Keras](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.4-loss_function_frameworks/keras_implementation.ipynb). Las [conclusiones](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.4-loss_function_frameworks/conclusions.md) de este experimento son que no hay una forma sencilla de implementarlo, ya que las bibliotecas tradicionales no permiten modificar el resultado de la función de pérdida al vuelo. No obstante, sí es posible realziarlo con pytorch.

<h3 id="experimentos_4">Experimentos - Validación ruido no gausiano</h3>

Estos experimentos se realizaron con el objetivo era validar la siguiente hipótesis:

- Modelización de incertidumbre aleatórica generada con ruido no gausiano

Conclusiones:

- El método tiene carencias a la hora de modelizar ruido aleatórico no gausiano del tipo heterocedastico
- El tipo de distribucción aprendida para la estimación de la incertidumbre tiene a una aprox.normal

<h3 id="experimentos_5">Experimentos - Validación datasets reales</h3>
    
En cualquier caso, los resultados continuaban siendo sobre el conjunto de valores que se habían seleccionado para el experimento originalmente, por lo que se decidió [probar con un dataset real de valores inmobiliarios](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.1.6-real_datasets/uncertainty_prediction_house_prices.ipynb) que contuviese valores heterocedásticos. Las [conclusiones de usar este dataset](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.1.6-real_datasets/conclusions.md) fueron que, si bien se suavizan las varianzas, el algoritmo se comporte como era de esperar y permite descartar aquellas predicciones no válidas.

<h3 id="conclusiones">Conclusiones Finales</h3>

*Interpretación Bayesiana*

Dado este experimento surgió la duda de por qué este método se puede considerar bayesiano. Para que el método se pueda considerar bayesiano debe tener una probabilidad a priori y otra a posteriori. En este caso, se vío que el prior estaba implícito en el cálculo de la función de pérdida que asume que el error de las predicciones se distribuye según una distribucción gausiana. Los parámetros de esta distribución son la varianza y la media, entendida como las predicciones de y, que se actualizan o ajustan en cada iteracción de entrenamiento de la red.
(https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V0.0.5-bayesian_interpretation)

De este punto se aprendió la importancia de explicitar, o detectar el prior implícito, para poder elegir el método adecuado a aplicar.

*Limitaciones de la técnica*

También se ha de tener en cuenta que la solución buscada introduce un sesgo sobre el tipo de distribución de la solución. Así, si se busca una media y una varianza implicitamente se está buscando una distribución gausiana, lo cual puede no ser coherente con el método o el problema

Visto el comportamiento del algoritmo se identificaron los siguientes problemas:
* Limitaciones en la modelización de incertidumbre aleatórica hereocedastica
* Tener otros métodos de referencia para comprobar el aporte de valor
* Obtener una definición de incertidumbre en este contexto
* Otros métodos de medicción de la incertidumbre que permitieran modelar distintas familias de distribucciones

Con respecto a tener una referencia, se recopilación una serie de [métodos no bayesianos de medir la incertidumbre](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V1.0.0-nonbayesian_techniques), así como sus ventajas y limitaciones, para poder compararlos.

El problema de la definición de la incertidumbre se vio más complejo, ya que era dependiente del problema y el contexto, además de que no parecía haber un consenso sobre ello en la academia.
Tras revisar como se maneja [este concepto en otros entornos](https://docs.google.com/document/d/110_gQ9yhVaELgoZJfjLxlWeL_D8YyORFrRyxF1da4UM/edit),se llegó a varias [conclusiones](https://docs.google.com/document/d/110_gQ9yhVaELgoZJfjLxlWeL_D8YyORFrRyxF1da4UM/edit), siendo la principal que las técnicas más comúnmente utilizadas como referencia son RMSE (teniendo la limitación de que la distribución debe ser gausiana) y NLL (sin esa limitación). 

<h2 id="mdn">Redes de densidad mixta </h2>

<h3 id="mdn_motivacion"> Motivación</h3>

Además de estudiar los métodos expuestos anteriormente, se exploraron las [redes de densidad mixta (MDN)](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V3.0.0-mixture_density_networks), [aplicándolas también al dataset inmobiliario](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.1.6-real_datasets/uncertainty_prediction_house_prices_mdn.ipynb). Se decidió estudiar está técnica, además de por las limitaciones expuestas anteriormente, por el trabajo realizado por Axel Brando de BBVA Data y expuesto en la conferencia anual de IA Factory.

<h3 id="mdn_exp-conclusiones">Experimentos y conclusiones</h3>
   
Este método en contraposición con lo validado en el Exp.I de estimación de incertidumbre al vuelo presentan las siguientes ventajas que se pueden resumir a mayor libertad en la definición del prior:

 - Permite modelar facilmente que el ruido provenga de distintas familias de distribucciones 
 - Pueden modelar ruido multimodal, es decir, que no sólo provenga de una sola distribución si no de la suma de varias distribucciones de la misma familia con distintos parámetros. Este prior, sin embargo, también esta implicito en el exp.I y no es fácilmente modificable.
 - Tienen más soporte, es decir, el método está más comunmente aceptado. 

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
