# CC5114-Tareas
Tareas y ejercicios para el curso CC5114-1 Redes Neuronales y Programación Genética

## Clase 01: Presentación

### Temas

1. Presentación del curso

## Clase 02: Neural Networks: Perceptron

### Temas

1. Conección biológica

2. Módelo toma de decisiones

3. Perceptron

4. Formulación de expresiones lógicas

### Ejercicios

Código: [`code/perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/perceptron)

Tests unitarios: [`tests/test_perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_perceptron)

## Clase 03:  Evaluación

### Temas

1. Evaluación

## Clase 04: Neural Networks: Learning Perceptron

### Temas

1. Algoritmos de aprendizaje
2. Estrategias de aprendizaje
3. Algoritmo de aprendizaje Perceptron
4. Perceptron en acción

### Ejercicios

Código:  [`code/learning_perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/learning_perceptron)

Tests unitarios: [`tests/test_learning_perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_learning_perceptron)

## Clase 05: Neurona sigmoidea y redes neuronales

### Temas

1. Neurona sigmoidea

2. Redes neuronales

### Ejercicios

Código: [`code/learning_perceptron/sigmoid_perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/learning_perceptron/sigmoid_perceptron.py) y [`code/neural_network`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network)

Tests unitarios: [`tests/test_learning_perceptron/test_sigmoid_neuron`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_learning_perceptron/test_sigmoid_neuron.py) y [`tests/test_neural_network`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network)

## Clase 06: Redes neuronales en acción y Tarea 1

### Temas

1. Redes neuronales en acción
2. Tarea 1

### [Tarea 1](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea1)

Código:

* Código utilizado: [`code/perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/perceptron), [`code/learning_perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/learning_perceptron), [`code/neural_network`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/neural_network) y [`code/useful`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful)

* Scripts ejecutables: [`tarea1/scripts`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea1/scripts)

* Markdown: [`tarea1/README.md`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/README%20(Extended).md)

* Tests unitarios: [`tests/test_perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_perceptron), [`tests/test_learning_perceptron`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_learning_perceptron), [`tests/test_neural_network`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_neural_network) y [`tests/test_useful`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful)

## Clase 07: Redes neuronales: Explicación de BackPropagation

### Temas

1. Alimentación
2. Entrenamiento
3. Backpropagation

## Clase 08: Algoritmo genético

### Temas

1. Premisa
2. Algoritmos evolutivos
3. Algoritmo genético
4. Terminología
5. Ejemplo
6. Pasos: inicio, calculo de *fitness*, selección, reprodución

### Ejercicios

Código: [`code/genetic_algorithm`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_algorithm)

Tests unitarios: [`tests/test_genetic_algorithm`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm)

Ejecutables: [`tarea2/script/evaluate_ga_engine_population`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea2/script/evaluate_ga_engine_population.py), [`tarea2/script/evaluate_ga_engine_mutation`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea2/script/evaluate_ga_engine_mutation.py) y [`tarea2/script/evaluate_ga_engine_heatmap`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea2/script/evaluate_ga_engine_heatmap.py)

[`tarea2/script/show_ga_example`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea2/script/show_ga_example.py)	Argumentos: `-t 0` [*Word Guesser*], `-t 1 -m 0.05` [*Sentence Guesser*]

## Clase 09:

### Temas

1. Beneficios de los algoritmos genéticos
2. Ejemplo: códigos binarios
3. Ejemplo: *Traveling Salesman Problem* (Problema del vendedor viajero)

### Ejercicios

Código: [`code/genetic_algorithm/individuals/binary_calculator`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_algorithm/individuals/binary_calculator.py), [`code/genetic_algorithm/individuals/travel_path`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_algorithm/individuals/travel_path.py)

Tests unitarios: [`tests/test_genetic_algorithm/test_binary_calculator`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_algorithm/test_binary_calculator.py), [`tests/test_genetic_algorithm/test_travel_path`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_algorithm/test_travel_path.py)

Ejecutable: [`tarea2/script/show_ga_example`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea2/script/show_ga_example.py)	Argumentos: `-t 2` [*Binary Encoding*], `-t 3 -e 20` [*TSP*]

## Clase 10:

### Temas

1. Multi-objetivo
2. Optimizaciones: Pareto, prioridad
3. Elitismo
4. Ejemplos organismos zoomórficos

### Ejercicios

Código: [`code/genetic_algorithm/individuals/robot_in_maze`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_algorithm/individuals/robot_in_maze.py), [`code/useful/simulations/maze_rdm`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/simulations/maze_rdm.py), [`code/useful/simulations/simple_maze`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/simulations/simple_maze.py) y [`code/useful/simulations/moves`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/simulations/moves.py)

Tests unitarios: [`tests/test_genetic_algorithm/test_robot_in_maze`](tests/test_genetic_algorithm/test_robot_in_maze.py), [`tests/test_useful/test_maze_rdm`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful/test_maze_rdm.py) y [`tests/test_useful/test_simple_maze`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful/test_simple_maze.py)

Ejecutable: [`tarea2/script/show_robot_in_maze`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea2/script/show_robot_in_maze.py)

### [Tarea 2](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea2)

Código:

* Código utilizado: [`code/genetic_algorithm`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_algorithm) y [`code/useful/simulations`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/simulations)

* Scripts ejecutables: [`tarea2/scripts`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea2/scripts)

* Markdown: [`tarea2/README.md`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/README%20(Extended).md)

* Tests unitarios: [`tests/test_genetic_algorithm`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_algorithm) y [`tests/test_useful`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful)

## Clase 11:

### Temas

1. Mejoras no triviales a los algoritmos genéticos
2. Cubrir árboles con ello: Programación Genética (*Genetic Programming*)

### Ejercicios

La mayoría de estos códigos son una *reinterpretación* o están basados en los códigos provistos por JP Silva. La idea era facilitar los test unitarios y mantener la funcionalidad.

Código: [`code/genetic_programming/ast`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_programming/ast)

Tests unitarios: [`tests/test_genetic_programming`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_programming)

## Clase 12:

### Temas

1. Conceptos avanzados de *Genetic Programming*
2. Herramientas teóricas para habilitar la generación de programas complejos

### Ejercicios

Código: [`code/useful/math_functions/super_neutral`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/math_functions/super_neutral.py),  [`code/genetic_programming/ast/nodes/yes_no_node`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_programming/ast/nodes/yes_no_node.py), [`code/genetic_programming/ast/chiffres_yn_variant`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_programming/ast/chiffres_yn_variant.py), [`code/genetic_programming/ast/nodes/if_then_else_node`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_programming/ast/nodes/if_then_else_node.py) y [`code/genetic_programming/ast/nodes/boolean_node`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_programming/ast/nodes/boolean_node.py)

Tests unitarios: [`tests/test_useful/test_super_neutral`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful/test_super_neutral.py),  [`tests/test_genetic_programming/test_yes_no_node.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_programming/test_yes_no_node.py), [`tests/test_genetic_programming/test_chiffres_yes_no_variant`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_programming/test_chiffres_yes_no_variant.py), [`tests/test_genetic_programming/test_if_then_else_node.py`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_programming/test_if_then_else_node.py) y [`tests/test_genetic_programming/test_boolean_node`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_programming/test_boolean_node.py)

Ejecutable: [`tarea3/script/show_DesChiffresEtDesLettres`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/script/show_DesChiffresEtDesLettres.py)	Argumentos: `-w unbound` [*Unbound*], `-w yes-or-no` [*0/1*]

### [Tarea 3](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3)

Código:

* Código utilizado: [`code/genetic_programming`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/genetic_programming) y [`code/useful/math_functions`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/useful/math_functions)

* Scripts ejecutables: [`tarea3/scripts`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/scripts)

* Markdown: [`tarea3/README.md`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/README%20(Extended).md)

* Tests unitarios: [`tests/test_genetic_programming`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_genetic_programming) y [`tests/test_useful`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/test_useful)

## Clase 13:

### Temas

1. 

### Ejercicios

Código: [`code/`](https://github.com/StarBrand/CC5114-Tareas/tree/master/code/)

Tests unitarios: [`tests/`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tests/)

Ejecutable: [`tarea4/`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea4/scripts)

