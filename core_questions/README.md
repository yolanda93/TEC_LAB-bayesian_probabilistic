
## Hipótesis/cuestiones resueltas 

### Q1: ¿Qué limitaciones tiene la técnica Exp.I Varianza al vuelo? 

- **Capacidad de modelizar la incertidumbre**: Este tipo de distribucción no permite modelar incertidumbre heterogénea o heterocedastica por punto de estimación. La distribución del error de la P(Y|X=x), es decir, distribución de Y para una xi dada, se aproxima a una distribución gaussiana. 
- **Capacidad de generalización**: La fuerte asunción de priors podría generar problemas de overfitting. Al final es una técnica que tiene limitaciones de generalización. Esto no debería ser un problema si conoces bien la problemática y sabes que la problemática se ajusta a las asunciones o priors de esta técnica. Este tipo de problemas se da en cualquier modelo ML/Deep Learning y es necesario un conjunto de datos representativo o conocimiento de la problemática para poder evaluarla*.

*Nota: Consideramos como parte de los priors la arquitectura y parámetros de la red*

### Q2: ¿Dónde tendría sentido aplicar la técnica Exp.I varianza al vuelo? 

**Conocimiento del problema**
  - En aquellos problemas en los que tengamos cierta certeza de que la distribución del error de la P(Y|x) se puede aproximar usando una distribución gausiana
  - Se tenga suficiente conocimiento del problema o modelizar la incertidumbre de manera 'muy aproximada o detallada' no interese

**Ejemplo de aplicación**
  - Robótica e IoT: Aprox. la incertidumbre con una dist.normal podría evitar inestabilidades en sistema complejos.
  A veces no interesa modelizar 'en su completitud' la incertidumbre de las estimaciones que utilizan como fuente de datos sensores calibrados puesto que se sabe que este error se podría aproximar con una distribucción gaussiana, además tampoco interesa recoger picos de la distribucción ya que podrían dar lugar a inestabilidades en el propio sistema. (e.g. estimaciones que se van a pasar como input a un controlador PID)

### Q3: ¿Dónde tendría sentido aplicar la técnica UMAL?

**Conocimiento del problema**
 - Problemas en los que (se sospecha) que no se dispone o va a disponer de información relevante de la problemática o conjunto de variables que modelizan esa problemática. Es decir, tenemos un alto grado de incertidumbre.
 [En problemas de forecasting siempre se va a dar esta problemática y va ser dependiente del horizonte de tiempo de predicción](#https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/poc_forecasting_uncertainty/techniques/quantile_regression#por-que-utilizar-intervalos-de-predicci%C3%B3n-o-cuantiles-en-forecasting) 

**Aplicación**
 - Mejora de la robustez en aplicaciones en tiempo real
 - Nos interesa ser capacaces de modelizar esa incertidumbre porque nos proporciona información core para el negocio (e.g. riesgo financiero)

### Q4: ¿Qué tipo de incertidumbre estamos intentando modelar cuando hacemos experimentos con estimaciones que se alejan en eje X en función de la Y de los datos de entrenamiento?

Incertidumbre epistémica: Es un error reducible que se está dando por falta de datos en un intervalo

### Q5: ¿Cómo se podría probar la incertidumbre aleatorica heterocedástica?

Para probar la incertidumbre aleatórica es necesario introducir error en la sálida de la red (predicciones de la red) en datos de testing. Este error no puede ser igual al error conocido, es decir, en nuestro caso el prior es una distribución normal y potencialmente distinto de la distribucción del error real de los datos de entrenamiento.
La incertidumbre heterocedástica es aquel error que puede provenir de distintas fuentes. Por tanto, necesitamos N procesos distintos generadores de ese ruido aleatórico.

### Q6: ¿Cómo podríamos modelar una incertidumbre conocida e.g. dist.laplace, exponencial?

Solución Naive:
Cambiando la función de pérdida de la red para optimizar los valores de los parámetros de la distribución conocida.
Para el cálculo de la función que máximiza el valor de los parámetros para un conjunto de datos se utiliza el algoritmo de MLE (Maximum Likelihood Estimation)

## Próximas preguntas


### ¿Qué es UMAL - idea clave?
### ¿Es posible estimar la distribución posterior de forma exacta?
### ¿Por qué es importante UMAL? ¿Qué tipo de problemas estamos resolviendo con UMAL?
### ¿Cuales son las técnicas principales de UMAL?
### ¿Qué papel juega la regresión cuantílica en UMAL? ¿Y las MDN?


## Cuestiones e Hipótesis clave sin resolver
