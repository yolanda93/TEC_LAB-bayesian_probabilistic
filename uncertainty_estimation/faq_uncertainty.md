
### Q4: ¿Qué tipo de incertidumbre estamos intentando modelar cuando hacemos experimentos con obs. que se alejan en eje X en función de la Y de los datos de entrenamiento? 

Incertidumbre epistémica: Es un error reducible que se está dando por falta de datos en un intervalo

*Nota: El resultado de este experimento fue que obteniamos una varianza proporcional al alejamiento en el eje X*

### Q5: ¿Cómo se podría probar la incertidumbre aleatorica heterocedástica? 

Para probar la incertidumbre aleatórica es necesario introducir error en la sálida de la red (predicciones de la red) en datos de testing. Este error no puede ser igual al error conocido, es decir, en nuestro caso el prior es una distribución normal y potencialmente distinto de la distribucción del error real de los datos de entrenamiento.
La incertidumbre heterocedástica es aquel error que puede provenir de distintas fuentes. Por tanto, necesitamos N procesos distintos generadores de ese ruido aleatórico.

### Q6: ¿Cómo podríamos modelar una incertidumbre conocida e.g. dist.laplace, exponencial?

Solución Naive:
Cambiando la función de pérdida de la red para optimizar los valores de los parámetros de la distribución conocida.
Para el cálculo de la función que máximiza el valor de los parámetros para un conjunto de datos se utiliza el algoritmo de MLE (Maximum Likelihood Estimation)


