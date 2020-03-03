# Estimación de la incertidumbre - Aprendizajes

Tabla de Contenidos
=================

-   [Introducción](#introduccion)
    -   [Estado del arte y objetivos](#scope)
    -   [Terminología](#conceptos_clave)
-   [Framework: Validación de las medidas de incertidumbre](#Framework)
    -   [State-of-Art](#state-of-art)
    -   [Experimentos](#experimentos)
-   [Técnica: Exp.I - Estimacion de la varianza al vuelo](#exp_I)
    -   [Experimentos - Validación de Medida de Incertidumbre](#experimentos_1)
    -   [Experimentos - Validación Interpretación de Incertidumbre - Loss](#experimentos_2)
    -   [Experimentos - Compatibilidad de Frameworks](#experimentos_3)
    -   [Experimentos - Validación datasets reales](#experimentos_4)
    -   [Conclusiones](#conclusiones)
-   [Redes de densidad mixta](#mdn)
    -   [Motivación](#mdn_motivacion)
    -   [Experimentos y conclusiones](#mdn_exp-conclusiones)
---

# Aprendizajes


<h2 id="introduccion">Introducción </h2>

La técnica de deep learning bayesiano se seleccionó con la intención de obtener conocimiento de técnicas de inteligencia artificial que, además de realizar su cometido, ofreciesen una medida de lo bueno que era su resultado. Por tanto, esta técnica se engloba dentro de los siguientes retos de alto nivel:

* **Interpretabilidad**: Ofrecer una medida de incertidumbre y/o confianza que permita entender las variaciones en el comportamiento del modelo o cuantificar/acotar el riesgo de las predicciones

* **Robustez**. Filtramos predicciones con un nivel de incertidumbre alto o baja confianza, mejorando la respuesta del modelo. Estos son los casos en los que no se tenga mucha confianza en las predicciones (e.g. se sospecha que el modelo está sobre-ajustado, sistemas con comportamientos variables, falta de datos o desconocimiento del problema a modelar).

<h3 id="scope">Estado del Arte y Objetivos</h2>

![alt text](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/edit/master/BDL/uncertainty_estimation/doc/bdl.png)

El interés en este campo se enfocó tras conversaciones con universidades y otros expertos en IA sobre las áreas más candentes dentro de las técnicas bayesianas

Inicialmente se realizó un [estado del arte de las técnicas existentes](https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit). De este informe se destacaron tres posibles enfoques a estudiar:
* Aprendizaje al vuelo (a.k.a experimento uno)
* Clasificación con BDL (Bayesian Deep Learning) (a.k.a semáforos)
* Montecarlo Dropout

<h3 id="conceptos_clave">Terminología</h2>

Dentro de estos restos se vió que los siguientes conceptos eran claves en este área:
* **Homocedasticidad**: Todas las muestras tienen el mismo error de medición.
* **Heterocedasticidad**: Las muestras tienen diferentes errores de medición (no todas son igual de fiables)

* **Incertidumbre epistémica**: Los datos no representan completamente el problema a modelar.
* **Incertidumbre aleatoria**: Los datos tienen una variabilidad asociada intrínseca.


<h2 id="exp_I">Técnica: Exp.I - Estimacion de la varianza al vuelo</h2>

Para comenzar con el modelo más simple, se seleccionó el enfoque de aprendizaje al vuelo, donde el modelo va aprendiendo del error de sus propias predicciones durante el entrenamiento. No obstante, este método es una técnica aislada que se encontró, por lo que había duda sobre su validez o si los resulatdos se debían a como estaba diseñado el experimento.

<h3 id="experimentos_1">Experimentos - Validación de Medida de Incertidumbre</h3>

Tras una replicación inicial, se plantearon las siguientes hipótesis:
* [¿Sigue funcionando si se introduce ruido no gausiano?](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.1-nongaussian_noise/predicting-uncertainty-addedNonGaussianNoise.ipynb) El resultado fue que el algoritmo mantenía su comportamiento.

* [Si se predice lejos de los datos existentes ¿aumenta la incertidumbre como es de esperar?](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.2-data_faraway_original/predicting-uncertainty-PredictionFarAwayFromSignal.ipynb) El resultado fue que la incertidumbre aumentaba linealmente a medida que se alejaba de los datos conocidos.
* [Si se añaden muestras lejos de los datos existentes ¿Se reduce la incertidumbre en la zona con datos como es de esperar?](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.2-data_faraway_original/predicting-uncertainty-AddedDataFarAwayFromOriginal.ipynb) En este caso, la varianza no aumentaba entre los datos, por lo que el comportamiento no era el esperado.

* [Añadir la varianza durante el entrenamiento ¿hace que el modelo prediga peor?](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.3-loss_function_customization/predicting-uncertainty-withoutvar.ipynb) El resultado fue que la diferencia en el error era despreciable.

<h3 id="experimentos_2">Experimentos - Validación Interpretación de Incertidumbre - Loss </h3>

Dado que el modelo aprende la incertidumbre de la predicción y la predicción a la vez, se plantearon varias hipótesis:
* ¿Se comporta igual si se entrenan por separado las dos variables que si se tratan de forma conjunta?
* ¿Cual es el efecto de cada error al actualizar los pesos de la red?
* ¿Qué ocurre si sólo propagamos el error de la predicción mientras mantenemos al vuelo el error de la incertidumbre?
[Estos experimentos](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.3-loss_function_customization/loss_error_experiments.ipynb) llevaron a una serie de [conclusiones](https://docs.google.com/document/d/1DkcUwaWw3lTW_1ylt3POmfGURaD08xCuaUBYcRnc_5U/edit#), de donde se puede destacar que el conocimiento validado es que algoritmo funciona bajo las siguientes condiciones:
* Datos con distribuciones de entrada aproximables a una monomodal (la arquitectura de red optimiza a la media)
* Sólo se ha probado en problemas de predicción
* La función de incertidumbre debe poder ser usada como función de pérdida en el entrenamiento.
* Este método se basa en que existe una covarianza entre la distribución de las predicciones y el error de las predicciones. Aprende cómo varía el error a medida que varía la predicción.
* Este método está pensado para usarse sobre una red ya entrenada y con buena precisión en los valores de predicción. La distribución del error de las predicciones en entrenamiento tiene que ser muy parecida a la distribución del error en validación. De este modo, el error de las predicciones con respecto a los datos de entrenamiento ofrece información sobre la incertidumbre de las predicciones.

<h3 id="experimentos_3">Experimentos - Compatibilidad de Frameworks</h3>

Para intentar utilizar bibliotecas estándar con este método en lugar de código realizado por nosotros se intentó [reimplementar utilizando Keras](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.4-loss_function_frameworks/keras_implementation.ipynb). Las [conclusiones](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.0.4-loss_function_frameworks/conclusions.md) de este experimento son que no hay una forma sencilla de implementarlo, ya que las bibliotecas tradicionales no permiten modificar el resultado de la función de pérdida al vuelo. No obstante, sí es posible realziarlo con pytorch.

<h3 id="experimentos_4">Experimentos - Validación datasets reales</h3>
    
En cualquier caso, los resultados continuaban siendo sobre el conjunto de valores que se habían seleccionado para el experimento originalmente, por lo que se decidió [probar con un dataset real de valores inmobiliarios](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.1.6-real_datasets/uncertainty_prediction_house_prices.ipynb) que contuviese valores heterocedásticos. Las [conclusiones de usar este dataset](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.1.6-real_datasets/conclusions.md) fueron que, si bien se suavizan las varianzas, el algoritmo se comporte como era de esperar y permite descartar aquellas predicciones no válidas.


<h3 id="conclusiones">Conclusiones Finales</h3>

Dado este experimento surgió la duda de por qué este método se puede considerar bayesiano. Para que el método se pueda considerar bayesiano debe tener una probabilidad a priori y otra a posteriori. En este caso, se vío que el prior estaba implícito en el cálculo de la función de pérdida que asume que el error de las predicciones se distribuye según una distribucción gausiana. Los parámetros de esta distribución son la varianza y la media, entendida como las predicciones de y, que se actualizan o ajustan en cada iteracción de entrenamiento de la red.

De este punto se aprendió la importancia de explicitar, o detectar el prior implícito, para poder elegir el método adecuado a aplicar.
También se ha de tener en cuenta que la solución buscada introduce un sesgo sobre el tipo de distribución de la solución. Así, si se busca una media y una varianza implicitamente se está buscando una distribución gausiana, lo cual puede no ser coherente con el método o el problema.


Visto el comportamiento del algoritmo surgieron dos problemas:
* Tener otros métodos de referencia para comprobar el aporte de valor.
* Obtener una definición de incertidumbre en este contexto.
* Otros métodos de medicción de la incertidumbre que permitieran modelar distintas familias de distribucciones

Con respecto a tener una referencia, se recopilación una serie de [métodos no bayesianos de medir la incertidumbre](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V1.0.0-nonbayesian_techniques), así como sus ventajas y limitaciones, para poder compararlos.

El problema de la definición de la incertidumbre se vio más complejo, ya que era dependiente del problema y el contexto, además de que no parecía haber un consenso sobre ello en la academia.
Tras revisar como se maneja [este concepto en otros entornos](https://docs.google.com/document/d/110_gQ9yhVaELgoZJfjLxlWeL_D8YyORFrRyxF1da4UM/edit),se llegó a varias [conclusiones](https://docs.google.com/document/d/110_gQ9yhVaELgoZJfjLxlWeL_D8YyORFrRyxF1da4UM/edit), siendo la principal que las técnicas más comúnmente utilizadas como referencia son RMSE (teniendo la limitación de que la distribución debe ser gausiana) y NLL (sin esa limitación). 

<h2 id="mdn">Redes de densidad mixta </h2>


<h3 id="mdn_motivacion"> Motivación</h3>

Además de estudiar los métodos expuestos anteriormente, se exploraron las [redes de densidad mixta (MDN)](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V3.0.0-mixture_density_networks), [aplicándolas también al dataset inmobiliario](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.1.6-real_datasets/uncertainty_prediction_house_prices_mdn.ipynb).

<h3 id="mdn_exp-conclusiones">Experimentos y conclusiones</h3>
   
Este método en contraposición con lo validado en el Exp.I de estimación de incertidumbre al vuelo presentan las siguientes ventajas que se pueden resumir a mayor libertad en la definición del prior:

 - Permite modelar facilmente que el ruido provenga de distintas familias de distribucciones 
 - Pueden modelar ruido multimodal, es decir, que no sólo provenga de una sola distribución si no de la suma de varias distribucciones de la misma familia con distintos parámetros. Este prior, sin embargo, también esta implicito en el exp.I y no es fácilmente modificable.
 - Tienen más soporte, es decir, el método está más comunmente acetpado. 

# Proximos pasos
  
Respecto a la clasificación con BDL, se revisó el [experimento que utilizaba Montecarlo dropout](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V4.3.0-traffic_lights), pero no se pudo profundizar suficiente para entender su comportamiento.

# Documentos de referencia

- **Estado del Arte**:
https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit

- **Sprint [27 de Nov - 11 de Dec] 2019**
https://docs.google.com/document/d/1bp_Rl6-gARMsEufxQt622elKwv38dIKmtIs2tWVcrOc/edit#heading=h.et9co8t7x85v

- **Sprint 4Q7S - 2019 - Validación de métodos de estimación con incertidumbre**
https://docs.google.com/document/d/1DkcUwaWw3lTW_1ylt3POmfGURaD08xCuaUBYcRnc_5U/edit

- **Sprint 1Q2S - 2020 - Estimación de la Incertidumbre - Validación - Scoring**
https://docs.google.com/document/d/110_gQ9yhVaELgoZJfjLxlWeL_D8YyORFrRyxF1da4UM/edit
