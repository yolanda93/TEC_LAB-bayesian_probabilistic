<h3 id="contexto">Contexto del reto en la industria</h3>

**El reto de estimación de la incertidumbre** se seleccionó con la intención de obtener conocimiento de técnicas de inteligencia artificial que, además de realizar su cometido, ofreciesen una medida de fiabilidad de lo bueno que era su resultado. Esta solución es de especial importancia de acuerdo a las directrices publicadas por comisión europea en 2018 de [Inteligencia Artificial Confiable](https://github.com/beeva/TEC_LAB-Trustworthy_AI) que responde a la necesidad de la industria en construir IA con una visión 'human-centric'

En particular, se ha visto que esta técnica **ofrece las siguientes ventajas en el desarrollo de un marco de inteligencia artificial confiable**:

* [**Interpretabilidad**](https://github.com/beeva/TEC_LAB-Trustworthy_AI/blob/master/pages/areas/transparencia.md): Ofrece una medida de incertidumbre y/o confianza que permita entender las variaciones en el comportamiento del modelo o cuantificar/acotar el riesgo de las predicciones

    -   **Precisión vs. Explicabilidad**: [Dentro de este reto](https://github.com/beeva/TEC_LAB-Trustworthy_AI/blob/master/pages/retos/precision-explicabilidad.md), es importante destacar, que en particular los modelos de deep learning, tiene la desventaja de ser *modelos de caja-negra*, es decir, las inferencias suelen ser más precisas pero a la vez también son más dificiles de explicar. Está técnica nos permite mejorar la explicabilidad de los modelos Deep Learning sin penalizar su rendimiento.

* [**Robustez**](https://github.com/beeva/TEC_LAB-Trustworthy_AI/blob/master/pages/areas/robustez.md): Mejorar la respuesta del modelo ante situaciones adversas. Esta técnica nos podría *filtrar predicciones con un nivel de incertidumbre alto o baja confianza*. Estos son los casos en los que no se tenga mucha confianza en las predicciones (e.g. se sospecha que el modelo está sobre-ajustado, sistemas con comportamientos variables, falta de datos o desconocimiento del problema a modelar).

* [**Ética y responsabilidad**](https://github.com/beeva/TEC_LAB-Trustworthy_AI/blob/master/pages/areas/sesgo.md): Al no ser posible cuantificar la incertdumbre o el grado de certeza de las inferencias de los modelos, se podrían *tomar decisiones automatizadas erroneas sin ser incluso capaces de cuantificar los daños*, en el caso de que no se comportará de la forma esperada. De esta manera, esta técnica, nos permitiría detectar estos casos y no realizar una toma de decisiones automatizada trasladando esta responsabilidad al humano. 
