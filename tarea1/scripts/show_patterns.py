"""show_patterns.py: Show patterns on graphs"""
import matplotlib.pyplot as plt
import logging
from useful import plot_result
from utils.patterns import Line, DoubleLine, Circle, Square

N = int(1e3)
X_MIN = Y_MIN = -50
X_MAX = Y_MAX = 50
FIG_SIZE = (6 * 4 + 2, 6)
TITLE_SIZE = 20
RADIUS = 30
FACE = 50
CENTER = (0.0, 0.0)
SLOPE = (-2.0, 2.0)
INTERCEPT = (-10.0, 10.0)
INTERCEPT1 = (-40.0, -20.0)
INTERCEPT2 = (20.0, 40.0)
TWO_INTERCEPT = (INTERCEPT1, INTERCEPT2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    line = Line(SLOPE, INTERCEPT, (X_MIN, X_MAX), (Y_MIN, Y_MAX))
    double_line = DoubleLine(SLOPE, TWO_INTERCEPT, (X_MIN, X_MAX), (Y_MIN, Y_MAX))
    circle = Circle(RADIUS, CENTER, (X_MIN, X_MAX), (Y_MIN, Y_MAX))
    square = Square(FACE, CENTER, (X_MIN, X_MAX), (Y_MIN, Y_MAX))

    fig = plt.figure(figsize=FIG_SIZE)
    ax1 = fig.add_subplot(141)
    ax2 = fig.add_subplot(142)
    ax3 = fig.add_subplot(143)
    ax4 = fig.add_subplot(144)

    figures = {
        line: ax1,
        double_line: ax2,
        circle: ax3,
        square: ax4
    }

    for figure in figures.keys():
        logging.info("Generating {}".format(figure.name))
        points = figure.training_set(N)
        plot_result(points[0:-1], points[-1], figure, figures[figure])
        figures[figure].set_title(figure.name, fontsize=TITLE_SIZE)

    plt.savefig("../results/patterns.png")
