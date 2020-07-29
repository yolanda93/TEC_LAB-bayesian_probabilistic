
## La inferencia bayesiana y la estimación de la incertidumbre

La estimación de la incertidumbre y la inferencia bayesiana[METER ENLACE] son dos conceptos separados que, para los propósitos de este reto, de utilizan de forma conjunta, utilizando la inferencia bayesiana para realizar la estimación de la incertidumbre. 

### El problema de la estimación de la incertidumbre
<h3 id="conceptos_clave">Profundización en las problemáticas de estimación de la incertidumbre</h3>

La estimación de la incertidumbre presenta distintas dificultades asociadas que dependen principalmente de 2 factores clave:

- [Conocimiento del problema y asunciones realizadas por el modelo de IA](#asunciones)
- [Variabilidad de la incertidumbre a modelar](#var_incertidumbre)

<h4 id="asunciones">Conocimiento del problema y asunciones realizadas por el modelo de IA</h4> 

En la modelización de la incertidumbre es importante diferenciar aquellas problemáticas en las que se conoce el tipo de incertidumbre inherente y cómo se podría modelar esta incertidumbre de las que se desconoce por completo la manera de modelizar la incertidumbre de la respuesta o inferencia del modelo.

Teniendo en cuenta esta problemática, en el caso de desconocer esta incertidumbre nos podríamos encontrar con las siguientes dificultades técnicas, ordenadas de menor a mayor complejidad:

1- **Incertidumbre de aproximación**: Estos errores se obtienen cuando el modelo de ML es demasiado sencillo para modelar la complejidad de los datos o el problema, es decir, **se desconoce la complejidad real del problema a modelar**. 

En el contexto de este reto, las técnicas utilizadas se centraran en técnicas de deep learning por su aplicación cómo aproximadores universales. Sin embargo, se podría dar el caso en el que se posee suficiente conocimiento de la problemática a modelar y está no presenta una complejidad elevada. En este caso, podría ser suficiente con modelos de ML clásicos como árboles de decisión y técnicas de cross-validation para modelizar la incertidumbre.

2- **Presencia de incertidumbre epistémica**: Esta sería el caso en el que los datos no representan completamente el problema a modelar y no es posible obtener más datos o **se desconocen estas variables más representativas para modelar el problema**. *Esto es importante en datasets pequeños y dispersos y en aplicaciones críticas*

3- **Presencia de incertidumbre aleatorica**: Este es el tipo de incertidumbre más díficil de modelar, ya que **no es posible reducirla** aunque conozcas la distribución de la variable respuesta o manera de modelizar el problema. Es un error irreducible que se da en casi cualquier problemática real por **la imposibilidad de conocer exáctamente todas y cada una de las variables que afectan a nuestro sistema**. Todos los datos presentan una variabilidad asociada intrínseca que no se ajusta al error esperado. *Importante en aplicaciones en tiempo real con mucho ruído., e.g. stock market*

<h4 id="var_incertidumbre">Variabilidad de la incertidumbre a modelar</h4> 

Este caso trataría el caso en el que la incertidumbre a modelar (conocida o no) presente una gran variabilidad que haga que la distribución de la variable respuesta no se pueda aproximar con una distribución normal. Es decir, nos encontremos con distribucciones con colas largas, presencia de outliers o anomalías, distintas modas, volatilidad o variabilidad temporal, etc.

De acuerdo con esta definición, se pueden diferenciar, a su vez y en conjunto con las anteriores, los siguientes casos:

1- **Presencia de incertidumbre homocedastica**: Todas las muestras tienen el mismo error de medición. Es decir, la varianza de este error se mantiene más o menos constante u homogénea

2- **Presencia de incertidumbre heterocedastica**: Las muestras tienen diferentes errores de medición (no todas son igual de fiables). En este caso el valor de la varianza de las predicciones varía a lo largo del tiempo.


## La inferencia bayesiana y la estimación de la incertidumbre

La estimación de la incertidumbre y la inferencia bayesiana[METER ENLACE] son dos conceptos separados que, para los propósitos de este reto, de utilizan de forma conjunta, utilizando la inferencia bayesiana para realizar la estimación de la incertidumbre. 
