# Tarea 3

En este reporte se muestra la ubicación del código y de los test unitarios, junto con algunos resultados. Para una versión más extendida  de la explicación y más resultados intermedios ver la [Versión Extendida](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/README%20%28Extended%29.md).

## Programación genética

### Nodos y Árboles

Para la implementación de árboles de operaciones se realizó la implementación de un nodo (`Node`) como clase abstracta (`Abstract Base Class`), la cual contiene argumentos, que serán nodos. Esta permite evaluar, reemplazar algún argumento e inicializar.

Originalmente solo se debe entregar una función y el número de argumentos. Los argumentos en específico se entregaran al inicializar las clases hijas. Posteriormente se cambiarán muchos de estos parámetros para compatibilizar con nodos introducidos posteriormente.

![uml_nodes](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/UML/nodes.png)

**Código**: [`code/genetic_programming/ast/nodes`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/ast/nodes)

**Tests unitarios**: [`tests/test_genetic_programming`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming)

### Árbol sintáctico abstracto (*Abstract Syntatic Tree*)

Para terminar de implemetar un árbol sintáctico se implementó la clase `AST` que termina de agregar los métodos requeridos faltantes que no están en la clase `Node`. Esto incluye reemplazar cualquier nodo, obtener cualquier nodo en el árbol y funcionar como individuo (`Individual`) para cualquier motor genético (`GAEngine`, o *Genetic Algorithm Engine*), esto implica realizar *crossover* y mutaciones. En base a esta clase se implementan individuos específicos para diferentes problemas.

![uml_ast](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/UML/ast.png)

**Código**: [`code/genetic_programming/ast`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/ast)

**Tests unitarios**: [`tests/test_genetic_programming/test_ast`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_ast.py)

### Encontrar un número

Tomando la clase `AST` (sección anterior) se implementa la clase `BinaryAST` que solo especifica las operaciones (o clases hijas de `BinaryNode`) que `AST` puede utilizar para generar árboles. Los resultados observados al intentar adivinar 65346 utilizando los valores: 25, 7, 8, 100, 4, 2; con las operaciones `+`, `-`, `*` y `max` se muestran en los siguientes gráfico.

![unbound_number_max](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/unbound_d_c_e_d_l(max).png)

Se obtuvo uno de los máximos *fitness* por generación y aparte de los máximos, mínimos y promedio. Esto debido a que la escala del máximo valor (cercano a 0) era mucho mayor que para el promedio y los mínimos, para mostrar todos estos se utiliza una escala `symlog`.

![unbound_number](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/unbound_d_c_e_d_l.png)

Además de esta versión, se implementó una versión `01`, es decir, una versión sí/no, para utilizar o no, a lo más una vez, los números en la lista. Utilizando esta versión, implementada en la clase `ChiffresYesNoVariant`, se encontró un número cercano (70000). Esta nueva clase tiene un método completamente distinto para generar un árbol, ya que no utiliza la versión de `AST`.

Los resultados encontrados se muestran en los siguientes gráficos.

![yn_number_max](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/yes-or-no_d_c_e_d_l(max).png)

![yn_number](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/yes-or-no_d_c_e_d_l.png)

**Código**: [`code/genetic_programming/asbt`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/asbt.py), [`code/genetic_programming/chiffres_yn_variant`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/chiffres_yn_variant.py)

**Tests unitarios**: [`tests/test_genetic_programming/test_asbt`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_asbt.py), [`tests/test_genetic_programming/test_chiffres_yes_no_variant`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_chiffres_yes_no_variant.py)

**Ejecutables**: [`tarea3/script/show_DesChiffresEtDesLettres`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/script/show_DesChiffresEtDesLettres.py)	Argumentos: `-w unbound` [*Unbound*], `-w yes-or-no` [*0/1*]

### Variables

Para añadir las variables, el principal problema es evaluar. Ya que la operación se convierte en una ecuación, cuyo estados de libertad está dado por la cantidad de variables encontradas, se requiere que la evaluación reciba valores para reemplazar, convirtiendo el resultado de la evaluación de un valor a un arreglo (`array`, `list` o `[]`). Esto implico realizar un `refactor` e incluir el argumento variable `**kwargs` a todo los métodos que utilizan el método `evaluate`.

Para compatibilizar se utilizó una implementación si existe la variable `values` o no. Cuando no, el funcionamiento seguía siendo el mismo (los test unitarios no se cambiaron), cuando sí, el resultado será un arreglo.

**Código**: [`code/genetic_programming/ast/nodes/terminal_variable`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/ast/nodes/terminal_variable.py)

**Tests unitarios**: [`tests/test_genetic_programming/test_variable`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_variable.py)

### Encontrar una ecuación (no división)

Tomando la clase madre `AST`, se implementa un nuevo `Individual` que genera un árbol sintáctico aleatorio. Esta clase recibe la ecuación a adivinar como un método (`__call__`) de *Python*. Para adivinar una ecuación se requiere saber en que intervalo se requiere que la ecuación encontrada se comporte como la original, o lo más cercano posible. Por ello, el `AST` recibe la lista de valores para evaluar la diferencia. Cada valor de la lista tendrá una diferencia en valor absoluto y estás se sumaran para obtener el *fitness*.

Los resultados encontrados se muestran en los siguientes gráficos.

![eq_guesser](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/symbolic_regression.png)

Esto para encontrar la función

![s_r_equation](https://latex.codecogs.com/svg.latex?\Large&space;f%28x%29%3Dx%5E%7B2%7D%2Bx-6)

**Código**: [`code/genetic_programming/equation_guesser`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/equation_guesser.py)

**Tests unitarios**: [`tests/test_genetic_programming/test_equation_guesser`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_equation_guesser.py)

**Ejecutables**: [`tarea3/script/show_symbolic_regression`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/script/show_symbolic_regression.py)

### División

Se implementó y testeó la división como si fuese cualquier operación. Al dividir por 0, *Python* lanza una excepción `ZeroDivisionError`. Esta `Exception` será atrapada por la evaluación, devolviendo el valor *NaN*, ya que una división por 0 podría ser lo deseado (al intentar adivinar la ecuación *1/x*). Esto será resuelto al calcular el *fitness*, en caso de ser *NaN* el valor será 0, es decir, el mayor *fitness*, en caso contrario; si el valor deseado no es *NaN*, devuelve el valor *Inf*; si el valor original es *NaN*, el *fitness* será el valor absoluto del valor encontrado.

Como el *fitness* es el promedio de las diferencias (en valor absoluto) y en negativo (para que 0 sea el mayor), que alguna diferencia sea *Inf* implica que el promedio es *Inf* y que el *fitness* sea *-Inf*. Este resultado no será graficado y no podrá ser seleccionado como el mejor individuo, a menos que todos hayan obtenido este resultado.

#### Analisis adivinando una ecuación

En este caso, se utiliza el nodo división dentro de la clase `EquationGuesser`. Para ello, se realiza un refactor al código anterior y se agrega el argumento opcional `division` para indicar que `DivNode` será utilizado para la generación del árbol.

El problema acá, es que en la evaluación, se podría generar: `ZeroDivisionError`. Como esto retorna el `float ` *NaN*, la respuesta dependerá también de la función buscada:

1. Si el resultado esperado es `NaN`, la diferencia para ese valor particular será 0.
2. Si el resultado esperado es `NaN` y se obtuvo un número, la diferencia será el valor absoluto del número obtenido.
3. Si el resultado esperado no es `NaN`, pero se obtuvo `NaN`, la diferencia sera `Inf`, lo que implica que el *fitness*, al ser suma de las diferencias, será `-Inf` y como no existe número menor, será un árbol descartado en la etapa de selección.

Los motivos de 1) son triviales. En 3), la explicación es que, ya que el árbol obtiene un *NaN* cuando no debe, no es útil. La elección de la diferencia en 2) es arbitraria, pero mantiene el árbol para selección, ya que si no hay un *fitness* mejor, este podría ser utilizado.

Realizando lo mismo que para la versión sin división, el *fitness* encontrado en diferentes generaciones

![eq_guesser](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/symbolic_regression.png)

Notar que el gráfico cuando se utilizo el nodo `Div` solo se ve el valor máximo, ya que el mínimo y el promedio contienen el valor *-Inf* que no se muestra.

**Código**: [`code/genetic_programming/ast/nodes/div_node`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/ast/nodes/div_node.py)

**Tests unitarios**: [`tests/test_genetic_programming/test_div_node`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_div_node.py)

**Ejecutables**: [`tarea3/script/show_symbolic_regression`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/script/show_symbolic_regression.py)	Argumentos: `-d`

## Análisis de configuraciones

Para obtener el *heatmap* de cantidad de iteraciones variando tamaña de la población y tasa de mutación, se utilizó la función

![s_r_equation_2](https://latex.codecogs.com/svg.latex?\Large&space;f%28x%29%3Dx%5E%7B2%7D%2B2x-15)

Y la clase `EquationGuesser` con la opción de añadir división, obteniéndose

![heatmap](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/heatmap_eq_guesser_div.png)

Lo que muestra que a baja población no se encuentran resultados y los óptimos, a diferencia de los algoritmos genéticos, se encuentran a más altas tasas de mutación.

## Apreciaciones personales

Las partes más complejas, fueron encontrar las configuraciones indicadas para encontrar resultados. Esta dificultad se vio incrementada debido al tiempo que toman estos algoritmos en ejecutarse, lo que disminuye la cantidad de veces que se pueden probar los hiperparámetros.

La otra dificultad, fueron los *refractors* hechos durante la implementación. Muchas nuevas funcionalidades, como añadir variables o la división, implicaban generar valores o nuevos parámetros a clases y métodos ya implementados y testeados. Para este punto, la mejor opción, era siempre dejar el argumento `**kwargs` y siempre recibirlo, para evitar cambiar implementaciones de clases que utilizaban las modificadas.

