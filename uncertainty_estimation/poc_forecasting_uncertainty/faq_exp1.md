
# Hipótesis/cuestiones resueltas 

## Cuestiones correspondientes a experimentos del Q3

### Q1: ¿Qué limitaciones tiene la técnica Exp.I Varianza al vuelo? 

- **Capacidad de modelizar la incertidumbre**: Este tipo de distribucción no permite modelar incertidumbre heterogénea o heterocedastica por punto de estimación. La distribución del error de la P(Y|X=x), es decir, distribución de Y para una xi dada, se aproxima a una distribución gaussiana. 
- **Capacidad de generalización**: La fuerte asunción de priors podría generar problemas de overfitting. Al final es una técnica que tiene limitaciones de generalización. Esto no debería ser un problema si conoces bien la problemática y sabes que la problemática se ajusta a las asunciones o priors de esta técnica. Este tipo de problemas se da en cualquier modelo ML/Deep Learning y es necesario un conjunto de datos representativo o conocimiento de la problemática para poder evaluarla*.

*Nota: Consideramos como parte de los priors la arquitectura y parámetros de la red*

### Q2: ¿Dónde tendría sentido aplicar la técnica Exp.I varianza al vuelo?  [Core Question]

**Conocimiento del problema**
  - En aquellos problemas en los que tengamos cierta certeza de que la distribución del error de la P(Y|x) se puede aproximar usando una distribución gausiana
  - Se tenga suficiente conocimiento del problema o modelizar la incertidumbre de manera 'muy aproximada o detallada' no interese

**Ejemplo de aplicación**
  - Robótica e IoT: Aprox. la incertidumbre con una dist.normal podría evitar inestabilidades en sistema complejos.
  A veces no interesa modelizar 'en su completitud' la incertidumbre de las estimaciones que utilizan como fuente de datos sensores calibrados puesto que se sabe que este error se podría aproximar con una distribucción gaussiana, además tampoco interesa recoger picos de la distribucción ya que podrían dar lugar a inestabilidades en el propio sistema. (e.g. estimaciones que se van a pasar como input a un controlador PID)

