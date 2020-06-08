## Regresión Cuantílica
En está página se explica la regresión cuantílica como solución técnica para medir la incertidumbre de las predicciones en problemas de forecasting


### Indice de contenidos
- [Introducción a la técnica](#introduccion)
  - [Cuantiles](#cuantiles)
- [Regresión cuantílica en la medición de la incertidumbre](#cuantil-incertidumbre)
  - [¿Por que utilizar intervalos de predicción o cuantiles en Forecasting?](#forecast-incertidumbre)
- [Otras aplicaciones de la regresión cuantílica](#aplicaciones)
- [Implementación de la regresión cuantílica](#implementacion)
  - [Técnicas de regresión cuantílica](#tecnicas)
  - [Validación - Función de pérdida](#validacion)


<a name="introduccion"></a>
## Introducción

La **regresión cuantílica** a diferencia de la regresión lineal convencional tiene como objetivo estimar la mediana condicional u otros **cuantiles** de la variable de respuesta

<a name="cuantiles"></a>
#### Cuantiles

El cuantil de orden τ (0<τ<1) de una distribución es el valor de la variable X que marca un corte de modo que **una proporción τ de valores de la población es menor o igual** que dicho valor. Por ejemplo, el cuantil de orden 0,36 deja un 36% de valores por debajo y el cuantil de orden 0,50 se corresponde con la mediana de la distribución

<a name="cuantil-incertidumbre"></a>
### Regresión cuantílica en la medición de la incertidumbre

En el siguiente gráfico vemos la aplicación de **regresión cuantílica en el dataset de precios de vivienda de boston**. En el ejemplo se busca el mejor ajuste para estimar el precio de la vivienda en función del número de habitaciones. Cómo se puede observar en el gráfico la varianza entre ambas variables **no es constante u homocedastica**, por lo que es necesario proporcionar una medida de fiabilidad sobre esa posible variación o margen de error de las predicciones.

En este caso conseguimos esa medida de fiabilidad mediante **el ajuste de 5 regresiones cuantiles que se corresponden con los percentiles o cuantiles** de 10, 30, 50, 70 y 90. Lo que nos proporciona un intervalo de predicción o error sobre cada predicción, en el que el cuantil 50 se corresponde con la mediana que deja justo a cada lado el 50% de las observaciones, llegando hasta los límites o cuantiles extremos en los que el intervalo [10,90] recoge el 80% de las observaciones.

 <p align="center"><img src="/docs/assets/quantile_regression/quantile_regression_example.PNG" height="350" alt=“Ejemplo de regresión cuantílica” /></p>
<p align="center"><em>Ejemplo de regresión cuantílica</em><sup>[1]</sup></p>

En este gráfico se puede observar también la pendiente de la recta de cada cuantil es distinta, lo que significa que el predictor X influye de forma distinta a cada cuantil de la variable respuesta. Es importante destacar también que la regresión cuantílica ofrece un **estimador (basado en la mediana) más robusto** que se ve menos afectado por los outliers que OLS(Ordinary Least Square) que utiliza la media

<a name="forecast-incertidumbre"></a>
#### ¿Por que utilizar intervalos de predicción o cuantiles en Forecasting?

En problemas de forecasting se suele hacer forecasting sobre distintos horizontes de tiempo. Esto tiene una implicación en la incertidumbre y varianza de las predicciones.

El cálculo de esta varianza o intervalo de predicciónen el forecasting en el h-instante (h:horizonte) de la variable respuesta y con una desviación estándar σₕ, puede ser calculada como:

 <p align="center"><img src="/docs/assets/quantile_regression/forecast_variance.png" height="50" alt=“Ejemplo de regresión cuantílica” /></p>
<p align="center"><em>Estimación de la varianza de forecasting en el instante u horizonte h</em><sup>[2]</sup></p>

La constante c depende de la cobertura de probabilidades. Estos valores se pueden encontrar [aqui](https://otexts.com/fpp2/prediction-intervals.html)

Un característica importante de los intervalor de predicción es que incrementan con el horizonte. Cuánto más lejano sea el horizonte de tiempo al que hacemos forecasting, mayor será la incertidumbre asociada con esta predicción y más amplio será el intervalo de predicción.

<a name="implementacion"></a>
### Implementación de la regresión cuantílica

<a name="validacion"></a>
####  Función de Pérdida

La **función de pérdida de la regresión cuantílica** minimiza una suma con **penalizaciones asimétricas** para las sobre-predicciones (aquellas predecciones que se realizan por encima del valor real) y las infra-predicciones (aquellas que están por debajo) de tal forma que **para un mismo quantile o valor de q, las penzalizaciones que se aplican sobre estas predicciones son diferentes**

En concreto, se observa que los errores más positivos (sobre-predicciones) son penalizados más en los cuantiles superiores (se tienen más en cuenta) y los errores más negativos (infra-predicciones) se penalizan más en los cuantiles inferiores. En el caso del cuantil 50 o mediana, se penaliza por igual

* Notebook de referencia: [quantile_regression_loss_function.ipynb](./quantile_regression_loss_function.ipynb)

<a name="tecnicas"></a>
#### Técnicas de regresión cuantílica

La regresión cuantílica se puede aplicar casi con cualquier regresor **cambiando la función de pérdida**. Entre los métodos más populares están la regresión cuantílica lineal, los métodos basados en árboles y deep quantile regression. En el siguiente notebook se puede encontrar la implementación de cada uno de ellos y el comportamiento o rendimiento sobre la problemática del dataset de precios de viviendas de boston de scikit-learn.

Métodos implementados:

* OLS Linear regression - confident intervals
* Linear quantile regression
* Random forest regression
* Gradient Boosting regression
* Deep quantile regression


* Notebook de referencia: [quantile_regression_techniques.ipynb](./quantile_regression_techniques.ipynb)

<a name="aplicaciones"></a>
### Otras aplicaciones de la regresión cuantílica

El poder realizar regresión sobre cualquier parte de la distribución permite conocer la influencia de los predictores desde el mínimo al máximo rango de la variable respuesta

https://www.semanticscholar.org/paper/La-desigualdad-salarial-de-g%C3%A9nero-medida-por-el-del-Freitas/610f046522d329e917f1b090b89fdf0da604d7dc


#### Referencias

https://medium.com/analytics-vidhya/quantile-regression-and-prediction-intervals-e4a6a33634b4

[2]  https://otexts.com/fpp2/prediction-intervals.html
