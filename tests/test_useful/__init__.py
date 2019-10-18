"""test_useful.py: unittest of useful package"""

from test_useful.test_line import TestLine
from test_useful.test_double_line import TestDoubleLine
from test_useful.test_circle import TestCircle
from test_useful.test_square import TestSquare
from test_useful.test_confusion_matrix import ConfusionMatrixTest
from test_useful.test_activation_functions import ActivationFunctionTest
from test_useful.test_set_functions import FunctionTest
from test_useful.test_one_hot_encoding import OneHotTest
from test_useful.test_standard_trainer import StandardTrainerTest
from test_useful.test_cross_validation import KFoldTest
from test_useful.test_oversample import OversampleTest
from test_useful.test_move import MoveTest
from test_useful.toy_maze import tester_maze, tester_robot_out, tester_robot_wrong, tester_robot_wrong_closer
from test_useful.test_maze_rdm import MazeTest
