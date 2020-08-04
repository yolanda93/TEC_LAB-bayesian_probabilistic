
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
