## Estimación de la incertidumbre en Forecasting 

Este experimento realiza un recorrido por todas las técnicas explicadas anteriormente y la aplica sobre un dataset donde otras personas ya están aplicando otras técnicas, con el objetivo de detectar si supone una mejora.

El problema de forecasting realiza inferencias a futuro utilizando datos del pasado. Se podría considerar un caso particular de regresión en el que las variables están ordenadas en el tiempo. Se ha detectado especial aplicabilidad de las técnicas probabilísitcas debido a la **gran incertidumbre presente al realizar inferencias a futuro**.  

Está necesidad se ha detectado tras realizar un research en la industria y en BBVA Next Technologies. En concreto, se tiene como referencia la competición [M5 Forecasting Uncertainty de Kaggle](https://www.kaggle.com/c/m5-forecasting-uncertainty) en la que se pretende aplicar las técnicas estudiadas en este contexto

### Indice de contenidos

[PoC: Predicción de incertidumbre en ventas de producto](experiments/m5_forecasting_uncertainty)
* [Exploratorio de datos](experiments/m5_forecasting_uncertainty/dataset_exploration/) *Formulación de Hipótesis y Exploratorio de datos* 
* [Limipieza de datos](experiments/m5_forecasting_uncertainty/dataset_cleaning/) *Transformaciones para la limpieza de datos*
* [Transformación de datos](experiments/m5_forecasting_uncertainty/dataset_tranformation/) *Procesamiento y transformación de datos necesarias, feature engineering*
* [Modelado de la solución](experiments/m5_forecasting_uncertainty/ml_solutions/) *Aplicación de soluciones técnicas*
* [MVP](experiments/m5_forecasting_uncertainty/mvp_final_solution/) *Despliegue y documentatión de la solución final*

Técnicas de estimación de la incertidumbre en forecasting
 * [Regresión Cuantílica](../quantile_regression/) 
 * [LSTM](../LSTM/)
 * [DeepQuantile LSTM](../deepquantile_lstm/)
 * [Mixture Models](../mixture_density_networks/)
 * [UMAL](../umal/)

### Objetivos

Los **objetivos** a alcanzar en el contexto de este trabajo son:

1. **Aplicación y validación** de técnicas de estimación de la incertidumbre en una problemática real
   - **Validar el conocimiento extraído en Experiments Labs**
2. Validación de la **solución técnica UMAL** para resolver este tipo de problemática
3. Obtener conocimiento sobre **técnicas adyacentes** con aplicación en **Forecasting** (e.g. LSTM, regresión cuantílica)


#### Hipótesis Iniciales 

- **H1 - Las técnicas bayesianas del tipo BDL o UMAL nos dan el mejor estimador de incertidumbre en este reto**

   - Se probara la técnica UMAL y luego técnicas más sencillas de BDL (MonteCarlo Dropout, etc) 

- **H2 - El mejor estimador de la incertidumbre también nos dará la mejor predicción**
  
   - La competición se desarrolla en 2 partes, cada una con un método de validación diferente



#### Definición del ámbito del problema


- Evaluación de la incertidumbre
   - Se utiliza la función Pinball Loss adaptada a forecasting
   - Se piden los quantiles de la mediana 50%, 67%, 95%, y 99%
   - Todos los niveles jerarquicos (12) son igualmente ponderados
   - Quantiles son igualmente ponderados en la evaluación
   - Duda: we expect from the best performing forecasting methods to derive lower forecasting errors for the series that are more valuable for the company
 
 - El dataset incluye demanda esporádica o nulos (afectados por festivos, días SNAP, etc)
 - Inclusión de datasets externos (e.g. desastres naturales de incendios en Texas)
      
