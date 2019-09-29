"""sentence_guesser.py: SentenceGuesser class"""
import string
from random import choice, uniform
from genetic_algorithm.individuals import Individual


def _fitness(sentence: [str], expected_sentence: str) -> float:
    score = 0
    for index, letter in enumerate(sentence):
        if letter == expected_sentence[index]:
            score += 1
    return score


class SentenceGuesser(Individual):
    """Sentence Guesser, generate a random sentence"""

    def __init__(self, mutation_rate: float, actual_sentence: str):
        super(SentenceGuesser, self).__init__(_fitness, mutation_rate)
        self.sentence_to_guess = actual_sentence
        for index, _ in enumerate(actual_sentence):
            self.chromosome.append(self._letter())
            self.genes.append(str(index))

    @staticmethod
    def _letter() -> str:
        return choice(string.ascii_letters + " .,")

    def generate_individual(self) -> Individual:
        """
        Return another Word Guesser

        :return: New word guesser
        """
        return SentenceGuesser(self.mutation_rate, self.sentence_to_guess)

    def mutate(self) -> None:
        """
        Mutate an allele

        :return: None
        """
        for index, _ in enumerate(self.chromosome):
            if uniform(0, 1) <= self.mutation_rate:
                self.chromosome[index] = self._letter()
        return None

    def fitness(self) -> float:
        """
        Evaluate fitness of individual

        :return: Fitness
        """
        self.my_fitness = self.fitness_function(self.chromosome, self.sentence_to_guess)
        return self.my_fitness
