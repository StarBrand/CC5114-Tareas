"""sentence_guesser.py: SentenceGuesser class"""
import string
from random import choice
from genetic_algorithm.individuals import Individual


def _fitness(sentence: [str], expected_sentence: str) -> float:
    score = 0
    for index, letter in enumerate(sentence):
        if letter == expected_sentence[index]:
            score += 1
    return score


def _letter() -> str:
    return choice(string.ascii_letters + " .,")


class SentenceGuesser(Individual):
    """Sentence Guesser, generate a random sentence"""

    def __init__(self, mutation_rate: float, actual_sentence: str):
        super().__init__(_fitness, _letter, len(actual_sentence), mutation_rate)
        self.sentence_to_guess = actual_sentence
        for index, _ in enumerate(actual_sentence):
            self.genes.append(str(index))

    def generate_individual(self) -> Individual:
        """
        Return another Word Guesser

        :return: New word guesser
        """
        return SentenceGuesser(self.mutation_rate, self.sentence_to_guess)

    def fitness(self, **kwargs) -> float:
        """
        Evaluate fitness of individual

        :return: Fitness
        """
        return super().fitness(sentence=self.chromosome, expected_sentence=self.sentence_to_guess)
