"""word_guesser.py: WordGuesser class"""
import string
from random import choice, uniform
from genetic_algorithm.individuals import Individual


def _fitness(word: [str], expected_word: str) -> float:
    score = 0
    for index, letter in enumerate(word):
        if letter == expected_word[index]:
            score += 1
    return score


class WordGuesser(Individual):
    """Word Guesser, generate a random word, with lowercase letters"""

    def __init__(self, mutation_rate: float, actual_word: str):
        super(WordGuesser, self).__init__(_fitness, mutation_rate)
        self.word_to_guess = actual_word
        for index, _ in enumerate(actual_word):
            self.chromosome.append(self._letter())
            self.genes.append(str(index))

    @staticmethod
    def _letter() -> str:
        return choice(string.ascii_lowercase)

    def generate_individual(self) -> Individual:
        """
        Return another Word Guesser

        :return: New word guesser
        """
        return WordGuesser(self.mutation_rate, self.word_to_guess)

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
        self.my_fitness = self.fitness_function(self.chromosome, self.word_to_guess)
        return self.my_fitness
