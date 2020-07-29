## Mixture Models
En está página se explica **los modelos de mixturas** como solución técnica para aproximar distribuciones heterogéneas de la variable respuesta. Este es el caso en el que sabemos que los datos u observaciones provienen de fuentes o procesos diferentes conocidos.


### Indice de contenidos
- [Introducción a la técnica](#introduccion)
- [Mixture Density Networks](#mdn)
- [MLE - Maximum Likelihood Estimation](#MLE) 

<a name="introduccion"></a>
## Introducción

Un **modelo de mixturas** es un modelo probabilístico que nos permite representar la presencia de sub-poblaciones de la población general. Esta representación de sub-poblaciones nos va a permitir construir un estimador más robusto en el caso en el que la distribución de la variable respuesta sea heterogénea


<a name="mdn"></a>
### Mixture Density Networks

Las **redes de densidad mixta** (Bishop, 1994) es un tipo de red que combina las redes convencionales con el concepto de modelo de mixturas. En este modelo, la sálida de la DNN hace la estimación de parámetros para la familia de distribuciones o componentes seleccionadas las cuales se suman teniendo en cuenta el coeficiente de mezcla ⍺ para obtener finalmente una distribucción condicional hetérogena de y respecto a la entrada: 

<p align="center"><img src="/docs/assets/mdn/MDN.png" height="160" alt=“Mixture Density Network” /></p>
<p align="center">Mixture Density Network</p>

Formalmente la probabilidad condicionada de una red de mixturas tiene la siguiente forma:

<p align="center"><img src="/docs/assets/mdn/mdn_formula.png" height="70" alt=“Formula MDN" /></p>
<p align="center">Mixture Density Network</p>

En esta fórmula los parámetros tiene la siguiente semántica:

* **c se corresponde con el índice de la correspondiente mixtura**. Hay hasta C componentes de mixtura (e.g. distribuciones) por salida, siendo un parametro seleccionable.
* **⍺ es el coeficiente de mezcla**. Para entender este coeficiente podemos imaginarnos los controles deslizantes que controlan la mezcla de C salidas diferentes de audio. Este parámetro esta condicionado por la entrada x.
* **𝒟 esta es la correspondiente distribución de entrada a ser mezclada**. La distribución puede ser elegida atendiendo al tipo de aplicación.
* **λ son los parámetros de la distribución 𝒟**. En el caso denotamos 𝒟 como una distribución gausiana, estos parametros corresponderian a λ1 sería la media condicional mean μ(x) y 
λ2 la desviación estándar σ(x). Las distribuciones pueden tener distinto número de parámetros (e.g.: Bernoulli and Chi2 tienen 1 parámetro, Beta tiene 2, y la gaussiana truncada tiene hasta 4 parámetros) Estos son parámetros que forman también la salida de la red.

<a name="MLE"></a>
### MLE - Maximum Likelihood Estimation

El algoritmo de MLE o máxima verosimilitud nos permite obtener los parámetros del modelo o distribución que maximizan la probabibilidad de obtener unos datos dados.

Referencia - [Ejemplo de cálculo de MLE para la implementación de la función de pérdida](https://d3c33hcgiwev3.cloudfront.net/_f678abd2f50f7171a76c7cb3ec03f726_MLE-for-Gaussian.pdf?Expires=1594252800&Signature=lDPX5Y6JT03mRyNj65JYEMZ7gjQuP5oXy-7019GmL8e8VuYRLo07K-N1iGU3geREMr1xj-VwjEh4qsV4R~PDQRpQuoH~UvEnrlpC3NyCzlgd1vcAKFQkppHqMXWsLDSg8HLu796cvDiu0R8bKy24ppHRdF4dta7sJCb3tvF8P8c_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)


### Aplicaciones

Entre las **aplicaciones más destacadas** se encuentra la de Apple’s Siri en iOS 11 para reconocimiento de voz[2]. En [3] se puede ver su aplicación en generación de manuscritos y Amazon Forecast lo tiene dentro su suite de algoritmos incluidos en su plataforma.

### Ventajas y desventajas

* *Ventajas* 

Permite estimar distribuciones heterogéneas de la variable respuesta

* *Desventajas* 

El tamaño de la sálida de la red creada por la capa final de la MDN es (c+2)* m, dónde c es la dimensión de sálida de la red convencional y m el número de mixturas que estamos usando. Esto supone un incremento considerable en la dimensión de sálida respecto a la red convencional lo que puede volverlas muy inestables.

#### Referencias

[1] https://towardsdatascience.com/a-hitchhikers-guide-to-mixture-density-networks-76b435826cca

[2] Siri Team, Deep Learning for Siri’s Voice: On-device Deep Mixture Density Networks for Hybrid Unit Selection Synthesis (2017)

[3] Alex Graves, Generating Sequences With Recurrent Neural Networks (2014)
