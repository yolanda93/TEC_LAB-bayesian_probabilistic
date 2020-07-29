
# Aprendizajes de experimentos MDN

-   [Técnica: Redes de densidad mixta](#mdn)
    -   [Motivación](#mdn_motivacion)
    -   [Experimentos y conclusiones](#mdn_exp-conclusiones)


<h2 id="mdn">Redes de densidad mixta </h2>

<h3 id="mdn_motivacion"> Motivación</h3>

Además de estudiar los métodos expuestos anteriormente, se exploraron las [redes de densidad mixta (MDN)](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/BDL/uncertainty_estimation/V3.0.0-mixture_density_networks), [aplicándolas también al dataset inmobiliario](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/BDL/uncertainty_estimation/V0.1.6-real_datasets/uncertainty_prediction_house_prices_mdn.ipynb). Se decidió estudiar está técnica, además de por las limitaciones expuestas anteriormente, por el trabajo realizado por Axel Brando de BBVA Data y expuesto en la conferencia anual de IA Factory.

<h3 id="mdn_exp-conclusiones">Experimentos y conclusiones</h3>
   
Este método en contraposición con lo validado en el Exp.I de estimación de incertidumbre al vuelo presentan las siguientes ventajas que se pueden resumir a mayor libertad en la definición del prior:

 - Permite modelar facilmente que el ruido provenga de distintas familias de distribucciones 
 - Pueden modelar ruido multimodal, es decir, que no sólo provenga de una sola distribución si no de la suma de varias distribucciones de la misma familia con distintos parámetros. Este prior, sin embargo, también esta implicito en el exp.I y no es fácilmente modificable.
 - Tienen más soporte, es decir, el método está más comunmente aceptado. 
