## Dataset Boston

- **descripción del dataset**
El dataset seleccionado es el de precios de viviendas de Boston. Este dataset está disponible en la librería de scikit-learn. Se ha elegido este dataset por la calidad del dato, amplio uso, sencillez y validez para probar las hipótesis planteadas anteriormente. 

Como podemos ver en los gráficos presenta ruido heteroscedastico y sigue una distribución normal

- **pruebas de heteroscedasticidad**:
Usando un dataset real (precios de las casas de Boston) se ha visto que el método del Exp.I da buenos resultados en pruebas de heteroscedasticidad. Si bien es cierto que las varianzas están ‘suavizadas’, es decir, no obtenemos valores muy extremos para observaciones con desviación típica alta. Se ha validado que este método nos podría servir perfectamente para descartar aquellas predicciones no válidas. (Faltaría probar sobre un problema de clasificación y no sólo regresión). Se comprueba que el dataset presenta error heteroscedastico utilizando tests de Levene.

