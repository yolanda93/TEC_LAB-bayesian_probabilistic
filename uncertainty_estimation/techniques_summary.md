## Listado de técnicas utilizadas

Para la estimación de la incertidumbre, tras un con técnicas más sencillas, se ha orientado el trabajo hacia la técnica de [UMAL](https://arxiv.org/abs/1910.12288), profundizando en las técnicas en las que se basa.


-   [Técnica: Exp.I - Estimacion de la varianza al vuelo](/docs/experimentos_labs/experimentos_q1/README.md)
    Esta técnica es muy simple de implementar y, aunque a servido para profundizar en el conocimiento, adolece de muchas delibidades que no la hace apta para su uso en producción.

-   [Técnica: Redes de densidad mixta](/docs/experimentos_labs/experimentos_q1/README.md#mdn)
    Son un tipo de redes que permiten utilizar redes neuronales convencionales con un modelo probabilístico que permite representar la presencia de sub-poblaciones dentro de la población general.   
 
-   [Técnica: Regresión Cuantílica](/poc_forecasting_uncertainty/techniques/quantile_regression/) 
    La técnica de regresión cuantílica permite obtener diferentes estimaciones para diferentes escenarios (cuantiles) dentro del mismo dataset. 
-   [Técnica: LSTM](/poc_forecasting_uncertainty/techniques/lstm/) [TODO]
    Las redes LSTM son una técnica de deep learning que permiten la predicción en series temporales.

-   [Técnica: DeepQuantile LSTM](/poc_forecasting_uncertainty/techniques/deepquantile_lstm/)
    Utilizando la regresión cuantílica, y utilizando los diferentes resultados como entrada de redes LSTM, podemos hacer estimaciones de serie de temporales en diferentes escenarios. 

-   [Técnica: Mixture Models](/poc_forecasting_uncertainty/techniques/mixture_models/)
    Los modelos de mixturas son una aproximación para poder trabajar con datos probenientes de diferentes fuentes y que pueden tener distribuciones heterogéneas de la variable respuesta.

-   [Técnica: UMAL](/poc_forecasting_uncertainty/techniques/umal/)
    La técnica UMAL (Uncountable Mixture Asymetric Laplacian) permite hacer predicciones en series temporales multimodales, sin tener conocimiento previo sobre las distribuciones de los datos ni de sus errores.


## Consideraciones previas de este curso de trabajo

* Asumimos un escenario con sufientes datos, por tanto:
  * Se puede tomar un modelo de Deep Learning tipo LSTM como baseline
  * Al contar con suficientes datos la incertidumbre por aproximación (underfitting) e incertidumbre epistémica se consideran despreciables y nos centramos en la aleatórica





