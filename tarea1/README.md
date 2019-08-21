# Tarea 1

<Introduccion>

## Elementos mínimos

### 0. Implementar redes neuronales

Para esta tarea se realizo una implementación nueva de redes neuronales, parte del código se baso en el código provisto por el profesor.

La estructura que sigue esta implementación es la siguiente:

<Altoque Bodoque>

### 1. Escoger el dataset

Para este trabajo se escoge el dataset ["iris"](https://archive.ics.uci.edu/ml/datasets/Iris), el cual se descarga y se maneja en forma local.

Para manejar este dataset se importa en forma de `numpy.ndarray`. El método que realiza esta conversión se le llama `import_data`, recibe el *path* del archivo.

Además se tiene el método `split_set` que separa un `numpy.ndarry` en el porcentaje que se le dé. Si recibe solo un número (entre 0 y 1) separa el arreglo en dos arreglos, uno con el porcentaje dado y otro con el restante. Puede recibir dos porcentajes, en este caso, mientras la suma sea menor que 1, separa el set en dos arreglos que contienen los dichos porcentajes. Este método se usará para separar el dataset en *train set* y *test set*.

**Código**: [`code/neural_network/utils/set_functions.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network/utils/set_functions.py)

**Test unitario**: [`tests/test_neural_network/test_set_functions.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network/test_set_functions.py)

### 2. Implementar normalización

La normalización fue implementada en una clase hija de la clase `NeuralNetwork` original (seccion: **Implementar redes neuronales**), llamada `NormalizedNetwork`. Esto, por dos motivos. El primero, para mantener una versión de `NeuralNetwork` sin normalización y aplicar buenas prácticas de programación orientada a objetos. El segundo, para presentar la normalización en una nueva clase que no considere la implementación de la red neuronal.

**Código**: [`code/neural_network/normalized_network.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network/normalized_network.py)

**Test unitario**: [`tests/test_neural_network/test_normalize.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network/test_normalize.py)

### 3.  Implementar la transformación one-hot

La transformación se definió como el método `one_hot_encoding` que recibe una lista o un `array ` y devuelve una tupla de dos elementos, el primero, la entrada como una versión codificada como `one-hot vector` (como lista si recibe una lista o como `numpy.ndarray` en el segundo caso) . El segundo elemento es el diccionario de codificación de la forma `key`: elemento original y `value`: `one-hot vector`.

**Código**: [`code/neural_network/utils/one_hot_encoding.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network/utils/one_hot_encoding.py)

**Test unitario**: [`tests/test_neural_network/test_one_hot_encoding.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network/test_one_hot_encoding.py)

### 4. Producir la matriz de confusión para representar el resultado del test del modelo



## Bonuses

### k-Fold Cross-Validation

### Segundo dataset

### Variación de las neuronas de la capa escondida

