"""test_multi_individual.py: unittest of Multi Objective Individual abstract class"""
from unittest import main
from test_genetic_algorithm import IndividualTest
from genetic_algorithm.individuals import MultiObjectiveIndividual


class MultiIndividualTest(IndividualTest):

    def std_test_greater_than(self, greater_individual: MultiObjectiveIndividual,
                              lesser_individual: MultiObjectiveIndividual, optimization: int):
        """
        Test comparing of multi fitness functions Individual

        :param greater_individual: Individual with greater fitness
        :param lesser_individual: Individual with lesser fitness
        :param optimization: 0: no optimization, 1: pareto, 2: priority
        """
        greater_individual.priority = False
        lesser_individual.priority = False
        greater_individual.pareto = False
        lesser_individual.pareto = False
        if optimization == 0:
            pass
        elif optimization == 1:
            greater_individual.pareto = True
            lesser_individual.pareto = True
        elif optimization == 2:
            greater_individual.priority = True
            lesser_individual.priority = True
        else:
            NotImplementedError("Unexpected optimization file")
        greater_individual.fitness()
        lesser_individual.fitness()
        self.assertGreater(greater_individual, lesser_individual)


if __name__ == '__main__':
    main()
