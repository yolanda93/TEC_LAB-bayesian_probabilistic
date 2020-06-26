



## Introducción a UMAL

Las técnicas convencionales de BDL para la modelización de la incertidumbre o generación de inferencias probabilísitcas **utilizan una fuerte asunción de priors** (e.g. dist.normal varianza de las predicciones) que no permite estimar una distribución heterógenea de la variable Y y cuyas estimaciones se aproximan a la esperanza condicional E[Y|X = x] para un x dado. 

Este tipo asunciones hace que sea **imposible modelizar la inceridumbre aleatórica heterocedastica** de la cual es imposible adquirir conocimiento previo para la definición de estos priors o asunciones. Además, la modelización de la incertidumbre sin necesidad de conocimiento previo de cómo es esta incertidumbre **nos podría permitir realizar posteriormente un análisis más detallado y orientado a tarea** para poder entender las causas por las que se está dando esas variaciones en las estimaciones. 


#### Modelo UMAL

El **modelo de UMAL (Uncountable Mixture Asymetric Laplacian)** tiene cómo objetivo aproximar la densidad predictiva P(Y|X) de tipo heterogénea. (véase Figura 1). Para ello predice para cada input x los parámetros de la ALDs condicionadas seleccionadas (por la lista de quantiles que se introduce como entrada) de manera simultánea.
 
Este modelo se caracteriza por lo siguiente:
  * **entrada**: vector de entrada X ∈ Rn y una lista de quantiles τ (selección de ALDs)
  * **salida**: los parámetros de la ALDs condicionadas seleccionadas, y el cuantil τi 
  


Es importante destacar que UMAL *es agnóstico del modelo de Deep Learning que se utilice*, es decir, podría ser válido tanto para CNN; LSTM, etc.


## Profundización en la técnica


### Relación con la regresión cuantílica

### Relación con las redes de densidad mixta

En el gráfico 


Density estimation involves selecting a probability distribution function and the parameters of that distribution that best explains the joint probability distribution of the observed data (X).

## Aplicaciones

**Algunos ejemplos de aplicaciones** dónde podría tener sentido esta técnica son: *la evaluación del riesgo in aplicaciones financieras, predicción de demanda/mobilidad para la optimización de sistemas de transporte o predicción del consumo energético*. 

**Todas estas problemáticas comparten un componente aleatórico heterocedastico dificil de modelar** que proporciona información muy relevante para el negocio. Para la evaluación de riesgo financiero nos daría predicciones mucho más robustas, en el caso de optimización de sistemas de transporte nos podría ofrecer información relevante para estimar la probabilidad de accidentes o congestiones de tráfico y en el caso de consumo energético nos podría servir para anticipar posibles picos de consumo.


