## Aproximación inicial de la línea

Para resolver esta problemática se ha decidido tomar como referencia el trabajo realizado por Axel Brando de la técnica [UMAL](https://arxiv.org/abs/1910.12288)

Tras una sesión introductoria con Axel a la técnica UMAL, decidimos realizar un estudio de las siguientes técnicas:
* [Regresión Cuantílica](/poc_forecasting_uncertainty/techniques/quantile_regression/) cómo método para la estimación de la incertidumbre aleatórica
* [LSTM](/poc_forecasting_uncertainty/techniques/lstm/) como baseline de referencia para realizar inferencias en problemas de forecasting con suficientes datos

## Consideraciones previas de esta aproximación

* Asumimos un escenario con sufientes datos, por tanto:
  * Se puede tomar un modelo de Deep Learning tipo LSTM como baseline
  * Al contar con suficientes datos la incertidumbre por aproximación (underfitting) e incertidumbre epistémica se consideran despreciables y nos centramos en la aleatórica





