## Regresión Cuantílica

La **regresión cuantílica** a diferencia de la regresión lineal convencional permite realizar regresión sobre cualquier parte de la distribución utilizando lo que se denomina como **cuantiles**

#### Cuantiles

El cuantil de orden τ (0<τ<1) de una distribución es el valor de la variable X que marca un corte de modo que **una proporción τ de valores de la población es menor o igual** que dicho valor. Por ejemplo, el cuantil de orden 0,36 deja un 36% de valores por debajo y el cuantil de orden 0,50 se corresponde con la mediana de la distribución

### Regresión cuantílica en la medición de la incertidumbre

En el siguiente gráfico vemos la aplicación de **regresión cuantílica en el dataset de precios de vivienda de boston**. En el ejemplo se busca el mejor ajuste para predecir el precio de la vivienda en función del número de habitaciones. Cómo se puede observar en el gráfico la varianza entre ambas variables **no es constante u homocedastica**, por lo que es necesario proporcionar una medida de fiabilidad sobre esa posible variación o margen de error de las predicciones.

En este caso conseguimos esa medida de fiabilidad mediante **el ajuste de 5 regresiones cuantiles que se corresponden con los percentiles o cuantiles** de 10, 30, 50, 70 y 90. Lo que nos proporciona un intervalo de predicción o error sobre cada predicción, en el que el cuantil 50 se corresponde con la mediana que deja justo a cada lado el 50% de las predicciones, llegando hasta los límites o cuantiles extremos en los que el intervalo [10,90] recoge el 80% de las predicciones.

 <p align="center"><img src="/docs/assets/quantile_regression/quantile_regression_example.PNG" height="350" alt=“Ejemplo de regresión cuantílica” /></p>
<p align="center"><em>Ejemplo de regresión cuantílica</em><sup>[2]</sup></p>

En este gráfico se puede observar también la pendiente de la recta de cada cuantil es distinta, lo que significa que el predictor X influye de forma distinta a cada cuantil de la variable respuesta

#### ¿Por que utilizar intervalos de predicción o cuantiles en Forecasting?

En problemas de forecasting se suele hacer forecasting sobre distintos horizontes de tiempo. Esto tiene una implicación en la incertidumbre y varianza de las predicciones.

El cálculo de esta varianza o intervalo de predicciónen el forecasting en el h-instante (h:horizonte) de la variable respuesta y con una desviación estándar σₕ, puede ser calculada como:

 <p align="center"><img src="/docs/assets/quantile_regression/forecast_variance.png" height="350" alt=“Ejemplo de regresión cuantílica” /></p>
<p align="center"><em>Estimación de la varianza de forecasting en el instante u horizonte h</em><sup>[1]</sup></p>

La constante c depende de la cobertura de probabilidades. Estos valores se pueden encontrar [aqui](https://otexts.com/fpp2/prediction-intervals.html)

Un característica importante de los intervalor de predicción es que incrementan con el horizonte. Cuánto más lejano sea el horizonte de tiempo al que hacemos forecasting, mayor será la incertidumbre asociada con esta predicción y más amplio será el intervalo de predicción.

#### Intervalos de predicción vs. intervalos de confianza

- **Intervalos de confianza**: Proporcionan una estimación de fiabilidad o intervalo de error sobre la media (o alguno otro parámetro) de la distribución de la población

- **Intervalos de predicción**: Proporcionan una estimación de fiabilidad o intervalo de error sobre futuras observaciones o (variables aleatorias individuales) tomadas de una población

### Otras aplicaciones de la regresión cuantílica

El poder realizar regresión sobre cualquier parte de la distribución permite conocer la influencia de los predictores desde el mínimo al máximo rango de la variable respuesta

### Cálculo de la regresión cuantílica

####  Función de Pérdida

### Técnicas de regresión cuantílica

- [OLS Linear regression - confident intervals](#ols)
- [Linear quantile regression](#linear_quantile)
- [Random forest regression](#rf_quantile)
- [Gradient Boosting regression](#gaadboost)
- [Deep quantile regression](#dqr)


#### Referencias

https://medium.com/analytics-vidhya/quantile-regression-and-prediction-intervals-e4a6a33634b4

[2]  https://otexts.com/fpp2/prediction-intervals.html
