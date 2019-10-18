"""results: Methods to use for show and evaluate results of network"""

from useful.results.confusion_matrix import confusion_matrix
from useful.results.confusion_matrix import accuracy
from useful.results.confusion_matrix import precision
from useful.results.confusion_matrix import recall
from useful.results.confusion_matrix import f1_score
from useful.results.trainer import Trainer
from useful.results.standard_trainer import StandardTrainer
from useful.results.cross_validation import KFoldTrainer
from useful.results.show_matrix import show_matrix, annotate
