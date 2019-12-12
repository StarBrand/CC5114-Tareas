

# Tarea 3

En este reporte se explicará el procesos de implementación, testeo y resultado de la implementación de algoritms genéticos siguiendo el orden lógico por el que se fueron desarrollando. Al final de cada sección se da la ubicación del código fuente en el repositorio y los *scripts* de los test unitarios.

## Programación genética

### Nodos y Árboles

Para la implementación de árboles de operaciones se realizó la implementación de un nodo (`Node`) como clase abstracta (`Abstract Base Class`), la cual contiene argumentos, que serán nodos. Esta permite evaluar, reemplazar algún argumento e inicializar.

Con esta implementación, reemplazar un nodo hijo o argumento se puede solo desde el nodo padre, no se puede cambiar un argumento de un argumento o ningún otro nivel de forma recursiva.

Originalmente solo se debe entregar una función y el número de argumentos. Los argumentos en específico se entregaran al inicializar las clases hijas. Posteriormente se cambiarán muchos de estos parámetros para compatibilizar con nodos introducidos posteriormente.

Los tipos de nodos más usados fueron binarios (`BinaryNode`) y booleano (`BooleanNode`), el cual puede (`OrNode`, `AndNode`, etc) o no (`NotNode`) clase hija de `BinaryNode`. Además de los nodos terminales (`TerminalNode`), el cual es número, booleano o variable (*string* y especificar el tipo de valor por el que será reemplazado: `float` o `bool` ).

![uml_nodes](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/UML/nodes.png)

**Código**: [`code/genetic_programming/ast/nodes`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/ast/nodes)

**Tests unitarios**: [`tests/test_genetic_programming`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming)

### Árbol sintáctico abstracto (*Abstract Syntatic Tree*)

Para terminar de implemetar un árbol sintáctico se implementó la clase `AST` que termina de agregar los métodos requeridos faltantes que no están en la clase `Node`. Esto incluye reemplazar cualquier nodo, obtener cualquier nodo en el árbol y funcionar como individuo (`Individual`) para cualquier motor genético (`GAEngine`, o *Genetic Algorithm Engine*). En base a esta clase se implementan individuos específicos para diferentes problemas.

![uml_ast](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/UML/ast.png)

**Código**: [`code/genetic_programming/ast`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/ast)

**Tests unitarios**: [`tests/test_genetic_programming/test_ast`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_ast.py)

### Variables

Para añadir las variables, el principal problema es evaluar. Ya que la operación se convierte en una ecuación, cuyo estados de libertad está dado por la cantidad de variables encontradas, se requiere que la evaluación reciba valores para reemplazar, convirtiendo el resultado de la evaluación de un valor a un arreglo (`array`, `list` o `[]`). Esto implico realizar un `refactor` e incluir el argumento variable `**kwargs` a todo los métodos que utilizan el método `evaluate`.

Para compatibilizar se utilizó una implementación si existe la variable `values` o no. Cuando no, el funcionamiento seguía siendo el mismo (los test unitarios no se cambiaron), cuando sí, el resultado será un arreglo.

**Código**: [`code/genetic_programming/ast/nodes/terminal_variable`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/ast/nodes/terminal_variable.py)

**Tests unitarios**: [`tests/test_genetic_programming/test_variable`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_variable.py)

### División

Se implementó y testeó la división como si fuese cualquier operación. Al dividir por 0, *Python* lanza una excepción `ZeroDivisionError`. Esta `Exception` será atrapada por la evaluación, devolviendo el valor *NaN*, ya que una división por 0 podría ser lo deseado (al intentar adivinar la ecuación *1/x*). Esto será resuelto al calcular el *fitness*, en caso de ser *NaN* el valor será 0, es decir, el mayor *fitness*, en caso contrario; si el valor deseado no es *NaN*, devuelve el valor *Inf*; si el valor original es *NaN*, el *fitness* será el valor absoluto del valor encontrado.

Como el *fitness* es el promedio de las diferencias (en valor absoluto) y en negativo (para que 0 sea el mayor), que alguna diferencia sea *Inf* implica que el promedio es *Inf* y que el *fitness* sea *-Inf*. Este resultado no será graficado y no podrá ser seleccionado como el mejor individuo, a menos que todos hayan obtenido este resultado.

**Código**: [`code/genetic_programming/ast/nodes/div_node`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/ast/nodes/div_node.py)

**Tests unitarios**: [`tests/test_genetic_programming/test_div_node`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_div_node.py)

## Problemas Analizados

### UML (*Unified Modeling Language*)

Estas fueron las clases implementadas hijas de `AST` que fueron utilizadas para resolver los problemas descritos en las siguientes secciones.

![uml_gp](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/UML/genetic_programming.png)

### Encontrar un número

Tomando la clase `AST` (sección anterior) se implementa la clase `BinaryAST` que solo especifica las operaciones (o clases hijas de `BinaryNode`) que `AST` puede utilizar para generar árboles. Los resultados observados al intentar adivinar 65346 utilizando los valores: 25, 7, 8, 100, 4, 2; con las operaciones `+`, `-`, `*` y `max` se muestran en los siguientes gráfico.

![unbound_number_max](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/unbound_d_c_e_d_l(max).png)

Se obtuvo uno de los máximos *fitness* por generación y aparte de los máximos, mínimos y promedio. Esto debido a que la escala del máximo valor (cercano a 0) era mucho mayor que para el promedio y los mínimos, para mostrar todos estos se utiliza una escala `symlog` que es algo como:

![equation1](https://latex.codecogs.com/svg.latex?\Large&space;%5Cwidehat%7By%7D%3D-%28log%28-y%29%29)

Como `y` es negativo, `-y` es positivo y se le puede aplicar `log`. 

![unbound_number](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/unbound_d_c_e_d_l.png)

Además de esta versión, se implementó una versión `01`, es decir, una versión sí/no, para utilizar o no, a lo más una vez, los números en la lista. Utilizando esta versión, implementada en la clase `ChiffresYesNoVariant`, se encontró un número cercano (70000). Esta nueva clase tiene un método completamente distinto para generar un árbol, ya que no utiliza la versión de `AST`.

Para señalar aquellos que no se ocupan se utiliza una subclase de `float`, implementada: `super neutral`. La cual al ser aplicada en `max`, `+`, `-` y `*` siempre devuelve el otro número (`float`). Por la manera en la que fue implementada, es decir, reescribiendo operaciones básicas en *Python* de la clase `float`, falla al usarla en la operación `min`.

Los resultados encontrados se muestran en los siguientes gráficos.

![yn_number_max](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/yes-or-no_d_c_e_d_l(max).png)

![yn_number](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/yes-or-no_d_c_e_d_l.png)

Utilizando ambas clases y los valores para terminales: -10, -5, 0, 5, 10. Se intentó encontrar el número 20. Esto para distintos valores de individuos y tasas de mutación. Ambos *heatmaps* se muestran a continuación.

![hm_number](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/heatmap_n_guesser.png)

![hm_number_yn](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/heatmap_n_guesser_01.png)

**Código**: [`code/genetic_programming/asbt`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/asbt.py), [`code/genetic_programming/chiffres_yn_variant`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/chiffres_yn_variant.py)

**Tests unitarios**: [`tests/test_genetic_programming/test_asbt`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_asbt.py), [`tests/test_genetic_programming/test_chiffres_yes_no_variant`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_chiffres_yes_no_variant.py)

**Ejecutables**: [`tarea3/script/show_DesChiffresEtDesLettres`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/script/show_DesChiffresEtDesLettres.py)	Argumentos: `-w unbound` [*Unbound*], `-w yes-or-no` [*0/1*]

[`tarea3/script/heatmaps`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/script/heatmaps.py)

### Encontrar una ecuación

Tomando la clase madre `AST`, se implementa un nuevo `Individual` que genera un árbol sintáctico aleatorio. Para inicializarse, esta clase requiere 1) la ecuación a adivinar como un método (`__call__`) de *Python*, 2) los valores para calcular *fitness*, 3) el tipo de variable (disponibles `float` si es un número y `bool` si es verdadero o falso), 4) si se quiere utilizar la operación dividir y 5), como en todo `AST`, la probabilidad que un nodo sea terminal, la profundidad y la tasa de mutación.

El punto 2) es la principal diferencia con adivinar un número. Por lo que, para adivinar una ecuación se requiere saber en que intervalo se requiere que la ecuación encontrada se comporte como la original, o lo más cercano posible. Por ello, el `AST` recibe la lista de valores para evaluar la diferencia. Cada valor de la lista tendrá una diferencia en valor absoluto y estás se sumaran para obtener el *fitness*.

En caso que se utilice el node división, alguno de los valores entregados podría generar: `ZeroDivisionError`. Cuando esto ocurre, como la respuesta es el `float ` *NaN*, la respuesta dependerá también de la función buscada:

1. Si el resultado esperado es `NaN`, la diferencia para ese valor particular será 0.
2. Si el resultado esperado es `NaN` y se obtuvo un número, la diferencia será el valor absoluto del número obtenido.
3. Si el resultado esperado no es `NaN`, pero se obtuvo `NaN`, la diferencia sera `Inf`, lo que implica que el *fitness*, al ser suma de las diferencias, será `-Inf` y como no existe número menor, será un árbol descartado en la etapa de selección.

Los motivos de 1) son triviales. En 3), la explicación es que, ya que el árbol obtiene un *NaN* cuando no debe, no es útil. La elección de la diferencia en 2) es arbitraria, pero mantiene el árbol para selección, ya que si no hay un *fitness* mejor, este podría ser utilizado.

Los resultados encontrados se muestran en los siguientes gráficos.

![eq_guesser](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/symbolic_regression.png)

![eq_guesser_div](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/symbolic_regression%28div%29.png)

Esto para encontrar la función

![s_r_equation](https://latex.codecogs.com/svg.latex?\Large&space;f%28x%29%3Dx%5E%7B2%7D%2Bx-6)

Utilizando todos las operaciones, los valores para terminales [-10, 10] y los valores para *fitness* [-100, 100].  Notar que el gráfico cuando se utilizo el nodo `Div` solo se ve el valor máximo, ya que el mínimo y el promedio contienen el valor *-Inf* que no se muestra.

Para obtener los *heatmap* ya descritos, de cantidad de iteraciones variando tamaña de la población y tasa de mutación, se utilizó la función

![s_r_equation_2](https://latex.codecogs.com/svg.latex?\Large&space;f%28x%29%3Dx%5E%7B2%7D%2B2x-15)

![sr_heatmap](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/heatmap_eq_guesser.png)

![sr_heatmap_div](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea3/results/heatmap_eq_guesser_div.png)

Es decir, la versión factorizada.

**Código**: [`code/genetic_programming/equation_guesser`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_programming/equation_guesser.py)

**Tests unitarios**: [`tests/test_genetic_programming/test_equation_guesser`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_programming/test_equation_guesser.py)

**Ejecutables**: [`tarea3/script/show_symbolic_regression`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/script/show_symbolic_regression.py)	Argumentos: ` ` [*Sin división*], `-d` [*Con división*]

[`tarea3/script/heatmaps`](https://github.com/StarBrand/CC5114-Tareas/tree/master/tarea3/script/heatmaps.py)

