
## UMAL (Uncountable Mixture Asymetric Laplacian)
En está página se explica la UMAL como **solución técnica para estimar la incertidumbre aleatórica heterocedastica**


### Indice de contenidos
- [Introducción a la técnica](#introduccion)
  - [Modelo UMAL](#modelo_umal)
- [Profundización teórica de UMAL](#how_tecnica)
  - [Relación con la regresión cuantílica](#rel_cuantil)
  - [Relación con las redes de densidad mixta](#rel_mdn)
 - [Aplicaciones](#aplicaciones)


<a name="introduccion"></a>
## Introducción a UMAL

**¿Qué es UMAL?**

**UMAL (Uncountable Mixture Asymetric Laplacian)** es una técnica bayesiana que sirve para estimar la incertidumbre aleatórica [heterocesdástica](#heterocesdástica) de las predicciones P(Y|X) *sin necesidad de conocimiento previo* de cómo se modela esta incertidumbre, es decir, permite obtener una distribucción de Y del tipo [heterogénea](#heterogénea) que se puede adaptar mejor a la distribucción real en *escenarios de alta incertidumbre*

**¿Qué problemática resuelve UMAL?**

Las técnicas convencionales de BDL para la modelización de la incertidumbre o generación de inferencias probabilísitcas **utilizan una fuerte asunción de priors** (e.g. dist.normal varianza de las predicciones) que **no permite estimar una distribución heterógenea de la variable Y, P(Y|X=x)** cómo se observa en la fig.1. (curva verde) y cuyas estimaciones se aproximan a la esperanza condicional E[Y|X = x] para un x dado (e.g. media de la distrbucción normal çomo se representa en amarillo en la fig.1)

<p align="center"><img src="/docs/assets/umal/umal_pdf.PNG" height="300" alt=“Figura1. UMAL - estimación de la pdf predictiva” /></p>
<p align="center"><em>UMAL - estimación de la pdf predictiva</em></p>

Este tipo asunciones hace que sea **dificil modelizar la inceridumbre aleatórica heterocedástica** de la cual es imposible adquirir conocimiento previo para la definición de estos priors o asunciones. Además, la modelización de la incertidumbre sin necesidad de conocimiento previo de cómo es esta incertidumbre **nos podría permitir realizar posteriormente un análisis más detallado y orientado a tarea** para poder entender las causas por las que se está dando esas variaciones en las estimaciones y aportarnos conocimiento o insights relevantes. 


**Profundización técnica en el tipo de problemática que resuelve UMAL**

En la figura.1 anterior se muestra un problema de regresión con unos datos sintéticos cuya distribucción de Y varia a lo largo del eje X por zonas. Estas zonas son generadas con distintos procesos generadores que modelan distintas distribucciones de probabilidad, en este caso de los tipos: asimétrica, simétrica, uniforme, multimodal. Estas variaciones a lo largo del eje X hace que el tipo de incertidumbre a modelar sea del tipo <a name="heterocesdástica"> *heterocedástica*, ya que la variabilidad de la Y en función de la X no se mantiene constante </a>. 

Además si nos fijamos en un input de X concreto, pongamos X1 = 0.6 vemos que <a name="heterogénea"> el tipo de distribucción de Y puede presentar varias modas, es decir, la varianza de la distribucción de Y es del tipo *heterogénea* </a>.

**¿Qué soluciones existen para estimar este tipo de incertidumbre?**

Para comprender la aplicación de UMAL respecto a otras técnicas bayesianas, es necesario compararlo con aunción de prior que realizan otras técnicas. Para esto nos ponemos  en 2 casos o soluciones hipóteticas

* **Solución 1 : Asunción restrictiva de prior - Utilizada por técnicas convencionales Bayesian Deep Learning**: Este es el caso en el que estimamos Y como *una esperanza condicional E[Y|X = x] asumiendo una distribucción normal de Y*, como sucede en la mayoría de las técnicas BDL. El resultado que obtendriamos utilizando este tipo de soluciones es que para la zona en la que la distribucción es simétrica; no nos alejaríamos mucho de la distribucción real de Y puesto que este tipo de distribucción está centrada en la media. Sin embargo, si nos vamos a otras regiones en el eje X, como por ejemplo, la que se muestra en el gráfico x=0.6, vemos que no vale con tomar una distribucción centrada en la media de Y (curva amarilla del gráfico) puesto que la varianza de la misma varía según el valor que esta tome, es decir, el tipo de distribucción es multimodal o *heterogénea*

* **Solución 2: Asunción menos restrictiva, agnóstica del tipo de distribucción de probabilidad - UMAL**: En UMAL utilizamos el concepto de regresión cuantílica que permite construir un estimador sin realizar fuertes asunciones del tipo de distribucción de Y. Esto permite estimar una distribucción heterogénea que como se ve en el gráfico (curva verde) al final se aproxima mejor a la distribucción real de Y. 

    Para ello, se hace una aproximación de esta distribucción usando una composición de distintas ALDs (Asymmetric Laplace Distribution) que realiza una discretización por partes de la distribucción real, es decir, hace una estimación por cuantil de la distribucción. (*Nota: La moda de la distribucción posterior de la función de probabilidad de la ALD se corresponde con el valor del estimador de la regresión cuantilica para un cuantil*)



<a name="modelo_umal"></a>
#### Modelo UMAL

El **modelo de UMAL (Uncountable Mixture Asymetric Laplacian)**, como se ha mencionado anteriormente, tiene cómo objetivo aproximar la densidad predictiva P(Y|X) de tipo heterogénea. (véase Figura 1). Para ello predice para cada input x los parámetros de la ALDs condicionadas seleccionadas (por la lista de quantiles que se introduce como entrada) de manera simultánea.
 
Este modelo se caracteriza por lo siguiente:
  * **entrada**: vector de entrada X ∈ Rn y una lista de quantiles τ  =  { 0.1, 0.2, … ,0.9}  (selección de ALDs)
  * **salida**: los parámetros de la ALDs condicionadas seleccionadas, y el cuantil τi :  {μ,  τ , σ }
  
<p align="center"><img src="/docs/assets/umal/umal_model.PNG" height="200" alt=“UMAL modelo” /></p>
<p align="center"><em>UMAL modelo</em></p>

Es importante destacar que UMAL *es agnóstico del modelo de Deep Learning que se utilice*, es decir, podría ser válido tanto para CNN; LSTM, etc.

<a name="implementacion"></a>
#### Ejemplos de Implementación 

* [Notebook 1 - Uncertainty Forecasting with UMAL](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/poc_forecasting_uncertainty/techniques/umal/umal_implementation.ipynb) *Implementación de UMAL con aplicación en medición de la incertidumbre en forecasting mediante la generación de una serie temporal sintética*


<a name="how_tecnica"></a>
## Profundización téorica de UMAL

En el siguiente gráfico se puede observar la técnica de UMAL en contraposición a otras técnicas de BDL vistas. En el gráfico se muestran unos datos sintéticos cuya distribucción de Y varia a lo largo del eje X por zonas, cada zona se podría identificar con distintos procesos generadores que dan lugar a una distribución heterogénea de P(Y|X). A la izquierda se ve una **representación de la aproximación de la distribucción de Y para un input dado x=0.6**. En este caso vemos como UMAL es capaz de capturar distribucciones heterogéneas que aproximan mejor a la distribucción real de Y que otras técnicas basadas en aproximar una distribucción normal (curva amarilla) 

<p align="center"><img src="/docs/assets/umal/umal_pdf.PNG" height="300" alt=“UMAL - estimación de la pdf predictiva” /></p>
<p align="center"><em>UMAL - estimación de la pdf predictiva</em></p>

La distribucción P(Y|X=x) es el resultado del algoritmo MAP (Maximum A posteriori Estimation) que selecciona aquel valor de parámetros de la distribucción que mejor explica la probabilidad de que den un conjunto de observaciones (Y), denominandose esta como Likelihood.


La formulación de una distribucción UMAL queda descrita por la siguiente figura. En esta formula, se describe **la función de densidad predictiva de un UMAL como el conjunto ponderado de N distribucciones asimétricas de laplace - ALDs**. Estas distribucciones se suman como resultado de la marginalización sobre el parámetro tau (o cuantíl) ya que se consideran independientes entre sí (véase MDN). 

<p align="center"><img src="/docs/assets/umal/umal_function.PNG" height="90" alt=“UMAL formulación” /></p>
<p align="center"><em>UMAL formulación</em></p>
  

<a name="rel_cuantil"></a>
### Relación con la regresión cuantílica

La estimación de la densidad posterior predictiva en [estadística bayesiana es intratable computacionalmente](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/docs/problematica_bayesiana/README.md) por ello es necesario un método de aproximación que nos permita aproximar esta CDF. La aproximación utilizada en UMAL utiliza la función de pérdida de la regresión cuantílica o Pinball Loss para aproximar N distribucciones del tipo ALD que se ajustan a distintos cuantíles  τ  =  { 0.1, 0.2, … ,0.9} o partes concretas de la distribucción de la predicción de Y para un input X dado.

Esta función de Pinball Loss, como se describió en el capítulo de regresión cuantílica, nos permite ajustar los pesos w y así estimar el valor de un cuantíl concreto τ de la distribucción P(Y|X) mediante la siguiente fórmula:

<p align="center"><img src="/docs/assets/umal/quantile_loss.PNG" height="60" alt=“Quantile/Pinball Loss - formulación” /></p>
<p align="center"><em>Quantile/Pinball Loss - formulación</em></p>

Sin embargo, esta función de pérdida sólo nos ofrece el parámetro de ubicación (location parameter) o la moda de la distribucción ALD. Para estimar la distribucción de ALD necesitamos obtener la varianza  (μ,  τ , **σ** ) cómo se observa en la formulación de la distribucción:


<p align="center"><img src="/docs/assets/umal/ALD_distribution.PNG" height="70" alt=“ALDs distribución - formulación” /></p>
<p align="center"><em>ALDs distribución - formulación</em></p>


De esta manera se modifica la función de pérdida o Pinball Loss definida anteriormente se modifica para la estimación de los parámetros de la ALD  (μ,  τ , **σ** ). Esto se consigue maximizando el log-likelihood:

<p align="center"><img src="/docs/assets/umal/MLE_ALD.PNG" height="70" alt=“Maximización del log-likelihood de la función ALD - formulación” /></p>
<p align="center"><em>Maximización del log-likelihood de la función ALD  - formulación</em></p>

Finalmente la función de pérdida de UMAL para obtener el ajuste de los pesos w que maximizen de forma conjunta los parámetros de la ALD quedaría de la siguiente manera:

<p align="center"><img src="/docs/assets/umal/ald_loss.PNG" height="70" alt=“ALDs parameter estimation - formulación” /></p>
<p align="center"><em>Función de pérdida UMAL - formulación</em></p>



<a name="rel_mdn"></a>
### Relación con las mixturas de componentes

Para estimar una **distribución heterógenea de la variable Y** es necesario ajustar N familias de distribucciones utilizando lo que se conoce como mixturas de componentes. En el caso de UMAL la familia de distribucciones a ajustar es la distrbucciones asimétricas de laplace. Este metodo está descrito en [detalle aqui](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/poc_forecasting_uncertainty/techniques/mixture_models) y se cálcula mediante la siguiente fórmula:

<p align="center"><img src="/docs/assets/umal/mdn_function.PNG" height="80" alt=“MDN - formulación” /></p>
<p align="center"><em>MDN - formulación</em></p>

Con el método anterior (véase Relación la regresión cuantílica) tendríamos la estimación de parámetros de la ALD. El método UMAL estima la distribucción posterior o predicitva como la suma ponderada de los pesos para cada ALDs. El número de ALDs a estimar viene determinado por la lista de quantiles τ  =  { 0.1, 0.2, … ,0.9} que es un parámetro de entrada de la red. A mayor número de quantiles, mayor es la aproximación a la distribucción real de Y. 


<p align="center"><img src="/docs/assets/umal/rel_tecnicas_umal.PNG" height="340" alt=“MDN UMAL - representación gráfica” /></p>
<p align="center"><em>MDN UMAL - representación gráfica</em></p>



<a name="aplicaciones"></a>
## Aplicaciones

**Algunos ejemplos de aplicaciones** dónde podría tener sentido esta técnica son: *la evaluación del riesgo in aplicaciones financieras, predicción de demanda/mobilidad para la optimización de sistemas de transporte o predicción del consumo energético*. 

**Todas estas problemáticas comparten un componente aleatórico heterocedastico dificil de modelar** que proporciona información muy relevante para el negocio. Para la evaluación de riesgo financiero nos daría predicciones mucho más robustas, en el caso de optimización de sistemas de transporte nos podría ofrecer información relevante para estimar la probabilidad de accidentes o congestiones de tráfico y en el caso de consumo energético nos podría servir para anticipar posibles picos de consumo.
