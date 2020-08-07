# Métodos Bayesianos y Programación Probabilística

## Introducción (TODO)
* ¿Qué es?
La **estadística bayesiana** es un subconjunto del campo de la estadística en la que la evidencia sobre el verdadero estado del mundo se expresa **en términos de grados de creencia, es decir, trata la modelización de la incertidumbre**
* ¿Por qué es interesante?

Con este enfoque podemos estimar la 'probabilidad de que una hipótesis sea cierta' (incertidumbre de la hipótesis), que llevado al campo de Machine Learning nos permite representar un modelo ML como el conjunto de asunciones o hipótesis que realiza y la probabilidad de que esas asunciones se acerquen a la realidad.

Sin embargo, esta incertidumbre actualmente no se modela ya que **los modelos de ML se basan más en estadística frecuentista** que a diferencia de la bayesiana realiza inferencias sin expresar esta incertidumbre al respecto, evaluando las hipótesis en términos absolutos usando las evidencias disponibles y de acuerdo a unos ciertos umbrales de aceptación de tal hipótesis (p-values, CI, etc)

Cómo resultado de aplicar este enfoque podríamos obtener la distribución (posterior) de los parámetros del modelo y no sólo puntos de estimación como se puede observar en la siguiente fórmula:

---

## Teorema de Bayes

La formulación matemática del enfoque bayesiano utiliza [el teorema de bayes](https://es.wikipedia.org/wiki/Teorema_de_Bayes), descrito mediante la siguiente fórmula:

![](img/formula_bayes.png)

En la fórmula matemática anterior podemos ver un ejemplo de cómo calcular estas probabilidades, usando el teorema de bayes. Este teorema por definición trata de calcular las probabilidades subjetivas que puede tomar un determinado suceso cuando hemos recibido algún tipo de información previa. Para ello, se calcula la probabilidad a posteriori P(A|B), en base a las probabilidades a priori o P(A) y la probabilidad de que se dé el suceso B si la hipótesis A es cierta, P(B|A). [1]


---


Actualmente se están utilizando multitud de técnicas para obtención de indicadores y métricas dentro de las tecnologías de la información, que van desde estadística básica hasta técnicas de aprendizaje automático. Así, se obtienen unos valores que aportan una información que ayuda en las estimaciones y toma de decisiones. No obstante, la naturaleza de gran parte de los datos y, sobre todo, de gran parte de las métricas que se quieren obtener es probabilística. 

Las técnicas más tradicionales, orientadas desde el punto de vista frecuentista, nos permiten obtener medidas descriptivas de los datos, tales como la mediai, la moda o la varianza de los datos. Sin embargo, obteniendo estos datos como descriptivos, podemos estar cayendo en una serie de asunciones de las que no somos conscientes: si asumimos que una media y una varianza describen nuestros datos, seguramente sea porque estamos suponiendo que nuestros datos siguen una distribución normal, o gausiana.

Es decir, estamos haciendo unas suposiciones a priori sobre nuestros datos, lo que nos lleva a unos resultados a posteriori sobre ellos. Pero podemos cambiar esas asuciones por otras cualesquiera, y el modelo estadístico que permite trabajar con esta serie de asunciones es la estadística bayesiana [METER ENLACE].

Una vez entramos en este enfoque, podemos ir mas allá. Un modelo de red neuronal se puede determinar como, dados unos priors, como son la arquitectura y los datos de entrada, obtenemos a posteriori unos pesos para la neuronas.[REVISAR]

Así, la inferencia bayesiana abre los límites de las aproximaciones frecuentistas y propociona un campo más amplio de trabajo, donde no sólo obtenemos unos resultados, si no que obtenemos información asociada a esos resultados.

Con esta idea en mente, se han realizado una serie de trabajos orientados a obtener predicciones y la incertidumbre asociada a estas predicciones. De este modo, quienes interpreten los resultados no sólo obtendrán un valor, si no también una métrica que informe acerca de lo preciso, válido o importante que sea este valor, dependiendo de cómo se haya aplicado la métrica.

Estos trabajos parten de la determinación del grado de confianza en un resultado mediante técnicas más comunes y específicas hasta la utilización de una técnica avanzanda generalista utilizando redes neuronales.

### Aplicaciones de la inferencia bayesiana

Una de las grandes aplicaciones de la estadística bayesiana es la [estimación de la incertidumbre](bayesian_deep_learning/uncertainty_estimation). Se ha realizado un amplio trabajo en este área, realizandose un estudio del problema, técnicas existentes y formas de abordarlo.  


### El problema de la inferencia Bayesiana

La inferencia bayesiana puede convertirse en un problema intratable o con una complejidad computacional muy alta dependiendo de las **asunciones tomadas por el modelo y la dimensionalidad**. Por ello todas las técnicas se basan en métodos de aproximación basandose en el conocimiento del problema para la modelización del prior o mediante la aproximación de la distribución a posteriori

En este sentido se han estudiado técnicas que permiten aproximar su resultado:

- **Sampling-based**: MCMC Markov Chain Monte Carlo. Las cadenas de Markov de Monte Carlo es un método númerico de aproximación que tiene como objetivo aproximar una distribución de probabilidad determinada. La idea del algoritmo es simular una cadena de Markov cuya distribución estacionaria se aproxime a la distribución a posteriori del modelo, de esta forma somos capaces de obtener una aproximación de la distribucción. Destacan 2 métodos:
	- Metropolis-Hasting 
	- Gibbs Sampling
	
- **Aproximation-based**: Variatonal Inference (VI). Este algoritmo aproxima la distribución a posteriori a través de funciones de distribución más sencillas, de esta forma transforma el problema a uno de optimización donde buscamos minimizar la diferencia entre la función a posteriori y la aproximación. Esta diferencia se mide a través de la divergencia de Kullback-Leibler.


## Trabajo realizado
* [Bayesian Deep Learning](bayesian_deep_learning)
  * [Estimación de la incertidumbre](bayesian_deep_learning/uncertainty_estimation)
* Redes Bayesianas
* Procesos Gausianos
* Causalidad
  * [Recursos en Google Drive](https://drive.google.com/drive/folders/1uefX12ZtAieVE3SVsTqI94E8s5wXOs07)
  * [Modelos de Ecuaciones Estructurales](https://github.com/beeva/TEC_LAB-structural_equation_modeling)
  * [Causalidad "vs" Machine Learning](https://github.com/beeva/TEC_LAB-causality_vs_machine_learning)
* Herramientas y librerías
  * [Pyro](https://github.com/next-samuelmunoz/bayprob) (Pytorch library)
  * [Árboles de decisión bayesianos](https://github.com/beeva/TEC_LAB-bayesian_decision_trees)
* Comunicación
  * [Bayesianos, viendo la inteligencia artificial desde otro prisma](https://www.bbvanexttechnologies.com/bayesianos-viendo-la-inteligencia-artificial-desde-otro-prisma/) - BBVA Next Technologies Blog
  
  
  
## Referencias
* Introduction to Bayesian data analysis - Youtube
  * [Part 1: What is Bayes?](https://www.youtube.com/watch?v=3OJEae7Qb_o)
  * [Part 2: Why use Bayes?](https://www.youtube.com/watch?v=mAUwjSo5TJE)
  * [Part 3: How to do Bayes?](https://www.youtube.com/watch?v=Ie-6H_r7I5A)
* [Is bayesian the most brilliant thing ever?](https://www.youtube.com/watch?v=HumFmLu3CJ8) - Youtube, NIPS 2016
* [Bayesian probability theory](http://users.ics.aalto.fi/harri/thesis/valpola_thesis/node12.html) - Polytechnica scandinavica

