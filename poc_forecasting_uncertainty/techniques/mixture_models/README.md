## Mixture Models
En está página se explica los modelos de mixturas como solución técnica para aproximar distribuciones heterogéneas de la variable respuesta. Este es el caso en el que sabemos que los datos u observaciones provienen de fuentes o procesos diferentes conocidos.


### Indice de contenidos
- [Introducción a la técnica](#introduccion)
- [Regresión cuantílica en la medición de la incertidumbre](#cuantil-incertidumbre)
  - [¿Por que utilizar intervalos de predicción o cuantiles en Forecasting?](#forecast-incertidumbre)
- [Otras aplicaciones de la regresión cuantílica](#aplicaciones)
- [Implementación de la regresión cuantílica](#implementacion)
  - [Técnicas de regresión cuantílica](#tecnicas)
  - [Validación - Función de pérdida](#validacion)


<a name="introduccion"></a>
## Introducción

La **regresión cuantílica** tiene como objetivo aproximar la mediana condicional u otros **cuantiles** (proporción τ de la distribución) de la variable de respuesta [2]

<a name="MLE - Maximum Likelihood Estimation"></a>
### MLE - Maximum Likelihood Estimation

El algoritmo de MLE o máxima verosimilitud nos permite obtener los parámetros del modelo o distribución que maximizan la probabibilidad de obtener unos datos dados.



 <p align="center"><img src="/docs/assets/quantile_regression/quantile_regression_example.PNG" height="350" alt=“Ejemplo de regresión cuantílica” /></p>
<p align="center"><em>Ejemplo de regresión cuantílica</em><sup>[1]</sup></p>



<a name="forecast-incertidumbre"></a>
#### ¿Por que utilizar intervalos de predicción o cuantiles en Forecasting?

En problemas de forecasting se suele hacer forecasting sobre distintos horizontes de tiempo. Esto tiene una **implicación en la incertidumbre y varianza de las predicciones**

El cálculo de esta varianza o intervalo de predicción en forecasting en el h-instante (h:horizonte) de la variable respuesta y con una desviación estándar σₕ, puede ser calculada como:

 <p align="center"><img src="/docs/assets/quantile_regression/forecast_variance.png" height="50" alt=“Ejemplo de regresión cuantílica” /></p>
<p align="center"><em>Estimación de la varianza de forecasting en el instante u horizonte h</em><sup>[2]</sup></p>

La constante c depende de la cobertura de probabilidades. Estos valores se pueden encontrar [aqui](https://otexts.com/fpp2/prediction-intervals.html)

Un característica importante de los intervalo de predicción es que incrementan con el horizonte. Cuánto más lejano sea el horizonte de tiempo al que hacemos forecasting, mayor será la incertidumbre asociada con esta predicción y más amplio será el intervalo de predicción

<a name="implementacion"></a>
### Implementación de la regresión cuantílica

<a name="validacion"></a>
####  Función de Pérdida

La **función de pérdida de la regresión cuantílica** minimiza una suma con **penalizaciones asimétricas** para las sobre-predicciones (aquellas predecciones que se realizan por encima del valor real) y las infra-predicciones (aquellas que están por debajo) de tal forma que **para un mismo quantile o valor de q, las penzalizaciones que se aplican sobre estas predicciones son diferentes**

En concreto, se observa que los errores más positivos (sobre-predicciones) son penalizados más en los cuantiles superiores (se tienen más en cuenta) y los errores más negativos (infra-predicciones) se penalizan más en los cuantiles inferiores. En el caso del cuantil 50 o mediana, se penaliza por igual

*Notebook de referencia: [quantile_regression_loss_function.ipynb](./quantile_regression_loss_function.ipynb)*

<a name="tecnicas"></a>
#### Técnicas de regresión cuantílica

La regresión cuantílica se puede aplicar casi con cualquier regresor **cambiando la función de pérdida**. Entre los métodos más populares están la regresión cuantílica lineal, los métodos basados en árboles y deep learning (deep quantile regression). En el siguiente notebook se puede encontrar la implementación de cada uno de ellos y el comportamiento o rendimiento sobre la problemática del dataset de precios de viviendas de boston de scikit-learn

Métodos implementados:

* OLS Linear regression - confident intervals
* Linear quantile regression
* Random forest regression
* Gradient Boosting regression
* Deep quantile regression

*Notebook de referencia: [quantile_regression_techniques.ipynb](./quantile_regression_techniques.ipynb)*

<a name="aplicaciones"></a>
### Otras aplicaciones de la regresión cuantílica

La regresión cuantílica tiene los siguientes usos y ventajas:

*Aplicación y ventajas*

* Proyectos sujetos **a gran incertidumbre** (e.g. falta de datos, gran volatilidad, mucho ruido, predicciones a futuro)
* El poder realizar regresión sobre cualquier parte de la distribución permite **conocer la influencia de los predictores desde el mínimo al máximo rango de la variable respuesta**

```
En el ejemplo anterior esto equivaldría a poder responder en el peor y el mejor de los casos cúal sería 
el precio de la vivienda, conocer estos valores te puede ayudar a hacer una mejor previsión de los ahorros
en el caso en el que haya mucha volatilidad en el precio o no sólo te interese otra carácteristica a parte 
del número de habitaciones que sospechas que puede afectar a los datos.
```

* Cuando las **condiciones de la regresion lineal no se cumplen** (homocedasticidad, normalidad, colinearidad, etc)
* **No hace asunciones de la distribución** de los residuos
* Ofrece una medida más robusta (estimamos la mediana condicionada) cuando la **distribución de los datos está sesgada** 
* Nos interesa realizar un **estudio de outliers** o sesgar la respuesta del modelo para minimizar el riesgo o por restricciones de negocio


*Ejemplos de aplicaciones*

* **Estudio de la desigualdad salarial de género**. Se estudian cuales son los factores que más afectan a la brecha salarial de género o sí los salarios más bajos se corresponden realmente con salarios de mujeres u hombres [3]

* **Estudio de tratamientos médicos** Queremos estudiar un tratamiento y queremos observar cómo se comporta en enfermedades raras y resulta muy costoso repetir el experimento o recoger más datos de ese sector poblacional 


#### Referencias

[1] https://medium.com/analytics-vidhya/quantile-regression-and-prediction-intervals-e4a6a33634b4

[2] https://otexts.com/fpp2/prediction-intervals.html

[3] https://www.semanticscholar.org/paper/La-desigualdad-salarial-de-g%C3%A9nero-medida-por-el-del-Freitas/610f046522d329e917f1b090b89fdf0da604d7dc
