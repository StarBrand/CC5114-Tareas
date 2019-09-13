"""ga_result.py: GAResult class"""
from genetic_algorithm import Individual, NullIndividual


class GAResult(object):
    """GAResult, class of result for a genetic algorithm"""

    def __init__(self):
        self.individual = NullIndividual()
        self.found_solution = False
        self._generations = list()
        self._score = list()
        self._ready = False

    def ready_to_export(self, individual: Individual, solution: bool) -> None:
        """
        Ready to export as result, if this method is not called, Result
        will raise Exception

        :param individual: Individual who encounter the solution
        :param solution: Whether the solution was found
        :return: None
        """
        self._ready = True
        self.individual = individual
        self.found_solution = solution
        return

    def register_score(self, score: float, generation: int = 0) -> None:
        """
        Register score

        :param score: Score to registered
        :param generation: Generation of score registered, if not given, next generation after last one
        :raise RuntimeError: If this is for get only
        :return: None
        """
        if self._ready:
            raise RuntimeError("This result is for get info only, not registered")
        if generation == 0:
            try:
                last = self._generations[-1]
            except IndexError:
                last = 0
            self._generations.append(last + 1)
        else:
            self._generations.append(generation)
        self._score.append(score)
        return None

    def get_generations(self) -> [int]:
        """
        Get generations

        :raise: Runtime Error: if this is not yet ready
        :return: Generations registered
        """
        if not self._ready:
            raise RuntimeError("Not ready to return results")
        return self._generations

    def get_scores(self) -> [float]:
        """
        Get generations

        :raise: Runtime Error: if this is not yet ready
        :return: Generations registered
        """
        if not self._ready:
            raise RuntimeError("Not ready to return results")
        return self._score
