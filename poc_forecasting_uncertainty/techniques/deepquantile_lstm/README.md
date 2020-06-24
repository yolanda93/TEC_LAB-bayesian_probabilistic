Deep Quantile LSTM

**Implementación**
------

Pasos de implementación:

(1) DQR  → (1a) DQR Nquantiles → (2) DQ+LSTM → (3) MultiOutput DQ+LSTM → (4) UMAL ¿?

*Paso 1 - Deep Quantile Regression*
-----
Pasamos de estar aproximando la media condicionada de y a aproximar un cuantil (parte concreta de la distribucción)

* fi(x) = y con MSE →  fi(x) = y con Pinball Loss

*Resultado*:
- Tenemos un estimador capaz de predecir cualquier cuantil de la distribucción de la variable respuesta
- Esto también nos da un intervalo de predicción. Por ejemplo, estimando los cuantiles 2.5% y 97.5% tenemos el intervalo de prediccion 95%. 

Hipotesis: ¿ Cómo conseguimos con esto tener una medida robusta que se aproxime a la distribucción real de la variable respuesta sin imposición de asunciones ? No queremos la relación aprox. a media entre las variables inpependientes y dependientes. Queremos saber todas las relaciones posibles. Cual es la relación en el caso de la mediana, el peor de los casos, el mejor, etc..

Solución: 1a --> Vamos a construir N estimadores para ajustarnos a N quantiles --> Podríamos verlo como discretizar un problema que sería intratable de forma continua

**Paso 1a - Solución Naive -  Ajuste independiente de N cuantiles**
Fixed quantile bins τ0, …, τN

Estimación de N cuantiles ajustando un modelo independiente para cada quantile

*Desventajas*:
 * Implica ajustar N funciones diferentes 
 * Violación de el principio básico de que los cuantiles no se pueden cruzar


*Paso 2 Deep Quantile Regression --> DQ + LSTM (Forecasting)*
-----
Pasamos de un problema de regresión a forecasting

* fi(x) = y con Pinball Loss →  fi(xi) = xi+1 

¿Cómo es esa X de la LSTM? Trabajamos con ventanas de tiempo fijas de 2 time steps y horizonte de 1 time steps. La resolución temporal la fijamos a una 1 hora.

Resultado:
- Tenemos un estimador que nos permite hacer inferencias a futuro con incertidumbre

Dudas:
- Habría que ver cómo afecta los cuantiles a la seleccion de la ventana temporal. Axel no le da importancia, yo si.
- No tengo muy claro como de sensible es a outliers en el tiempo... ¿Cuánto crecería la incertidumbre por el efecto de outliers? 
- LSTM con relaciones temporales y espaciales

*Paso 3 - Solución Multi-Output - Predicción Conjunta de N cuantiles*
-----

 --> No queremos cuantiles cruzados
Estimamos de forma conjunta la media condicionada y N cuantiles en un sólo modelo

Ventajas:
 * Nos permite resolver el problema de cuantiles cruzados

*Paso 4 - Solución Implicit Quantile*
-----
*¿Qué queremos?*
Aprendemos N_tau o n quantiles. Antes pasabamos una lista de N *fijos* y ahora los aprendemos de forma implicita en la red.

*¿Cómo lo implemento?*
Sampleamos Q (o tau) de una distribucción uniforme (Aproximación MC de la distribución real). 

UMAL lo que hace es extender las idea de mixture model, aprendiendo implicitamente un numero finito de ALD (N quantiles) para aproximar la distribucción de la variable respuesta

2 modos --> training y testing. Es necesario crearse una clase en Keras para esto, ya que el batch size va a cambiar.

*Training*
La entrada del modelo en training X y N_taus (X es la serie temporal, N_taus nos delimita el numero de cuantiles)

*Testing*
Le pasamos X (batch temporal) y lista de Q e.g. [0.1,0.3,...,0.4]


--- Más detalles de implementación

- Importante! la concatenación del cuantil con las features (batch temporal de la serie) . Esto es más por Keras ya que no se puede meter más de 2 argumentos en la función de perdida

- Vamos a tener deficiencias del estilo voy a coger el batch size y me lo voy a replicar para cada cuantil. No veo muy eficiente trabajar con este tensor. ¿No se podría hacer esto mejor? 


Nota:
Ya veremos a ver cuando pasemos a un problema real lo eficiente que es esto....


Duda: Lo ideal sería que me diera sólo los cuantiles más informativos, es decir, eliminar aquellos cuantiles redundantes o que no proporcionaran información. ¿No se podría filtrar calculando su entropía?


**Hipótesis**
------
Mejora del rendimiento del modelo
H1: Adding quantiles to the overall loss function adds relevant information about the target domain and can induce a regularization effect

**Desventajas**
------
Cuantiles cruzados

   

   
**Referencias**
------
Rodrigues, F., & Pereira, F. C. (2020). Beyond Expectation: Deep Joint Mean and Quantile Regression for Spatiotemporal Problems. IEEE Transactions on Neural Networks and Learning Systems, 1–13. https://doi.org/10.1109/tnnls.2020.2966745

Brando, A., Rodríguez-Serrano, J. A., Vitrià, J., & Rubio, A. (2019). Modelling heterogeneous distributions with an Uncountable Mixture of Asymmetric Laplacians. (NeurIPS 2019). Retrieved from http://arxiv.org/abs/1910.12288
