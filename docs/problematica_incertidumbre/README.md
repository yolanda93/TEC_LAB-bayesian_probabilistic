<h2 id="conceptos_clave">Profundización en las problemáticas de estimación de la incertidumbre</h2>

La estimación de la incertidumbre presenta distintas dificultades asociadas que dependen principalmente de 2 factores clave:

- [Conocimiento del problema y asunciones realizadas por el modelo de IA](#asunciones)
- [Tipo de incertidumbre a modelar inherente a la problemática y conocimiento de la misma](#tipo_incertidumbre)

<h3 id="asunciones">Conocimiento del problema y asunciones realizadas por el modelo de IA</h3> 

En la modelización de la incertidumbre es importante diferenciar aquellas problemáticas en las que se conoce el tipo de incertidumbre inherente y cómo se podría modelar esta incertidumbre de las que se desconoce por completo la manera de modelizar la incertidumbre de la respuesta o inferencia del modelo.

Teniendo en cuenta esta problemática, en el caso de desconocer esta incertidumbre nos podríamos encontrar con las siguientes dificultades técnicas, ordenadas de menor a mayor dificultad técnica y conocimiento del problema:

1- **Errores de aproximación**: Estos errores se obtienen cuando el modelo de ML es demasiado sencillo para modelar la complejidad de los datos. En el contexto de este reto, las técnicas utilizadas se centraran en técnicas de deep learning por su aplicación cómo aproximadores universales.

2- **Presencia de incertidumbre epistémica**: Esta sería el caso en el que nos encontramos con unos datos que no representan completamente el problema a modelar. También está relacionado con la correcta calibración del modelo. *Esto es importante en datasets pequeños y dispersos y en aplicaciones críticas*

3- **Presencia de incertidumbre aleatorica**: Este es el tipo de incertidumbre más díficil de modelar, ya que no es posible reducirla aunque conozcas la distribución de la variable respuesta o manera de modelizar el problema. Es un error irreducible que se da en casi cualquier problemática real cuando los datos tienen una variabilidad asociada intrínseca que no se ajusta al error esperado. *Importante en aplicaciones en tiempo real con mucho ruído., e.g. stock market*


<h3 id="tipo_incertidumbre">Tipo de incertidumbre a modelar inherente a la problemática y conocimiento de la misma</h3> 


* **Incertidumbre Homocedastica**: Todas las muestras tienen el mismo error de medición. Es decir, la varianza de este error se mantiene más o menos constante u homogénera
* **Incertidumbre Heterocedastica**: Las muestras tienen diferentes errores de medición (no todas son igual de fiables). En este caso el valor de la varianza de las predicciones varía a lo largo del tiempo.



