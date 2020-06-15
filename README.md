
# Estimación de la Incertidumbre 

El reto de estimación de la incertidumbre tiene como objetivo ofrecer una **medida de fiabilidad** sobre las predicciones de un modelo de Machine Learning o Deep Learning

Esto es importante para poder **cuantificar el margen de error cometido en las predicciones** de un modelo en escenarios con **alta incertidumbre**. 

Un ejemplo de este escenario lo podemos ver en [problemas de predicción de ventas de producto](/poc_forecasting_uncertainty) en los que se plantean cuestiones con alta incertidumbre como ¿Cuántos equipamentos de acampada vamos a vender el mes que viene? Ser capaces de dar una estimación de por ejemplo 50 equipamentos con un margen de error bajo (e.g. +-4) o alto (e.g. +-30) nos podría ayudar a optimizar mejor las campañas de ventas y evitar costes inecesarios

## Entregables

* [Experimentos Labs](/labs_experiments) *Experimentos realizados con datos de juguete para profundizar en las técnicas*
* [PoC: Forecasting de ventas de producto](/poc_forecasting_uncertainty) *Aplicación en una problemática real*
* [Libro de Aprendizajes](/docs/README.md) *Documentación sobre el conocimiento adquirido*
* [Presentacion Ejecutiva del Reto](https://docs.google.com/presentation/d/1mRkL54FNAwC0YNSKmbeWWg-IJNR2ch6oCLktIXDMjfc) 

## Contexto y alcance del reto

El **reto de la estimación de la incertidumbre tiene como objetivo** desarrollar técnicas de inteligencia artificial que, además de realizar su cometido, ofrezcan **una medida de fiabilidad de lo bueno que es su resultado**. Esta solución es de especial importancia de acuerdo a las directrices publicadas por comisión europea en 2018 de [Inteligencia Artificial Confiable](https://github.com/beeva/TEC_LAB-Trustworthy_AI) que responde a la necesidad de industria de construir IA segura con una visión 'human-centric' 

## Aproximación de la línea

En esta línea se hará foco en **la estadística bayesiana** cómo una solución técnica alternativa a otras técnicas de uso más extendido en en proyectos de ciencia de dato basadas en estadística frequentista. 

La estadística bayesiana se selecciona tras realizar un estado del arte y analizar el feedback recibido de universidades y otros expertos en IA de las técnicas utilizadas para la resolución de este reto. Marcando cómo principal objetivo de la línea ganar conocimiento en las límitaciones y ventajas de estas técnicas frente a las utilizadas actualmente en este contexto.

Inicialmente se propone validar estas técnicas en el **contexto de problemas de regresión** sobre datos sintéticos y de juguete para explotar sus capacidades en un entorno controlado. Posteriormente, se propone llevarlo a un entorno de pruebas real dentro de una problemática detectada de gran aplicabilidad como es **la problemática de forecasting** con el objetivo de explotar estas técnicas con datos reales y ofrecer una referencia de uso de las mismas.
