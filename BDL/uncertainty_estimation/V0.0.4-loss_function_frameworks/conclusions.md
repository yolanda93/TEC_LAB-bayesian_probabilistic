### ¿Qué se ha hecho?
Se ha intentado implementar la técnica de estimación de varianza al vuelo Exp.1 utilizando Keras con TF como backend. 

### Conclusiones - Implementación en Keras 
No se ha encontrado una solución sencilla para actualizar/modificar la salida (target) sigma en la función de pérdida al vuelo. Creando una sesión en tensorflow sí es posible, pero es mucho más sencillo con la opción de requires_grad=False de PyTorch. Está opción evitar propagar la variable actualizada en el cómputo del gradiente.

Si creamos una sesión en tensorflow tenemos que compartir y modificar el valor de la salida y compartir ese valor entre iteraciones. Esta variable no puede ser diferenciable. En Pytorch se soluciona fácilmente con requires_grad=False
