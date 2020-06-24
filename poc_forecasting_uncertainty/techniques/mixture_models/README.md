## Mixture Models
En está página se explica **los modelos de mixturas** como solución técnica para aproximar distribuciones heterogéneas de la variable respuesta. Este es el caso en el que sabemos que los datos u observaciones provienen de fuentes o procesos diferentes conocidos.


### Indice de contenidos
- [Introducción a la técnica](#introduccion)
  - [MLE - Maximum Likelihood Estimation](#MLE)
- [Mixture Density Networks](#mdn)

<a name="introduccion"></a>
## Introducción

Un **modelo de mixturas** es un modelo probabilístico que nos permite representar la presencia de sub-poblaciones de la población general. Esta representación de sub-poblaciones nos va a permitir construir un estimador más robusto en el caso en el que la distribución de la variable respuesta sea heterogénea


<a name="MLE"></a>
### MLE - Maximum Likelihood Estimation

El algoritmo de MLE o máxima verosimilitud nos permite obtener los parámetros del modelo o distribución que maximizan la probabibilidad de obtener unos datos dados.


<a name="mdn"></a>
### Mixture Density Networks

Las **redes de densidad mixta** (Bishop, 1994) es un tipo de red que combina las redes convencionales con la concepto de modelo de mixturas.

Entre las **aplicaciones más destacadas** se encuentra la de Apple’s Siri en iOS 11 para reconocimiento de voz[2]. En [3] se puede ver su aplicación en generación de manuscritos y Amazon Forecast lo tiene dentro su suite de algoritmos incluidos en su plataforma.


<p align="center"><img src="/docs/assets/mdn/MDN.png" height="50" alt=“Mixture Density Network” /></p>
<p align="center">Mixture Density Network</p>

Formalmente la probabilidad condicionada de una red de mixturas tiene la siguiente forma:

<p align="center"><img src="/docs/assets/mdn/mdn_formula.png" height="50" alt=“Mixture Density Network” /></p>
<p align="center">Mixture Density Network</p>

En esta fórmula los parámetros tiene la siguiente semántica:

* **c se corresponde con el índice de la correspondiente mixtura**. Hay hasta C componentes de mixtura (e.g. distribuciones) por salida, siendo un parametro seleccionable.
* **⍺ es el coeficiente de mezcla**. Para entender este coeficiente podemos imaginarnos los controles deslizantes que controlan la mezcla de C salidas diferentes de audio. Este parámetro esta condicionado por la entrada x.
* **𝒟 esta es la correspondiente distribución de entrada a ser mezclada**. La distribución puede ser elegida atendiendo al tipo de aplicación.
* **λ son los parámetros de la distribución 𝒟**. En el caso denotamos 𝒟 como una distribución gausiana, estos parametros corresponderian a λ1 sería la media condicional mean μ(x) y 
λ2 la desviación estándar σ(x). Las distribuciones pueden tener distinto número de parámetros (e.g.: Bernoulli and Chi2 tienen 1 parámetro, Beta tiene 2, y la gaussiana truncada tiene hasta 4 parámetros) Estos son parámetros que forman también la salida de la red.



#### Referencias

[1] https://towardsdatascience.com/a-hitchhikers-guide-to-mixture-density-networks-76b435826cca

[2] Siri Team, Deep Learning for Siri’s Voice: On-device Deep Mixture Density Networks for Hybrid Unit Selection Synthesis (2017)

[3] Alex Graves, Generating Sequences With Recurrent Neural Networks (2014)
