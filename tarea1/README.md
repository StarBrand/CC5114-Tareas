# Tarea 1

En este reporte se explicará el procesos de implementación, testeo y resultado de la implementación de neuronas y redes neuronales siguiendo el orden lógico por el que se fueron desarrollando. Al final de cada sección se da la ubicación del código fuente en el repositorio y los *scripts* de los test unitarios.

## Neuronas

### Perceptrón

Siguiendo el orden del curso, primero se implementó la clase [`GatePerceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/perceptron/gate_perceptron.py) (anteriormente `Perceptron`) que solo recibe una entrada de dos argumentos y devuelve un booleano. Sobre este primer perceptrón se implementan los operadores lógicos *and*, *or*, *nand* y *sum*, fijando los pesos a conveniencia.

Abstrayendo este perceptrón se implementa [`Perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/perceptron/perceptron.py) que recibe, en su contructor, el número de argumentos de entrada. Como función de activación utiliza *step*. Utilizando este perceptrón, se realiza *refactoring* sobre `GatePerceptron` y se vuelven a correr los tests unitarios para comprobar que sigue funcionando.

![perceptrons](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea1/UML/perceptron.png)

**Código**: [`code/perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/perceptron)

**Tests unitarios**: [`tests/test_perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_perceptron)

### *Learning Perceptron*

Pasados los tests, se implementa la clase [`LearningPerceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/learning_perceptron/gate_perceptron.py) que aplica el algoritmo básico de aprendizaje visto en clase. Además de realizar los test unitarios se realizó un proceso de aprendizaje sobre una línea generada al azar. Los resultados se muestran en la siguiente sección y los métodos utilizados se encuentran reportados en la sección: **Anexo/Patrones** y **Anexo/Visualización**

![learning_perceptron](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea1/UML/learning_perceptron.png)

**Código**: [`code/learning_perceptron/learning`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/learning_perceptron/learning.py)

**Tests unitarios**: [`tests/test_learning_perceptron/test_learning_perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_learning_perceptron/test_learning_perceptron.py)

#### Resultados

Se muestran tres imágenes sobre el aprendizaje del perceptrón: sin entrenamiento, a las 10 y 100 *epochs*.

![training](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/example_perceptron.png)

Ejecutable [`tares1/scripts/show_learning_perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/show_learning_perceptron.py)

Gráfico de *accuracy* sobre las etapas del entrenamiento para varias tasas de aprendizaje (*learning rate*).

![lrs](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/perceptron_different_lr.png)

Ejecutable [`tares1/scripts/learning_perceptron_lrs`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/learning_perceptron_lrs.py)

### Neurona sigmoidea

Como se revisó en clases, el perceptrón utiliza como función de activación la función *step*. Esta función cambia abruptamente a pequeños cambios en los pesos. Por ello, una neurona que permite cambios más precisos es la función sigmoid. Una neurona con esta función de activación se implementó como un perceptrón (`SigmoidPerceptron`) dentro de la clase `SigmoidNeuron` que modifica algunos métodos de  `LearningPerceptron`.

![sigmoid_neuron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/sigmoid_neuron.png)

No se muestran resultados por extensión.

**Código**: [code/learning_perceptron/sigmoid_perceptron](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/learning_perceptron/sigmoid_perceptron.py)

**Tests unitario**: [tests/test_learning_perceptron/test_sigmoid_neuron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_learning_perceptron/test_sigmoid_neuron.py)

### Neurona

Finalmente, para completar los requisitos de la neurona que se pide, se implementa la clase `Neuron` que recibe una función de activación distinta. Las funciones de activación se encuentran implementadas en [`utils/math_functions/activation_functions`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/utils/math_functions/activation_functions.py) (reportado más abajo)

![neuron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/neuron.png)

**Código**: [`code/learning_perceptron/neuron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/learning_perceptron/neuron.py)

**Tests unitario**: [`tests/test_learning_perceptron/test_neuron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_learning_perceptron/test_neuron.py)

#### Resultados

A continuación se muestra como esta neurona con función de activación *tanh* (por ser la única no implementada previamente). Se ve como es capaz de aprender una línea, pero no las dos líneas (se requiere una red para ello).

![training_neuron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/example_neuron.png)

Ejecutable: [`tarea1/scripts/show_neuron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/show_neuron.py)

Para mostrar la diferencia con la red implementada, más abajo, se muestra una neurona sigmoidea aprende el dataset iris (se utilizan las funciones de testeo que se reportan más abajo).

![neuron_on_iris](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/neuron_on_iris.png)

Ejecutable: [`tarea1/scripts/neuron_on_iris`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/neuron_on_iris.py)

## Funciones de activación y métodos para pre-procesamiento

### Escoger el dataset

Para este trabajo se escoge el dataset ["iris"](https://archive.ics.uci.edu/ml/datasets/Iris), el cual se descarga y se maneja en forma local.

Para manejar este dataset se importa en forma de `numpy.ndarray`. El método que realiza esta conversión se le llama `import_data`, recibe el *path* del archivo.

Además se tiene el método `split_set` que separa un `numpy.ndarry` en el porcentaje que se le dé. Si recibe solo un número (entre 0 y 1) separa el arreglo en dos arreglos, uno con el porcentaje dado y otro con el restante. Puede recibir dos porcentajes, en este caso, mientras la suma sea menor que 1, separa el set en dos arreglos que contienen los dichos porcentajes. Este método se usará para separar el dataset en *train set* y *test set*.

**Código**: [`code/neural_network/utils/set_functions.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network/utils/set_functions.py)

**Test unitario**: [`tests/test_neural_network/test_set_functions.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network/test_set_functions.py)

###  Implementar la transformación one-hot

La transformación se definió como el método `one_hot_encoding` que recibe una lista o un `array ` y devuelve una tupla de dos elementos, el primero, la entrada como una versión codificada como `one-hot vector` (como lista si recibe una lista o como `numpy.ndarray` en el segundo caso) . El segundo elemento es el diccionario de codificación de la forma `key`: elemento original y `value`: `one-hot vector`.

**Código**: [`code/neural_network/utils/one_hot_encoding.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network/utils/one_hot_encoding.py)

**Test unitario**: [`tests/test_neural_network/test_one_hot_encoding.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network/test_one_hot_encoding.py)

### Funciones de activación

###  Producir la matriz de confusión para representar el resultado del test del modelo

<Tardare--->

### k-Fold Cross-Validation

## Redes neuronales

### Capas (*Layers*)

### Red neuronal

Para esta tarea se realizo una implementación nueva de redes neuronales, parte del código se baso en el código provisto por el profesor.

La estructura que sigue esta implementación es la siguiente:

<Altoque Bodoque>

#### Resultados

### Implementar normalización

La normalización fue implementada en una clase hija de la clase `NeuralNetwork` original (seccion: **Implementar redes neuronales**), llamada `NormalizedNetwork`. Esto, por dos motivos. El primero, para mantener una versión de `NeuralNetwork` sin normalización y aplicar buenas prácticas de programación orientada a objetos. El segundo, para presentar la normalización en una nueva clase que no considere la implementación de la red neuronal.

**Código**: [`code/neural_network/normalized_network.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network/normalized_network.py)

**Test unitario**: [`tests/test_neural_network/test_normalize.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network/test_normalize.py)

### Segundo dataset

### Variación de las neuronas de la capa escondida

## Anexo

### Patrones

### Visualización

