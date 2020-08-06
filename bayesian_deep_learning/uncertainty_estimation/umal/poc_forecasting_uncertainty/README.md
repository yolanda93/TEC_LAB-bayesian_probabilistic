
# Estimación de la incertidumbre en Forecasting 

El problema de forecasting realiza inferencias a futuro utilizando datos del pasado. Se podría considerar un caso particular de regresión en el que las variables están ordenadas en el tiempo. Se ha detectado especial aplicabilidad de las técnicas probabilísitcas debido a la **gran incertidumbre presente al realizar inferencias a futuro**.  

Está necesidad se ha detectado tras realizar un research en la industria y en BBVA Next Technologies. En concreto, se tiene como referencia la competición [M5 Forecasting Uncertainty de Kaggle](https://www.kaggle.com/c/m5-forecasting-uncertainty) en la que se pretende aplicar las técnicas estudiadas en este contexto

## Forecasting de ventas de productos - M5 Forecasting Uncertainty de Kaggle 

La competición M5 Forecasting Uncertainty de Kaggle es un reto propuesto por la cadena de supermercados Wallmart que trata de predecir las **ventas de productos** en varias localización para un **periodo de tiempo de 28 dias**. Las tiendas se encunentran en los estados de California, Texas, y Wisconsin.

### Aproximación del problema

El desarollo de este proyecto se realizará siguiendo la ejecución normal de un proyecto de ciencia de datos con los siguientes pasos:

1. **Exploratorio de datos** *Formulación de Hipótesis y Exploratorio de datos* 
2. **Limipieza de datos** *Transformaciones para la limpieza de datos*
2. **Transformación de datos** *Procesamiento y transformación de datos necesarias, feature engineering*
3. **Modelado de la solución** *Aplicación de soluciones técnicas*

### Objetivos y alcance

Los **objetivos** a alcanzar en el contexto de este trabajo son:

1. **Aplicación y validación** de técnicas de estimación de la incertidumbre en una problemática real
   - **Validar el conocimiento extraído en Experiments Labs**
2. Validación de la **solución técnica UMAL** para resolver este tipo de problemática
3. Obtener conocimiento sobre **técnicas adyacentes** con aplicación en **Forecasting** (e.g. LSTM, regresión cuantílica)


#### Hipótesis Iniciales 

- **H1 - Las técnicas bayesianas del tipo BDL o UMAL nos dan el mejor estimador de incertidumbre en este reto**

   - Se probara la técnica UMAL y luego técnicas más sencillas de BDL (MonteCarlo Dropout, etc) 

- [**H2 - El mejor estimador de la incertidumbre también nos dará la mejor predicción**](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/labs_experiments)
  
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
 
### Indice de contenidos
- [Dataset](#dataset_description)
  - [Ficheros del dataset](#dataset_files)
- [Exploracion inicial](#initial_exploration)


<a name="dataset_description"></a>
## Descripción del dataset

We are working with 42,840 hierarchical time series. The data were obtained in the **3 US states** of California (CA), Texas (TX), and Wisconsin (WI). **Hierarchical** here means that data can be aggregated on different levels: item level, department level, product category level, and state level. The sales information reaches back **from Jan 2011 to June 2016**. In addition to the sales numbers, we are also given corresponding data on **prices, promotions, and holidays**. Note, that we have been warned that **most of the time series contain zero values**

<a name="dataset_files"></a>
### Dataset files

#### Training data
- *sales_train_validation.csv* - Contains the historical daily **unit sales** data per product and store [d_1 - d_1913].
    - Date range: [2011-01-29 - 2016-05-22] 
    - Fields: IDs, department, category, store, and state 
- *sell_prices.csv* - Contains information about the **price of the products** sold per store and date. It is a weekly average
    - Fields: store_id, item_id, wm_yr_wk (the id of the week), sell_price (provided per week (average across seven days), if not available the product was not sold during this week) 
- *calendar.csv* - Contains **the dates** on which products are sold. The dates are in a yyyy/dd/mm format.
    - Fields: day-of-the week, month, year, and an 3 binary flags of [SNAP food stamps](https://www.benefits.gov/benefit/361)

#### Validation data
 - *sales_train_evaluation.csv* - Available one month before the competition deadline. It will include sales for [d_1 - d_1941]. It includes the validation period of 28 days until 2016-06-19

#### Submission file
- *submission.csv* - Demonstrates the correct format for submission to the competition. The prediction of 28 forecast days (F1-F28)

<a name="initial_exploration"></a>
### Notebook: Exploracion inicial

1. [Exploración de los datos por distintos niveles (12 niveles)](https://www.kaggle.com/headsortails/back-to-predict-the-future-interactive-m5-eda#header)

- **El día de Navidad** es el único día en el que todas las tiendas están cerradas. Las ventas de los productos es 0.
- **Dias SNAP**
- El dataset presenta estacionalidad anual, mensual y semanal. La estacionalidad semanal es parecida para los 3 estados en la mensual hay variaciones.


