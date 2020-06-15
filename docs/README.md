En esta carpeta se encuentra la documentación con **los aprendizajes extraídos de la soluciones técnicas estudiadas** en el contexto del reto de estimación de la incertidumbre


## Índice de Contenidos 

-   [Contexto del reto en la industria](/docs/contexto_industria/README.md)
-   [Introducción a técnicas bayesianas cómo solución al reto](/docs/tecnicas_bayesianas/README.md)
-   [Profundización en las problemáticas de estimación de la incertidumbre](/docs/problematica_incertidumbre/README.md)
----
-   [Experimentos de Laboratorio - Profundización en las técnicas](/docs/experimentos_labs/README.md)
-   [Aplicación en la problemática de Forecasting](/docs/forecasting_uncertainty/README.md)
----
-   [Proximos pasos](#prox_pasos)
-   [Documentos de referencia](#doc_ref)


<h2 id="prox">Proximos pasos </h2>

*Monte Carlo Dropout*
  
Respecto a la clasificación con BDL, se revisó el [experimento que utilizaba Montecarlo dropout](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V4.3.0-traffic_lights), pero no se pudo profundizar suficiente para entender su comportamiento. Tras realizar una revisión del estado del arte se vió que este método estaba ampliamente aceptado en la comunidad científica y se utilizaba como baseline en distintos benchmarks.

*Metodología y/o Framework de Validación*

El enfoque de validación de estos experimentos ha ido guiado por la generación de datos sintéticos para modelizar distintos escenarios. Dentro de este metodología se ha visto que para comprobar la robustez del modelo es importante validar en casos extremos cambiando el proceso de generación de datos para que se ajuste a distintas distribuciones. Revisando posteriormente el estado del arte se vió que en muchas publicaciones cientificas utilizaban la generación de ejemplos adversarios en un espacio de N-dimensiones como generador de banco de pruebas.

*Aplicaciones*

Dentro de otras aplicaciones interesantes que podría ofrecer esta técnica se han destacado las siguientes relacionadas con la exploración de otras formas de entrenamiento de los modelos:
- Active Learning
- Continual Learning

<h2 id="doc_ref">Documentos de referencia </h2>

- **Estado del Arte**:
https://docs.google.com/document/d/10TrBLqnkROiWhTFf8V6cTIQBr30Wjjw8J2j4fZkMMAk/edit

- **Sprint [27 de Nov - 11 de Dec] 2019**
https://docs.google.com/document/d/1bp_Rl6-gARMsEufxQt622elKwv38dIKmtIs2tWVcrOc/edit#heading=h.et9co8t7x85v

- **Sprint 4Q7S - 2019 - Validación de métodos de estimación con incertidumbre**
https://docs.google.com/document/d/1DkcUwaWw3lTW_1ylt3POmfGURaD08xCuaUBYcRnc_5U/edit

- **Sprint 1Q2S - 2020 - Estimación de la Incertidumbre - Validación - Scoring**
https://docs.google.com/document/d/110_gQ9yhVaELgoZJfjLxlWeL_D8YyORFrRyxF1da4UM/edit
