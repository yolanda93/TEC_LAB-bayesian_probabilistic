# Estimación de la Incertidumbre 

Dentro del aporte de valor que pueden realizar las técnicas bayesianas, está la estimacion de la incertidumbre.

El reto de la estimación de la incertidumbre tiene como objetivo ofrecer una **medida de fiabilidad** sobre las predicciones de un modelo de Machine Learning o Deep Learning.

Esto es importante para poder **cuantificar el margen de error cometido en las predicciones** de un modelo en escenarios con **alta incertidumbre**. 

Un ejemplo de este escenario lo podemos ver en [problemas de predicción de ventas de producto](poc_forecasting_uncertainty) en los que se plantean cuestiones con alta incertidumbre como ¿Cuántos equipamentos de acampada vamos a vender el mes que viene? Ser capaces de dar una estimación de por ejemplo 50 equipamentos con un margen de error bajo (e.g. +-4) o alto (e.g. +-30) nos podría ayudar a optimizar mejor las campañas de ventas y evitar costes innecesarios

## Indice de contenidos

* [La inferencia bayesiana y la estimación de la incertidumbre](uncertainty_estimation_problem.md)
* [La estimación de la incertidumbre y deep learning](bayesian_statistics_and_deep_learning.md) 
* [Contexto del reto en la industria](industry_uncertainty_estimation.md)
* [Listado de técnicas exploradas](techniques_summary.md)
* [PoC: Forecasting de ventas de producto](poc_forecasting_uncertainty) *Aplicación en una problemática real de las técnicas presentadas*
* [Proximos pasos](uncertainty_estimation_next_steps.md)
* [Preguntas frecuentes](#preguntas-frecuentes)
* [Documentos de referencia](#documentos-de-referencia)
* [Recursos externos](#recursos)
* [Presentacion Ejecutiva del Reto](https://docs.google.com/presentation/d/1mRkL54FNAwC0YNSKmbeWWg-IJNR2ch6oCLktIXDMjfc) 
* [Listado detallado de experimentos](/docs/experimentos_labs/README.md) *Experimentos realizados con datos sintéticos para profundizar en las técnicas*

## Contexto y alcance del reto

El **reto de la estimación de la incertidumbre tiene como objetivo** desarrollar técnicas de inteligencia artificial que, además de realizar su cometido, ofrezcan **una medida de fiabilidad de lo bueno que es su resultado**. Esta solución es de especial importancia de acuerdo a las directrices publicadas por comisión europea en 2018 de [Inteligencia Artificial Confiable](https://github.com/beeva/TEC_LAB-Trustworthy_AI) que responde a la necesidad de industria de construir IA segura con una visión 'human-centric' 

## Aproximación de la línea

En esta línea se hará foco en **la estadística bayesiana** cómo una solución técnica alternativa a otras técnicas de uso más extendido en en proyectos de ciencia de dato basadas en estadística frequentista. 

**La estadística bayesiana se selecciona tras** realizar un [estado del arte](https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit). y analizar el feedback recibido de universidades y otros expertos en IA de las técnicas utilizadas para la resolución de este reto. Marcando cómo principal objetivo de la línea ganar conocimiento en las límitaciones y ventajas de estas técnicas frente a las utilizadas actualmente en este contexto.

**Inicialmente se propone validar estas técnicas en el contexto de problemas de regresión** sobre datos sintéticos y datasets pequeños para explotar sus capacidades en un entorno controlado. **Posteriormente, se propone llevarlo a un entorno de pruebas real** dentro de una problemática detectada de gran aplicabilidad como es **la problemática de forecasting** con el objetivo de explotar estas técnicas con datos reales y ofrecer una referencia de uso de las mismas.

## Preguntas frecuentes

### ¿Qué tipo de incertidumbre estamos intentando modelar cuando hacemos experimentos con obs. que se alejan en eje X en función de la Y de los datos de entrenamiento? 

Incertidumbre epistémica: Es un error reducible que se está dando por falta de datos en un intervalo

*Nota: El resultado de este experimento fue que obteniamos una varianza proporcional al alejamiento en el eje X*

### ¿Cómo se podría probar la incertidumbre aleatorica heterocedástica? 

Para probar la incertidumbre aleatórica es necesario introducir error en la sálida de la red (predicciones de la red) en datos de testing. Este error no puede ser igual al error conocido, es decir, en nuestro caso el prior es una distribución normal y potencialmente distinto de la distribucción del error real de los datos de entrenamiento.
La incertidumbre heterocedástica es aquel error que puede provenir de distintas fuentes. Por tanto, necesitamos N procesos distintos generadores de ese ruido aleatórico.

### ¿Cómo podríamos modelar una incertidumbre conocida e.g. dist.laplace, exponencial?

Solución Naive:
Cambiando la función de pérdida de la red para optimizar los valores de los parámetros de la distribución conocida.
Para el cálculo de la función que máximiza el valor de los parámetros para un conjunto de datos se utiliza el algoritmo de MLE (Maximum Likelihood Estimation)



## Documentos de referencia

- **Estado del Arte**:
https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit

- **Sprint [27 de Nov - 11 de Dec] 2019**
https://docs.google.com/document/d/1bp_Rl6-gARMsEufxQt622elKwv38dIKmtIs2tWVcrOc/edit#heading=h.et9co8t7x85v

- **Sprint 4Q7S - 2019 - Validación de métodos de estimación con incertidumbre**
https://docs.google.com/document/d/1DkcUwaWw3lTW_1ylt3POmfGURaD08xCuaUBYcRnc_5U/edit

- **Sprint 1Q2S - 2020 - Estimación de la Incertidumbre - Validación - Scoring**
https://docs.google.com/document/d/110_gQ9yhVaELgoZJfjLxlWeL_D8YyORFrRyxF1da4UM/edit

## Recursos 

* [Video Lecture - Introduction to Bayesian data analysis - part 1: What is Bayes?](https://www.youtube.com/watch?v=3OJEae7Qb_o)
* [Video Discussion - Is bayesian the most brilliant thing ever?](https://www.youtube.com/watch?v=HumFmLu3CJ8)

