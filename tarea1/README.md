# Tarea 1

En este reporte se muestra la ubicación del código y de los test unitarios, junto con algunos resultados. Para una versión más extendida de la explicación y más resultados intermedios ver la [Versión Extendida](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/README%20(Extended).md)

## Neuronas

La implementación de las neuronas se realizó en paralelo con las clases de cátedra. Se muestran a continuación los diagramas *UML* de cada una de estas étapas, hasta llegar a la neurona que se pide.

La idea fue implementar un perceptrón para los operadores lógicos, `GatePerceptron`, junto con versiones hijas de cada una de ellas. Luego se generaliza este perceptrón, realizando *refactor* sobre `GatePerceptron`, que ahora hereda de la clase `Perceptron`. `LearningPerceptron` es la versión que puede utilizar y actualizar los pesos de un perceptrón  via composición. `Sigmoid Neuron` es la versión con función de activación *sigmoid* y finalmente *Neuron* generaliza esta noción.

### Perceptrón

![perceptrons](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/perceptron.png)

### *Learning Perceptron*

![learning_perceptron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/learning_perceptron.png)

### Neurona sigmoidea

![sigmoid_neuron](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/UML/sigmoid_neuron.png)

### Neurona

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

###  Implementar la transformación one-hot

La transformación se definió como el método `one_hot_encoding` que recibe una lista o un `array ` y devuelve una tupla de dos elementos, el primero, una versión codificada como `one-hot vector` de la entrada (como lista si recibe una lista o como `numpy.ndarray` en el segundo caso, respetando la estructura `shape`) . El segundo elemento es el diccionario de codificación de la forma `key`: elemento original y `value`: `one-hot vector`.

**Código**: [`code/useful/preprocess_dataset/one_hot_encoding`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/preprocess_dataset/one_hot_encoding.py)

**Test unitario**: [`tests/test_useful/test_one_hot_encoding`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful/test_one_hot_encoding.py)

### Funciones de activación

Las funciones de activación, y sus respectivas derivadas, fueron implementadas como métodos. Para conectar ambas se diseña un diccionario (`derivative`) cuya `key` es la función y `value` es la derivada.

No se utilizó la recomendación del enunciado, porque ya se había implementado antes que ésta fuese subida.

**Código**: [`code/useful/math_functions/activation_functions`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/math_functions/activation_functions.py)

**Test unitario**: [`tests/test_useful/test_activation_functions`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful/test_activation_functions.py)

###  Producir la matriz de confusión para representar el resultado del test del modelo

La matriz de confusión recibe la predicción y las etiquetas (ambas como `numpy.ndarray`) codificadas como *one-hot vector*. Si recibe elementos de una dimensión los convierte a dos dimensiones, de tal forma que queda representado la clase y los elementos que no corresponden a la clase. El método, también chequea las etiquetas y la predicción tengas las mismas dimensiones.

La salida de este método es una matriz de `N x N`, con `N` la cantidad de clases. En caso de solo tener una clase la matriz es de `2 x 2` como la clase y los elementos que no corresponden a la clase. Esta salida se utiliza como entrada para las funciones `accuracy`, `precision`, `recall` y `f1-score`.  

**Código**: [`code/useful/results/confusion_matrix`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/results/confusion_matrix.py)

**Test unitario**: [`tests/test_useful/test_confusion_matrix`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful/test_confusion_matrix.py)

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

### KFold Cross Validation

Para entrenar las redes neuronales se utilizaron dos clases "entrenadoras" (*trainer*). Una, `StandardTrainer`, se utilizó en el ejemplo anterior. La segunda, `KFoldTrainer`, utiliza, y hereda, la clase `KFold` (de la librería [`sklearn`](https://scikit-learn.org/stable/)).

**Código**: [`code/useful/results`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/useful/results)

**Tests unitarios**: [`tests/test_useful`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_useful)

#### Resultados

Se muestran los resultados obtenidos entrenando una red neuronal con *Cross Validation 3Fold*  (se escoge 3, sin ninguna razón particular).

![network3Fold](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/network_on_iris_3fold.png)

Resultados obtenidos en test set (mismos que en la matriz de confusión mostrada arriba), sacados sumando las matrices de las 3 iteraciones:

| Clases          | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **Iris-setosa** | 0.96 | 1.0 | 1.0 | 1.0 |
| **Iris-versicolor** | - | 0.9583 | 0.92 | 0.9388 |
| **Iris-virginica** | - | 0.9231 | 0.96 | 0.9412 |

Ejecutable: [`tarea1/scripts/network_on_iris`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/network_on_iris.py)	Argumentos: `-x 3`

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
| **Iris-setosa** | 0.9111 | 1.0 | 1.0 | 1.0 |
| **Iris-versicolor** | - | 0.8571 | 0.8571 | 0.85714 |
| **Iris-virginica** | - | 0.8571 | 0.0.8571 | 0.8571 |

Ejecutable: [`tarea1/scripts/network_on_iris`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/network_on_iris.py)	Argumento: `-n`

Al igual que para la versión no normalizada, se realizaron mediciones de *Cross validation*. Se escogio el *10Fold* por ninguna razón particular.

![normalized10Fold](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/normalized_on_iris_10fold.png)

Resultados obtenidos en test set (mismos que en la matriz de confusión mostrada arriba), sacados sumando las matrices de las 10 iteraciones:

| Clases          | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **Iris-setosa** | 0.8467 | 1.0 | 1.0 | 1.0 |
| **Iris-versicolor** | - | 0.8857 | 0.62 | 0.7294 |
| **Iris-virginica** | - | 0.7077 | 0.92 | 0.8 |

Ejecutable: [`tarea1/scripts/network_on_iris`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/scripts/network_on_iris.py)	Argumentos: `-n -x 10`

### Otros dataset

Se realizaron más experimentos sobre otros datasets, los cuales son reportados en [`tarea1/results/other_dataset`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset) utilizando el ejecutable [`code/use_network`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/use_network.py) con argumentos distintos.

## Análisis

La implementación de perceptrones y neuronas no tuvo mayor complicación. La, tal vez, excesiva cantidad de clases que se implementaron fueron solo para reflejar la progresión natural y lógica del modelo perceptrón para puerta lógicas al modelo de la neurona con cualquier función de activación.

Las complicaciones encontradas al programar las redes neuronales y las *layers* fueron, principalmente, verificar la implementación de *backpropagation* y diseñar los tests unitarios. Los problemas de *backpropagation* estuvieron dados por las derivadas, no por la derivada en sí, sino por las formas de calcular en base al *output/input* de las respectivas *layers*. Finalmente, fue más fácil aplicar la derivada sobre la función en sí, en lugar de evaluarla desde la entrada de la función, es decir:

![equation](https://latex.codecogs.com/svg.latex?\Large&space;%5Cfrac%7B%5Cpartial%20f%28x%29%7D%7B%5Cpartial%20x%7D%20%3D%20f%27%28x%29%20%3D%20f%27%28f%28x%29%29)

Por ejemplo, con la función *sigmoid*

![sigmoid_equation](https://latex.codecogs.com/svg.latex?\Large&space;%5Cfrac%7B%5Cpartial%20%5Csigma%28x%29%7D%7B%5Cpartial%20x%7D%3D%5Csigma%28x%29%281-%5Csigma%28x%29%29)

Evaluar en sigmoid(x) en lugar de en x.

Las dificultades en el test unitario fue para evaluar si *layer* o la red, efectivamente están aprendiendo en evaluaciones unitarias. Para lograrlo, se optó por evaluar ejemplos extremos (1.0 o 0.0) si verificar que los pesos efectivamente crecían o decrecían.

Otra dificultad fue en encontrar resultados que mostraran lo que se pedía, esto, posiblemente dado, por los problemas de encontrar un mínimo global del gradiente en lugar de un mínimo local. Esto provocó que algunas implementaciones no mostraran aprendizaje. Para ello, se optó por definir el *seed* y ejecutar los scripts hasta que los datos fuesen los buscados.

En lo personal, esta tarea permitió entender los algoritmos de aprendizaje de redes neuronales y la exploración de otros métodos para visualizar resultados. La exploración de estas redes se sigue realizando y se muestra más en la [versión extendida de este markdown](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/README%20(Extended).md)

