"""results: Methods to use for show and evaluate results of network"""

from utils.results.confusion_matrix import confusion_matrix
from utils.results.confusion_matrix import accuracy
from utils.results.confusion_matrix import precision
from utils.results.confusion_matrix import recall
from utils.results.confusion_matrix import f1_score
from utils.results.trainer import Trainer
from utils.results.standard_trainer import StandardTrainer
from utils.results.cross_validation import KFoldTrainer
from utils.results.show_matrix import show_matrix, annotate
