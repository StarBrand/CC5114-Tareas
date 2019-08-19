# Tarea 1

<Introduccion>

## Elementos mínimos

### 0. Implementar redes neuronales

Para esta tarea se realizo una implementación nueva de redes neuronales, parte del código se baso en el código provisto por el profesor.

La estructura que sigue esta implementación es la siguiente:

<Altoque Bodoque>

### 1. Escoger el dataset

### 2. Implementar normalización

### 3.  Implementar la transformación one-hot

La transformación se definió como el método `one_hot_encoding` que recibe una lista o un `array ` y devuelve la entrada con una versión codificada como un `one-hot vector` (como lista si recibe una lista o como `numpy.ndarray` en el segundo caso).

Código: [`code/neural_network/utils/one_hot_encoding.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network/utils/one_hot_encoding.py)

Test unitario: [`tests/test_neural_network/test_one_hot_encoding.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network/test_one_hot_encoding.py)

### 4. Producir la matriz de confusión para representar el resultado del test del modelo

## Bonuses

### k-Fold Cross-Validation

### Segundo dataset

### Variación de las neuronas de la capa escondida

