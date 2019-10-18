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

1. Inicialización: toma el individuo, que realiza la acción con el resultado esperado. (`__init__`)
2. Iniciar población: Dado un tamaño genera una población, lista o *array* de individuos de diferentes `fitness`, lo que se traduce en diferentes cromosomas (`chromosome`). (`initialize_population(size)`)
3. Evaluación: se calcula el *fitness* de cada individuo llamando a su método. Esto lo registra y calcula el máximo alcanzado en la población. (`evaluate_fitness()`)
4. Selección: selecciona los individuos realizando el algoritmo del torneo. Esto deja un tamaño de la población dos veces mayor. Opcionalmente, se le puede dar un tamaño distinto al por defecto. (`selection`())
5. Reproducción: Realiza *crossingover* (método `crossover` de los individuos), reduciendo dos individuos a uno. El nuevo individuo generado, además, muta utilizando el método `mutate(self)` de un individuo. (`repoduction()`)
6. Generar nueva generación: realiza los procesos de selección, reproducción y evaluación, generando una nueva generación posterior a la actual. (`next_generation()`)
7. Correr algoritmo: el algoritmo se puede correr, deteniéndose en tres diferentes escenarios con tres métodos diferentes:
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

## Individuos

