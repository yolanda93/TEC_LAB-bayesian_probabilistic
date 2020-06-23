El problema de la inferencia Bayesiana

La inferencia bayesiana puede convertirse en un problema intratable o con una complejidad computacional muy alta dependiendo de las **asunciones tomadas por el modelo y la dimensionalidad**

En la práctica 

En este sentido se han desarrollado técnicas que permiten aproximar su resultado:

- **Sampling-based**: MCMC Markov Chain Monte Carlo. Las cadenas de Markov de Monte Carlo es un método númerico de aproximación que tiene como objetivo aproximar una distribución de probabilidad determinada. La idea del algoritmo es simular una cadena de Markov cuya distribución estacionaria se aproxime a la distribución a posteriori del modelo, de esta forma somos capaces de obtener una aproximación de la distribucción. Destacan 2 métodos:
	- Metropolis-Hasting 
	- Gibbs Sampling
	
- **Aproximation-based**: Variatonal Inference (VI). Este algoritmo aproxima la distribución a posteriori a través de funciones de distribución más sencillas, de esta forma transforma el problema a uno de optimización donde buscamos minimizar la diferencia entre la función a posteriori y la aproximación. Esta diferencia se mide a través de la divergencia de Kullback-Leibler.
