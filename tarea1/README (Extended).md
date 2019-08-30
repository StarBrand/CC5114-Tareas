# Tarea 1

En este reporte se explicará el procesos de implementación, testeo y resultado de la implementación de neuronas y redes neuronales siguiendo el orden lógico por el que se fueron desarrollando. Al final de cada sección se da la ubicación del código fuente en el repositorio y los *scripts* de los test unitarios.

## Neuronas

### Perceptrón

Siguiendo el orden del curso, primero se implementó la clase [`GatePerceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/perceptron/gate_perceptron.py) (anteriormente `Perceptron`) que solo recibe una entrada de dos argumentos y devuelve un booleano. Sobre este primer perceptrón se implementan los operadores lógicos *and*, *or*, *nand* y *sum*, fijando los pesos a conveniencia.

Abstrayendo este perceptrón se implementa [`Perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/perceptron/perceptron.py) que recibe, en su contructor, el número de argumentos de entrada. Como función de activación utiliza *step*. Utilizando este perceptrón, se realiza *refactoring* sobre `GatePerceptron` y se vuelven a correr los tests unitarios para comprobar que sigue funcionando.

![perceptrons](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/perceptron.png)

**Código**: [`code/perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/perceptron)

**Tests unitarios**: [`tests/test_perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_perceptron)

### *Learning Perceptron*

Pasados los tests, se implementa la clase [`LearningPerceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/learning_perceptron/gate_perceptron.py) que aplica el algoritmo básico de aprendizaje visto en clase. Además de realizar los test unitarios se realizó un proceso de aprendizaje sobre una línea generada al azar. Los resultados se muestran en la siguiente sección y los métodos utilizados se encuentran reportados en la sección: **Anexo/Patrones**

![learning_perceptron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/learning_perceptron.png)

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

**Código**: [`code/learning_perceptron/sigmoid_perceptron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/learning_perceptron/sigmoid_perceptron.py)

**Tests unitario**: [`tests/test_learning_perceptron/test_sigmoid_neuron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_learning_perceptron/test_sigmoid_neuron.py)

### Neurona

Finalmente, para completar los requisitos de la neurona que se pide, se implementa la clase `Neuron` que recibe una función de activación distinta. Las funciones de activación se encuentran implementadas en [`utils/math_functions/activation_functions`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/utils/math_functions/activation_functions.py) (reportado más abajo)

![neuron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/neuron.png)

**Código**: [`code/learning_perceptron/neuron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/learning_perceptron/neuron.py)

**Tests unitario**: [`tests/test_learning_perceptron/test_neuron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_learning_perceptron/test_neuron.py)

#### Resultados

A continuación se muestra como esta neurona con función de activación *tanh* (por ser la única no implementada previamente). Se ve como es capaz de aprender una línea, pero no las dos líneas (se requiere una red para ello).

![training_neuron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/example_neuron.png)

Ejecutable: [`tarea1/scripts/show_neuron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/show_neuron.py)

Para mostrar la diferencia con la red implementada, más abajo, se muestra una neurona sigmoidea que aprende el dataset iris (se utilizan las funciones de testeo que se reportan más abajo).

![neuron_on_iris](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/neuron_on_iris.png)

Como la neurona retorna un valor y no puede retornar un *one-hot vector*, solo se utilizan los primeros 100 datos (de 150) y se define el valor 1.0 como **Iris setosa**. El dataset se divide 80%/20% en *train set* y *test set* posterior a ser aleatorizado (ver función `split_set` más abajo). Se muestra solo *accuracy* y *recall* dado a problemas de división por cero para *precision* y *f1-score*.

Ejecutable: [`tarea1/scripts/neuron_on_iris`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/neuron_on_iris.py)

## Funciones de activación y métodos para pre-procesamiento

### Escoger el dataset

Para este trabajo se escoge el dataset ["iris"](https://archive.ics.uci.edu/ml/datasets/Iris), el cual se descarga y se maneja en forma local.

Para manejar este dataset se importa en forma de `numpy.ndarray`. El método que realiza esta conversión se le llama `import_data`, que recibe el *path* del archivo.

Además se tiene el método `split_set` que separa un `numpy.ndarry` en el porcentaje que se le dé. Antes de eso, además se randomiza utilizando el método [`numpy.random.permutate`](https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.random.permutation.html). Si recibe solo un número (entre 0 y 1) separa el arreglo en dos arreglos, uno con el porcentaje dado y otro con el restante. En cambio, si recibe dos porcentajes, y mientras la suma sea menor que 1, separa el set en dos arreglos que contienen los dichos porcentajes. Este método se usará para separar el dataset en *train set* y *test set*.

**Código**: [`code/utils/preprocess_dataset/set_functions`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/utils/preprocess_dataset/set_functions.py)

**Test unitario**: [`tests/test_utils/test_set_functions`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_utils/test_set_functions.py)

Se muestra un gráfico de la matriz, formada por el *one-hot vector* y los índices del dataset, del dataset completo, de una muestra del 60% y otra del 40%.

![split](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/labels_of_dataset.png)

Ejecutable: [`tarea1/scripts/sample_of_dataset`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/sample_of_dataset.py)

###  Implementar la transformación one-hot

La transformación se definió como el método `one_hot_encoding` que recibe una lista o un `array ` y devuelve una tupla de dos elementos, el primero, una versión codificada como `one-hot vector` de la entrada (como lista si recibe una lista o como `numpy.ndarray` en el segundo caso, respetando la estructura `shape`) . El segundo elemento es el diccionario de codificación de la forma `key`: elemento original y `value`: `one-hot vector`.

**Código**: [`code/utils/preprocess_dataset/one_hot_encoding`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/utils/preprocess_dataset/one_hot_encoding.py)

**Test unitario**: [`tests/test_utils/test_one_hot_encoding`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_utils/test_one_hot_encoding.py)

Una muestra del funcionamiento de este método se muestra en la sección anterior (**Escoger el dataset**).

### Funciones de activación

Las funciones de activación, y sus respectivas derivadas, fueron implementadas como métodos. Para conectar ambas se diseña un diccionario (`derivative`) cuya `key` es la función y `value` es la derivada.

No se utilizó la recomendación del enunciado, porque ya se había implementado antes que ésta fuese subida.

**Código**: [`code/utils/math_functions/activation_functions`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/utils/math_functions/activation_functions.py)

**Test unitario**: [`tests/test_utils/test_activation_functions`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_utils/test_activation_functions.py)

###  Producir la matriz de confusión para representar el resultado del test del modelo

La matriz de confusión recibe la predicción y las etiquetas (ambas como `numpy.ndarray`) codificadas como *one-hot vector*. Si recibe elementos de una dimensión los convierte a dos dimensiones, de tal forma que queda representado la clase y los elementos que no corresponden a la clase. El método, también chequea las etiquetas y la predicción tengas las mismas dimensiones.

La salida de este método es una matriz de `N x N`, con `N` la cantidad de clases. En caso de solo tener una clase la matriz es de `2 x 2` como la clase y los elementos que no corresponden a la clase. Esta salida se utiliza como entrada para las funciones `accuracy`, `precision`, `recall` y `f1-score`.  

**Código**: [`code/utils/results/confusion_matrix`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/utils/results/confusion_matrix.py)

**Test unitario**: [`tests/test_utils/test_confusion_matrix`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_utils/test_confusion_matrix.py)

Ejemplo de una clase como "fuera del círculo", predicha por un algoritmo al azar (con distribución gausseana para mayor contraste de las predicciones sobre el círculo).

![one_class](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/confusion_matrix_one_class.png)

Ejecutable: [`tarea1/scripts/confusion_matrix_example_one_class`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/confusion_matrix_example_one_class.py)

Ejemplo de las tres clases del dataset iris, predichas con un algoritmo al azar.

![three_class](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/confusion_matrix_three_class.png)

Ejecutable: [`tarea1/scripts/confusion_matrix_example_three_class`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/confusion_matrix_example_three_class.py)

### k-Fold Cross-Validation



## Redes neuronales

### Capas (*Layers*)

En lugar de implementar las capas (de ahora en adelante *layers*) como un conjunto de neuronas, se implementan como una nueva clase; para poder aprovechar la multiplicación matricial de la librería [`numpy`](https://www.numpy.org/)

Un *layer* se define por el tamaño de su entrada, de salida y la función de activación. Aprovechando el diccionario definido para las funciones de activación (sección **Funciones de activación**), la derivada se asigna de forma automática. Para esta implementación se define una *abc* en python (que cumple el rol de *interface* y *abstract class*) y un constructor como el patrón de diseño *factory method*.

![layers](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/layers.png)

**Código**: [`code/neural_network/layers`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/neural_network/layers)

**Tests unitarios**: [`tests/test_neural_network`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_neural_network/)

### Red neuronal

Para esta tarea se realizo una implementación nueva de redes neuronales, parte del código se baso en el código provisto por el profesor.

La estructura que sigue esta implementación es la siguiente.

![network](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/network.png)

**Código**: [`code/neural_network/network`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/neural_network/network.py)

**Tests unitarios**: [`tests/test_neural_network/test_network`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_neural_network/test_network.py)

#### Resultados

El primer resultado se realiza intentando predecir dos líneas, siendo la clase deseada los puntos fuera de la línea.

![example_network](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/example_network.png)

Ejecutable: [`tarea1/scripts/show_network`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/show_network.py)

Para mostrar el entrenamiento antes de comparar con la versión normalizada, se entrena la red con el dataset iris. El cual fue separado entre *train set* y *test set* en una proporción 70% / 30% respectivamente.

![example_network](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/network_on_iris.png)

Resultados obtenidos en test set (mismos que en la matriz de confusión mostrada arriba):

| Clases          | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **Iris-setosa** | 0.9333 | 1.0 | 1.0 | 1.0 |
| **Iris-versicolor** | - | 0.8947 | 0.9444 | 0.9189 |
| **Iris-virginica** | - | 0.9091 | 0.8333 | 0.8696 |

Ejecutable: [`tarea1/scripts/network_on_iris`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/network_on_iris.py)

### Implementar normalización

La normalización fue implementada en una clase hija de la clase `NeuralNetwork` original (seccion: **Implementar redes neuronales**), llamada `NormalizedNetwork`. Esto, por dos motivos. El primero, para mantener una versión de `NeuralNetwork` sin normalización y aplicar buenas prácticas de programación orientada a objetos. El segundo, para presentar la normalización en una nueva clase que no considere la implementación de la red neuronal.

![network](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/normalized_network.png)

**Código**: [`code/neural_network/normalized_network.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network/normalized_network.py)

**Test unitario**: [`tests/test_neural_network/test_normalize.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network/test_normalize.py)

Se muestra los resultados del mismo entrenamiento anterior (mismos *seeds*) con la red normalizada y con la misma arquitectura.

![example_network](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/normalized_on_iris.png)

Resultados obtenidos en test set (mismos que en la matriz de confusión mostrada arriba):

| Clases          | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **Iris-setosa** | 1.0 | 1.0 | 1.0 | 1.0 |
| **Iris-versicolor** | - | 1.0 | 1.0 | 1.0 |
| **Iris-virginica** | - | 1.0 | 1.0 | 1.0 |

Ejecutable: [`tarea1/scripts/network_on_iris`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/network_on_iris.py)	Argumento: `-n`

### Distintos dataset

### Variación de las neuronas de la capa escondida

### Revisión de los pesos de las neuronas

## Anexo

### Patrones

Para realizar pruebas mínimas sobre perceptrones, neuronas y redes neuronales, se diseñaron clases sobre figuras en el plano. Para cada una de ellas se define una función para agregar la figura a la gráfica, para identificar si está arriba (afuera) de la figura y para generar un set de entrenamiento.

![uml_pattern](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/patterns.png)

**Código**: [`code/utils/patterns`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/utils/patterns)

**Tests unitarios**: [`tests/test_utils`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_utils)

#### Resultados

![patterns](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/patterns.png)

Ejecutable [`tares1/scripts/show_patterns`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/show_patterns.py)
