# Estimación de la incertidumbre - Detalle de los aprendizajes de experimentos

Tabla de Contenidos
=================

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
---

# Aprendizajes de experimentos


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

<h3 id="conclusiones">Conclusiones de la técnica</h3>

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