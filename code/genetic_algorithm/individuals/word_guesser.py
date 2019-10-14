"""word_guesser.py: WordGuesser class"""
import string
from random import choice
from genetic_algorithm.individuals import Individual


def _fitness(word: [str], expected_word: str) -> float:
    score = 0
    for index, letter in enumerate(word):
        if letter == expected_word[index]:
            score += 1
    return score


def _letter() -> str:
    return choice(string.ascii_lowercase)


class WordGuesser(Individual):
    """Word Guesser, generate a random word, with lowercase letters"""

    def __init__(self, mutation_rate: float, actual_word: str):
        super().__init__(_fitness, _letter, len(actual_word), mutation_rate)
        self.word_to_guess = actual_word
        for index, _ in enumerate(actual_word):
            self.genes.append(str(index))

    def generate_individual(self) -> Individual:
        """
        Return another Word Guesser

        :return: New word guesser
        """
        return WordGuesser(self.mutation_rate, self.word_to_guess)

    def fitness(self, **kwargs) -> float:
        """
        Evaluate fitness for this individual

        :param kwargs:
        """
        return super().fitness(word=self.chromosome, expected_word=self.word_to_guess)
