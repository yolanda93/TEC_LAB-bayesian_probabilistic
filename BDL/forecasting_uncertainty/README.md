# Forecasting Uncertainty

## Contexto

### ¿Por qué estimación de la incertidumbre en problemas de Forecasting?

El problema de forecasting realiza inferencias a futuro utilizando datos del pasado. Se podría considerar un caso particular de regresión en el que las variables independientes son dependientes del tiempo. Se ha detectado especial aplicabilidad de las técnicas probabilísitcas debido a la gran incertidumbre presente al realizar inferencias a futuro.  

Está necesidad se ha detectado tras realizar un research en la industria y en BBVA Next Technologies. En  concreto se tiene como referencia la competición [M5 Forecasting Uncertainty de Kaggle](https://www.kaggle.com/c/m5-forecasting-uncertainty) en la que se pretende aplicar las técnicas estudiadas en este contexto.

### Aproximación de la línea

La manera de resolver este problema o necesidad tomará como referencia el trabajo realizado por Axel Brando que utiliza la técnica [UMAL](https://arxiv.org/abs/1910.12288)

Tras una sesión introductoria con Axel a la técnica UMAL, decidimos realizar un estudio de las siguientes técnicas:
* *Regresión Cuantílica* cómo método para la estimación de la incertidumbre aleatórica
* *LSTM* como baseline de referencia para realizar inferencias en problemas de forecasting con suficientes datos

Asunciones:
* Al tener suficientes datos se considera que un modelo de Deep Learning tipo LSTM se puede tomar como baseline
* Al contar con suficientes datos la incertidumbre por aproximación (underfitting) e incertidumbre epistémica se consideran despreciables y nos centramos en la aleatórica

### M5 Forecasting Uncertainty de Kaggle

El reto propuesto de esta competición, propuesta por la cadena de supermercados Wallmart, trata de predecir las ventas de productos en varias localización para dos periodos de tiempo de 28 dias. Las tiendas se encunentran en los estados de California, Texas, y Wisconsin






