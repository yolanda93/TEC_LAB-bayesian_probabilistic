# Estimación de la Incertidumbre 

El reto de estimación de la incertidumbre tiene como objetivo ofrecer una **medida de fiabilidad** sobre las predicciones de un modelo de Machine Learning o Deep Learning

Esto es importante para poder **cuantificar el margen de error cometido en las predicciones** de un modelo en escenarios con **alta incertidumbre**. 

Un ejemplo de este escenario lo podemos ver en [problemas de predicción de ventas de producto](/poc_forecasting_uncertainty) en los que se plantean cuestiones con alta incertidumbre como ¿Cuántos equipamentos de acampada vamos a vender el mes que viene? Ser capaces de dar una estimación de por ejemplo 50 equipamentos con un margen de error bajo (e.g. +-4) o alto (e.g. +-30) nos podría ayudar a optimizar mejor las campañas de ventas y evitar costes innecesarios

## Índice de Contenidos 

-   [Contexto del reto en la industria](/docs/contexto_industria/README.md)
-   [Introducción a técnicas bayesianas cómo solución al reto](/docs/tecnicas_bayesianas/README.md)
-   [La inferencia bayesiana y la estimación de la incertidumbre](/docs/problematica_bayesiana_y_estimacion_incertidumbre.md) 
----
-   [Técnica: Exp.I - Estimacion de la varianza al vuelo](/docs/experimentos_labs/experimentos_q1/README.md)
-   [Técnica: Regresión Cuantílica](/poc_forecasting_uncertainty/techniques/quantile_regression/) 
-   [Técnica: Redes de densidad mixta](/docs/experimentos_labs/experimentos_q1/README.md#mdn)
-   [Técnica: DeepQuantile LSTM](/poc_forecasting_uncertainty/techniques/deepquantile_lstm/)
-   [Técnica: UMAL](/poc_forecasting_uncertainty/techniques/umal/)
-   [PoC Aplicación en Forecasting - Kaggle M5 Forecasting Uncertainty](/docs/forecasting_uncertainty/README.md) 
----
-   [Diagrama de aplicabilidad de las técnicas estudiadas](/docs/problematica_incertidumbre/README.md) [TODO]
-   [Proximos pasos](#prox_pasos)
-   [Documentos de referencia](#doc_ref)


## Otros Recursos

* [Experimentos Labs](/labs_experiments) *Experimentos realizados con datos de juguete para profundizar en las técnicas*
* [Presentacion Ejecutiva del Reto](https://docs.google.com/presentation/d/1mRkL54FNAwC0YNSKmbeWWg-IJNR2ch6oCLktIXDMjfc) 
* [Conceptos y preguntas clave](/core_questions/README.md)
* [Otros recursos](/resources/README.md)

## Contexto y alcance del reto

El **reto de la estimación de la incertidumbre tiene como objetivo** desarrollar técnicas de inteligencia artificial que, además de realizar su cometido, ofrezcan **una medida de fiabilidad de lo bueno que es su resultado**. Esta solución es de especial importancia de acuerdo a las directrices publicadas por comisión europea en 2018 de [Inteligencia Artificial Confiable](https://github.com/beeva/TEC_LAB-Trustworthy_AI) que responde a la necesidad de industria de construir IA segura con una visión 'human-centric' 

## Aproximación de la línea

En esta línea se hará foco en **la estadística bayesiana** cómo una solución técnica alternativa a otras técnicas de uso más extendido en en proyectos de ciencia de dato basadas en estadística frequentista. 

**La estadística bayesiana se selecciona tras** realizar un [estado del arte](https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit). y analizar el feedback recibido de universidades y otros expertos en IA de las técnicas utilizadas para la resolución de este reto. Marcando cómo principal objetivo de la línea ganar conocimiento en las límitaciones y ventajas de estas técnicas frente a las utilizadas actualmente en este contexto.

**Inicialmente se propone validar estas técnicas en el contexto de problemas de regresión** sobre datos sintéticos y de juguete para explotar sus capacidades en un entorno controlado. **Posteriormente, se propone llevarlo a un entorno de pruebas real** dentro de una problemática detectada de gran aplicabilidad como es **la problemática de forecasting** con el objetivo de explotar estas técnicas con datos reales y ofrecer una referencia de uso de las mismas.


## Recursos 

* [Video Lecture - Introduction to Bayesian data analysis - part 1: What is Bayes?](https://www.youtube.com/watch?v=3OJEae7Qb_o)
* [Video Discussion - Is bayesian the most brilliant thing ever?](https://www.youtube.com/watch?v=HumFmLu3CJ8)

