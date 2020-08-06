# Estimación de la Incertidumbre 

Dentro del aporte de valor que pueden realizar las técnicas bayesianas, está la estimacion de la incertidumbre.

El reto de la estimación de la incertidumbre tiene como objetivo ofrecer una **medida de fiabilidad** sobre las predicciones de un modelo de Machine Learning o Deep Learning.

Esto es importante para poder **cuantificar el margen de error cometido en las predicciones** de un modelo en escenarios con **alta incertidumbre**. 

Un ejemplo de este escenario lo podemos ver en [problemas de predicción de ventas de producto](poc_forecasting_uncertainty) en los que se plantean cuestiones con alta incertidumbre como ¿Cuántos equipamentos de acampada vamos a vender el mes que viene? Ser capaces de dar una estimación de por ejemplo 50 equipamentos con un margen de error bajo (e.g. +-4) o alto (e.g. +-30) nos podría ayudar a optimizar mejor las campañas de ventas y evitar costes innecesarios

## Contexto y alcance del reto

El **reto de la estimación de la incertidumbre tiene como objetivo** desarrollar técnicas de inteligencia artificial que, además de realizar su cometido, ofrezcan **una medida de fiabilidad de lo bueno que es su resultado**. Esta solución es de especial importancia de acuerdo a las directrices publicadas por comisión europea en 2018 de [Inteligencia Artificial Confiable](https://github.com/beeva/TEC_LAB-Trustworthy_AI) que responde a la necesidad de industria de construir IA segura con una visión 'human-centric' 

## Aproximación de la línea

En esta línea se hará foco en **la estadística bayesiana** cómo una solución técnica alternativa a otras técnicas de uso más extendido en en proyectos de ciencia de dato basadas en estadística frequentista. 

**La estadística bayesiana se selecciona tras** realizar un [estado del arte](https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit). y analizar el feedback recibido de universidades y otros expertos en IA de las técnicas utilizadas para la resolución de este reto. Marcando cómo principal objetivo de la línea ganar conocimiento en las límitaciones y ventajas de estas técnicas frente a las utilizadas actualmente en este contexto.

**Inicialmente se propone validar estas técnicas en el contexto de problemas de regresión** sobre datos sintéticos y datasets pequeños para explotar sus capacidades en un entorno controlado. **Posteriormente, se propone llevarlo a un entorno de pruebas real** dentro de una problemática detectada de gran aplicabilidad como es **la problemática de forecasting** con el objetivo de explotar estas técnicas con datos reales y ofrecer una referencia de uso de las mismas.

## Indice de contenidos

* [Contexto del reto en la industria](industry_uncertainty_estimation.md)
* [Profundización en la problemática de estimación de la incertidumbre](uncertainty_estimation_problem.md)
* [Validación y métricas de estimación de la incertidumbre](uncertainty_validation_metrics.md)
* [Listado de técnicas exploradas](#listado-tecnicas-exploradas)
* [Proximos pasos](uncertainty_estimation_next_steps.md)


## Listado de técnicas exploradas

Para la estimación de la incertidumbre, tras un comienzo con técnicas más sencillas, se ha orientado el trabajo hacia la técnica de [UMAL](https://arxiv.org/abs/1910.12288), profundizando en las técnicas en las que se basa.


-   [Técnica: Exp.I - Estimacion de la varianza al vuelo](experiment_On_the_fly/README.md)
    Esta técnica es muy simple de implementar y, aunque a servido para profundizar en el conocimiento, adolece de muchas delibidades que no la hace apta para su uso en producción

 
-   [Técnica: Regresión Cuantílica](quantile_regression/README.md) 
    La técnica de regresión cuantílica permite obtener diferentes estimaciones para diferentes escenarios (cuantiles) dentro del mismo dataset 
-   [Técnica: LSTM](LSTM/README.md) [TODO]
    Las redes LSTM son una técnica de deep learning que permiten la predicción en series temporales

-   [Técnica: DeepQuantile LSTM](deepquantile_lstm/README.md)
    Utilizando la regresión cuantílica, y utilizando los diferentes resultados como entrada de redes LSTM, podemos hacer estimaciones de serie de temporales en diferentes escenarios

-   [Técnica: Redes de densidad mixta](mixture_density_networks/README.md)
    Son un tipo de redes que permiten utilizar redes neuronales convencionales con un modelo probabilístico que permite representar la presencia de sub-poblaciones dentro de la población general 

-   [Técnica: UMAL](umal/README.md)
    La técnica UMAL (Uncountable Mixture Asymetric Laplacian) permite hacer predicciones en series temporales multimodales, sin tener conocimiento previo sobre las distribuciones de los datos ni de sus errores



## Referencias

* PPT Ejecutiva - [Estimación de la incertidumbre](https://docs.google.com/presentation/d/1mRkL54FNAwC0YNSKmbeWWg-IJNR2ch6oCLktIXDMjfc)


