## Estimación de la incertidumbre en Forecasting - M5 Forecasting Uncertainty

El problema de forecasting realiza inferencias a futuro utilizando datos del pasado. Se podría considerar un caso particular de regresión en el que las variables independientes son dependientes del tiempo. Se ha detectado especial aplicabilidad de las técnicas probabilísitcas debido a la **gran incertidumbre presente al realizar inferencias a futuro**.  

Está necesidad se ha detectado tras realizar un research en la industria y en BBVA Next Technologies. En concreto, se tiene como referencia la competición [M5 Forecasting Uncertainty de Kaggle](https://www.kaggle.com/c/m5-forecasting-uncertainty) en la que se pretende aplicar las técnicas estudiadas en este contexto.

Los **objetivos** y **entregables** a alcanzar en el contexto de este trabajo son:

**PoC: Predicción de incertidumbre en ventas de producto**

1. **Aplicación y validación** de técnicas de estimación de la incertidumbre en una problemática real

**Técnicas de estimación de la incertidumbre en forecasting**

2. Validación de la **solución técnica UMAL** para resolver este tipo de problemática
3. Obtener conocimiento sobre **técnicas adyacentes** con aplicación en **Forecasting** (e.g. LSTM)

## Entregables

- [PoC: Predicción de incertidumbre en ventas de producto](/poc_forecasting_uncertainty/techniques)
- [Soluciones técnicas de estimación de la incertidumbre](/poc_forecasting_uncertainty/m5_forecasting_uncertainty)

## Contexto del trabajo

### Aproximación de la línea

Para resolver este problema se utilizará como referencia el trabajo realizado por Axel Brando que utiliza la técnica [UMAL](https://arxiv.org/abs/1910.12288)

Tras una sesión introductoria con Axel a la técnica UMAL, decidimos realizar un estudio de las siguientes técnicas:
* *Regresión Cuantílica* cómo método para la estimación de la incertidumbre aleatórica
* *LSTM* como baseline de referencia para realizar inferencias en problemas de forecasting con suficientes datos

### Consideraciones previas

* Asumimos un escenario con sufientes datos, por tanto:
  * Se puede tomar un modelo de Deep Learning tipo LSTM como baseline
  * Al contar con suficientes datos la incertidumbre por aproximación (underfitting) e incertidumbre epistémica se consideran despreciables y nos centramos en la aleatórica

### Forecasting de ventas de productos

La problemática en la que nos vamos a centrar es la propuesta por la cadena de supermercados Wallmart en la competición [M5 Forecasting Uncertainty de Kaggle](https://www.kaggle.com/c/m5-forecasting-uncertainty). 

El reto propuesto en esta competición trata de predecir las ventas de productos en varias localización para un periodo de tiempo de 28 dias. Las tiendas se encunentran en los estados de California, Texas, y Wisconsin.





