# Tarea 2

En este reporte se explicará el procesos de implementación, testeo y resultado de la implementación de algoritms genéticos siguiendo el orden lógico por el que se fueron desarrollando. Al final de cada sección se da la ubicación del código fuente en el repositorio y los *scripts* de los test unitarios.

## Algoritmos genéticos

### Primera implementación (Engine)

La primera implementación de un algoritmo genético se hizo basada en la descripción de tres etapas:

1. Evaluación (`evaluate_fitness`)
2. Selección (`selection`)
3. Reproducción (`reproduction`)

Todo ello se implemento en la clase `GAEngine` (de *"Genetic Algorithm Engine"* o motor de algoritmo genético). Esta clase toma referencia que existe una clase `Individual` (individuo) que se comporta como un individuo (ver más abajo) de un algoritmo genético. Básicamente un individuo debe poder:

1. Evaluar su *fitness* (`fitness(**kwargs)`, guardado en `my_fitness`)
2. Generar un nuevo individuo (`generate_individual()`) que tenga el mismo comportamiento, pero distinta *performance* (`fitness`).
3. Mutar (`mutate`) y reproducirse con otro individuo realizando *crossingover* (entrecruzamiento) (`crossover(individual: Individual)`).

Con ello el algoritmo genético realiza los pasos requeridos en sus diferentes métodos:

1. **Inicialización**: toma el individuo, que realiza la acción con el resultado esperado. (`__init__`)
2. **Iniciar población**: Dado un tamaño genera una población, lista o *array* de individuos de diferentes `fitness`, lo que se traduce en diferentes cromosomas (`chromosome`). (`initialize_population(size)`)
3. **Evaluación**: se calcula el *fitness* de cada individuo llamando a su método. Esto lo registra y calcula el máximo alcanzado en la población. (`evaluate_fitness()`)
4. **Selección**: selecciona los individuos realizando el algoritmo del torneo. Esto deja un tamaño de la población dos veces mayor. Opcionalmente, se le puede dar un tamaño distinto al por defecto. (`selection`())
5. **Reproducción**: Realiza *crossingover* (método `crossover` de los individuos), reduciendo dos individuos a uno. El nuevo individuo generado, además, muta utilizando el método `mutate(self)` de un individuo. (`repoduction()`)
6. **Generar nueva generación**: realiza los procesos de selección, reproducción y evaluación, generando una nueva generación posterior a la actual. (`next_generation()`)
7. **Ejecutar algoritmo**: el algoritmo se puede correr, deteniéndose en tres diferentes escenarios con tres métodos diferentes:
   1. **Al encontrar un puntaje**: pese a que esto no es lo que se busca, porque se desconoce la solución correcta, se utiliza para testear problemas con soluciones conocidas. Particularmente "adivinar" algo (lo que tiene fitness conocido y único si logra adivinar). Para efectos de ser utilizada para casos más generales, recibe un delta aceptable para detener el algoritmo. (`run_to_reach(expected_score, acceptable, population_size)`)
   2. **Al llegar a un equilibrio**: cuanto el fitness no mejora en una cierta cantidad de generaciones (`equilibrium`). (`run_to_equilibrium(population_size, equilibrium)`)
   3. **Una cantidad fija de generaciones**: No realiza más iteraciones que las dadas. (`run_fixed_generation(population_size, max_generation)`). Adicionalmente los otros  dos métodos, se detienen, para no correr un algoritmo eternamente, en un máximo de generaciones, que puede ser fijado por usuario (parámetro opcional `max_generation`).

![gaengine](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/UML/genetic_algorithm.png)

**Código**: [`code/genetic_algorithm/genetic_algorithm_engine`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/genetic_algorithm_engine.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_genetic_algorithm_engine`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_genetic_algorithm_engine.py)

#### Resultados de un algoritmo genético

Para obtener los resultados, `GAEngine` retorna los resultados en forma de un objeto de la clase `GAResult` (de _Genetic Algorithm Result_ o resultado de algoritmo genético). Esta clase permite registrar el mejor fitness alcanzado por cada generación, además controla cuando puede ser exportado (no se puede registrar), permitiendo que el resultado no sea alterado una vez es retornado.

**Código**: [`code/genetic_algorithm/ga_result`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/ga_result.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_ga_result`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_ga_result.py)

### Implementación con optimizaciones para varios objetivos

Para varios objetivos o funciones de fitness, la simple comparación no logra seleccionar el mejor fitness. Para ello, se utilizan las optimizaciones vistas:

1. **Sin optimizaciones**: comparar el mínimo valor dentro del fitness. (`Optimization.NONE`)
2. **Por prioridad**: compara el primer valor de fitness, en caso de igualdad, compara el siguientes y así. (`Optimization.PRIORITY`)
3. **Pareto**: para ser mayor, alguna función de fitness, debe ser mayor (estrictamente) y las demás mayores o iguales (o mayo no estricto). Esto significa que ninguna función de fitness puede ser menor para que el individuo sea más apto que otro. (`Optimization.PARETO`)

Con el fin de mantener el orden lógico, y las buenas prácticas de programación orientada a objetos, la implementación con estas optimizaciones es una clase hija de `GAEngine` llamada `GAEOptimized`.

![gaeoptimized](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/UML/genetic_algorithm_optimized.png)

Esta clase recibe como parámetro una instancia del individuo (se espera que sea un `MultiObjetiveIndividual`, descrito más abajo) tal como `GAEngine` y la optimización a implementar. Estas opciones están definidas en la clase `Optimization`.

Esta clase además, realiza la selección utilizando **elitismo**, es decir, rescata de la generación anterior al máximo fitness de la generación anterior.

**Código**: [`code/genetic_algorithm/genetic_engine_optimized`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/genetic_engine_optimized.py) y [`code/genetic_algorithm/options`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/options.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_engine_optimized`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_engine_optimized.py)

#### Testeo de optimizaciones

Para realizar el test unitario se diseñaron dos pares de funciones con óptimos diferentes al ser seleccionadas bajo distintas optimizaciones. El primer par de funciones, diferencian entre no optimizar y prioridad. Reciben como único atributo (y único gen) un `float`. La segunda función es siempre menor que la primera en el rango [0, 10], por lo que, para la no optimización, siempre se compara la segunda función, sin embargo, por prioridad, se compara la primera función primero. Ambas tienen máximos diferentes en el rango [0, 10]. Ambas funciones se muestran en el gráfico de la izquierda.

![testmultifitness](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/plot_for_unittest.png)

Cualquier selección por pareto dará el mismo óptimo que por prioridad y cualquier selección por prioridad dará el mismo óptimo o no podrá seleccionar, por pareto. Por ello, se escogió un par de ecuaciones distinta, con una función con un óptimo bien marcado y otra función constante, en el mismo rango anterior. Este test se muestra en el gráfico anterior en la figura derecha.

Como se esperaba los óptimos encontrados fueron ~ 6.0 para prioridad, ~4.0 para pareto y ~10 para el mínimo simple. La diferencia obtenida ante el valor esperado se debe a que la generación de individuos fue la generación al azar de números entre ]0, 10[ con distribución uniforme, el `crossover` y la mutación no influye al ser solo un cromosoma. Lo que no es una complicación, ya que ambas cosas son testeadas en la clase `GAEngine` y en las implementaciones concretas de los individuos.

**Ejecutable**: [`tarea2/script/test_optimize_functions`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/test_optimize_functions.py)

## Individuos

Para simular y modelar los problemas que serán resueltos por un algoritmo genético, se utiliza la clase `Individual`, las cuales cumplen las siguientes propiedades:

1. **Inicialización** (`__init__(fitness_function, generation_function, chromosome_size, mutation_rate)`): para inicializar un individuo se necesita definir (y por lo tanto pasar como argumento):

   1. Función de fitness: que define el resultado de una combinación de atributos (guardado en los genes) en el problema que se busca modelar.

   2. Función de generación: que define la forma de generar, de manera aleatoria, los valores de cada gen.

   3. Tamaño del cromosoma: cantidad de genes (o características) que tendrá el individuo.

   4. Tasa de mutación: cantidad, en porcentaje, de genes a cambiar de una generación a otra.

      *Nota*: la implementación de esto es generar un número al azar, con distribución unitaria, si el número generado es menor a la tasa de mutación, entonces el gen cambia.

2. **Generar un individuo** (`generate_individual()`): genera un nuevo individuo, es decir, una nueva instancia del individuo en concreto. Lo que significa, mismo comportamiento, pero con diferentes atributos o genes. Esto sirve para generar una población completa en el algoritmo genético.

3. **Fitness** (`fitness(self, **kwargs)`): Calcula el fitness, lo guarda dentro de la instancia y lo retorna. Dado las diferentes formas de calcularlo, la versión abstracta de este método recibe los argumentos variables con llave `**kwargs`

4. **Mutar** (`mutate()`): Cambia el valor de algunos genes considerando la tasa de mutación.

5. **Crossover** (`crossover(partner)`): Combina los cromosomas del individuo que llama el método y el individuo que se recibe como parámetro. El individuo resultante llama al método `mutate`.

6. **`Overridding` de operaciones intrínsecas**: para facilitar operaciones útiles entre individuos, ciertas operaciones son redefinidas en la clase individuos:

   1. **Largo** (`__len__`): el largo de un individuo es la cantidad de genes.
   2. **Mayor, menor, estricto y no estricto** (`__gt__`, `__lt__`, `__ge__`, `__le__`): las comparaciones numéricas están basadas en el resultado del fitness, lo que implica que si no se ha calculado, se comparará el *placeholder* del individuo (por defecto 0). La implementación no es tan trivial (algunas son definidas usando operaciones de orden, pero otras son negaciones), debido a los posteriores cambios necesarios en la clase abstracta `MultiObjectiveIndividual`.
   3. **Igualdad** `__eq__`: compara cada elemento que conforma el individuo. Útil para calcular el equilibrio o para realizar test unitarios.

Los individuos son una clase abstracta, por la particularidad de cada modelo, es probable tener que redefinir algunas operaciones más allá de las cuatro nombradas en la inicialización (`__init__`). En principio, todo individuo concreto debería no recibir argumentos en la inicialización o la tasa de mutación.

En pos de realizar test unitarios se define el individuo nulo (`NullIndividual`) siguiendo el patrón de diseño *Objeto Nulo* (*Null Object*).

**Código**: [`code/genetic_algorithm/individuals/individual`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/individual.py) y [`code/genetic_algorithm/individuals/null_individual`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/null_individual.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_individual`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_individual.py) y [`tests/test_genetic_algorithm/test_null_individual`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_null_individual.py)

![individual](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/UML/individuals.png)

### Adivinador de palabras (`WordGuesser`)

Adivinar una palabra no es un problema abierto, pero sirve para mostrar la capacidad de un algoritmo genético. El fitness se define como la cantidad de letras acertadas, lo que significa que el mayor puntaje posible es el largo de la palabra.

Eso hace que para este modelo, ejecutar el algoritmo hasta alcanzar este puntaje máximo conocido tiene sentido. El cromosoma tiene como gen una letra, lo que significa que la cantidad de genes es también el largo de la palabra a adivinar.

**Código**: [`code/genetic_algorithm/individuals/word_guesser`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/word_guesser.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_word_guesser`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_word_guesser.py)

#### Resultados y análisis

Al realizar esta implementación de un individuo concreto, se realizaron además algunos análisis sobre los hiperparámetros necesarios para el algoritmo genético. Esto por dos motivos: 1) el óptimo fitness conocido y 2) lo rápido (pocas iteraciones) necesarias en este problema.

Con una tasa de mutación de 0.3 (30%) y una población de 500 individuos, el avance en el fitness se muestra a continuación:

![guess_algorithm](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/word_guesser.png)

**Ejecutable**: [`tarea2/script/show_ga_example`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/show_ga_example.py)	**Argumentos**: `-t 0`

Para mostrar el efecto de estos hiperparámetros, se varía la población y la tasa de mutación por separado.

![wg_population](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/algorithm_vs_population.png)

**Ejecutable**: [`tarea2/script/evaluate_ga_engine_population`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/evaluate_ga_engine_population.py)

![wg_mutation](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/algorithm_vs_mutation.png)

**Ejecutable**: [`tarea2/script/evaluate_ga_engine_mutation`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/evaluate_ga_engine_mutation.py)

Y al variar ambas se realizó el siguiente heatmap:

![wg_heatmap](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/algorithm_heatmap.png)

**Ejecutable**: [`tarea2/script/evaluate_ga_engine_heatmap`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/evaluate_ga_engine_heatmap.py)

Este heatmap muestra que entre mayor sea la población más rápido se encontrará la palabra, dado por la probabilidad de encontrarla en la simple generación al azar. Por otro lado, la tasa de mutación presenta una menor *performance* a bajo y a altos porcentajes. A bajos porcentajes, se impide ingresar nuevos letras al proceso, y en altos porcentajes, el *crossingover* pierde importancia al lado de la constante generación poblaciones completamente nuevas.

### Adivinador de una frase (`SentenceGuesser`)

Básicamente, es una implementación idéntica a la clase `WordGuesser`. Tiene sentido, entonces, que se necesiten una menor tasa de mutación (ahora las posibilidades de encontrar el carácter correcto en la posición correcta es mucho menor, al haber más caracteres, minúsculas, mayúsculas y espacio, y más posiciones) y una mayor población.

**Código**: [`code/genetic_algorithm/individuals/sentence_guesser`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/sentence_guesser.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_sentence_guesser`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_sentence_guesser.py)

#### Resultados:

![sentence](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/sentence_guesser.png)

**Ejecutable**: [`tarea2/script/show_ga_example`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/show_ga_example.py)	**Argumentos**: `-t 1 -m 0.05`

### Calculadora de binarios (`BinaryCalculator`)

Calcular binarios también es un problema con óptimo conocido, ya que un el mayor fitness es cuando se encuentra el binario correspondiente y al calcular la diferencia se obtiene 0. Por lo que el fitness se calcula como el inverso aditivo del valor absoluto de la diferencia, generando valores menores al 0 esperado. El largo del binario debe ser calculado, ya que la cantidad de genes debe ser fijo o se le debe dar un número exagerado.

**Código**: [`code/genetic_algorithm/individuals/binary_calculator`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/binary_calculator.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_binary_calculator`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_binary_calculator.py)

#### Resultados:

![binary_calc](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/binary_calculator.png)

**Ejecutable**: [`tarea2/script/show_ga_example`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/show_ga_example.py)	**Argumentos**: `-t 2`

### El Problema del vendedor viajero o *Traveling Sales Problem* (`TravelPath`)

Para este problema particular, se debe redefinir ciertas operaciones estándar de la clase `Individual`.

1. Entrecruzamiento (`crossingover`): ya no se puede intercambiar un trozo del cromosoma desde el quiasma (*chiasma*) por otro, ya que esto puede retornar un ruta inválida. En vez de esto, el intercambio es entre un fragmento en que cada punto visitado es igual en ambos individuos y este es intercambiado.
2. Mutación (`mutate`): no se puede cambiar un gen por uno nuevo, se debe intercambiar para evitar recorrer más, o menos, de una vez un punto del camino.

#### Resultados:

![sentence](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/travel_path.png)

**Ejecutable**: [`tarea2/script/show_ga_example`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/show_ga_example.py)	**Argumentos**: `-t 3 -e 20`

## Individuos con más de un objetivo (`MultiObjectiveIndividual`)

Hay problemas que necesitan más de una función de fitness para ser modelados. Para ello se define una nueva clase abstracta que hereda de la clase abstracta `Individual`. Las diferencias fundamentales son:

1. **Multi-fitness**: El fitness ahora son varias funciones, por lo que el parámetro `fitness_function`, es un `array` o lista  de funciones. El cálculo es similar, y el fitness que se guarda en la instancia es el menor en el `array`. El `array` con todos los fitness se guarda en la variable `multi_fitness`.
2. **Optimizaciones**: Las variables booleanas `pareto` y `priority` indican si las comparaciones se realizan utilizando alguna de estas dos optimizaciones. Si ambas son falsas, se compara el `fitness` registrado, es decir, el menor fitness.

**Código**: [`code/genetic_algorithm/individuals/multi_objective_individual`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/multi_objective_individual.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_multi_individual`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_multi_individual.py)

### Robot en laberinto (`RobotInMaze`)

Un individuo con multi-objetivos es el robot en el laberinto. Las dos funciones son distancia a la salida y largo del camino (en ese orden de prioridad). Como ambas funciones se requieren minimizar, se utilizaran los inversos aditivos. Para el cálculo es necesario tener la simulación al laberinto (siguiente subsección).

**Código**: [`code/genetic_algorithm/individuals/robot_in_maze`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/robot_in_maze.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_robot_in_maze`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_robot_in_maze.py)

#### Laberinto (`Maze`)

Para la simulación del laberinto se utilizó el algoritmo de división recursiva (*recursive division method*), el cual toma una cámara (pieza vacía) que se divide dos veces dejando tres espacios para mantener las cámaras conexas. Esto se realiza recursivamente hasta tener un laberinto con caminos de ancho uno. Este laberinto calcula si un camino encuentra el final del laberinto o donde llega, tomando un set de movimientos (clase `Move`) los cuales serán los genes del cromosoma de `RobotInMaze`.

Encontrar las funciones de fitness, que permitían encontrar y dirigir los cromosomas para resolver el problema de encontrar la salida a este laberinto, se hizo un tema complicado. Debido a ello, y para utilizar las funciones sugeridas en clase se desarrollo un laberinto simple (siguiente subsección)

**Código**: [`code/useful/simulations/maze_rdm`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/useful/simulations/maze_rdm.py) y [`code/useful/simulations/moves`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/useful/simulations/moves.py)

**Tests unitarios**: [`tests/test_useful/test_maze_rdm`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_useful/test_maze_rdm.py)

#### Laberinto simple, con obstáculos (`SimpleMaze`)

**Código**: [`code/useful/simulations/simple_maze`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/useful/simulations/simple_maze.py)

**Tests unitarios**: [`tests/test_useful/test_simple_maze`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_useful/test_simple_maze.py)

#### Resultados

Sobre este laberinto simple se ejecutó el algoritmo con elitismo. Dado que el principal objetivo es encontrar la salida se utiliza la optimización por prioridad, y dado que, en el algoritmo del laberinto, encontrar la salida no es lo mismo que salir, la salida tiene una distancia de 0.0, pero salir tiene una distancia de 10.0 (bastaba con cualquier número mayor a 0.0) de forma que salir sea lo más valorado por el algoritmo.

El gráfico realizado muestra el cambio en el fitness por cada generación y además, muestra los laberintos encontrados al principio, del primero en salir y la solución encontrada por el algoritmo.

![show_maze](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/robot_in_maze.png)

**Ejecutable**: [`tarea2/script/show_robot_in_maze`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/show_robot_in_maze.py)

### Unbound-Knapsack (`UnboundKnapsack`)

Para el problema de mochila sin restricción (o *Unbound Knapsack problem*), la simulación incluye 15 cromosomas, referidos al máximo número de elementos que puede tener la mochila (ya que la caja menos pesada, pesa 1 kg). Para generar cada uno se escoge alguna de las cajas (clase `Box`) disponibles y una caja vacía para poder simular menos de 15 elementos.

Las funciones de fitness son:

1. Que el peso no sea mayor a 15 kg. Representado con un la diferencia entre el peso encontrado y el permitido. Como no es importante que se justo 15 kg o menos, si el peso es menor a 15 se devolverá el valor 0, si es mayor, se devuelve en negativo.
2. El valor obtenido, al sumar el valor de las cajas.

Ya que la primera es una restricción, se utilizará la optimización por prioridad para asegurar que el primer fitness sea 0 y el motor optimizado (`GAEOptimized`) con elitismo. El criterio para detener el algoritmo es encontrar 10 veces el mismo valor (`run_to_equilibrium(population_size, equilibrium=10)`)

**Código**: [`code/genetic_algorithm/individuals/unbound_knapsack`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/unbound_knapsack.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_unbound_knapsack`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_unbound_knapsack.py)

#### Análisis

Para observar cuales son los mejores hiperparámetros para resolver este problema, se realizaron tres *heatmap* ("mapas de calor") indicando la cantidad de iteraciones que se realizan para encontrar el óptimo, el peso de la mochila y el valor contenidos respectivamente.

![heatmap_uk](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/algorithm_heatmap_multi_obj.png)

**Ejecutable**: [`tarea2/script/heatmap_unbound_knapsack`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/heatmap_unbound_knapsack.py)

#### Resultados

Tomando uno de los mejores resultados de los heatmap anteriores, es decir, mayor valor, diferencia del peso en 0 y menor cantidad de iteraciones.

![uk](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/unbound_knapsack.png)

La discrepancia entre que los mínimos valores sean mayores que los máximos, es que los máximos valores se buscan entre los que cumplen con el peso requerido. Por ello los valores "mínimos", son los valores encontrados que superaron por más la diferencia de peso, y, por lo tanto, tiene sentido que tengas valores tan altos.

**Ejecutable**: [`tarea2/script/show_knapsack_problem`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/show_knapsack_problem.py)	**Argumentos**: `-w unbound`

### 0-1-Knapsack (`Knapsack01`)

Misma lógica que `UnboundKnapsack`, salvo que los cromosomas, está vez, son 0 o 1 indicando si el item se guarda o no. Debido a que la implementación es tan similar, esta clase `Knapsack01` hereda de `UnboundKnapsack`.

**Código**: [`code/genetic_algorithm/individuals/_01_knapsack`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/genetic_algorithm/individuals/_01_knapsack.py)

**Tests unitarios**: [`tests/test_genetic_algorithm/test_01_knapsack`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tests/test_genetic_algorithm/test_01_knapsack.py)

#### Resultados

![01k](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/results/0-1_knapsack.png)

#### **Ejecutable**: [`tarea2/script/show_knapsack_problem`](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea2/script/show_knapsack_problem.py)	**Argumentos**: `-w 01`

