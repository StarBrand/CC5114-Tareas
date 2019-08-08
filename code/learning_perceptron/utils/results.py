import matplotlib.pyplot as plt
from random import uniform
from learning_perceptron import LearningPerceptron


def results(perceptron: LearningPerceptron,
            range_x: (float, float),
            range_y: (float, float),
            n: int) -> ([float], [float], [float], [float]):
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for i in range(n):
        x = uniform(range_x[0], range_x[1])
        y = uniform(range_y[0], range_y[1])
        if perceptron.output(x, y):
            x1.append(x)
            y1.append(y)
        else:
            x2.append(x)
            y2.append(y)

    return x1, y1, x2, y2


def plot_result(x1: [float], y1: [float], x2: [float], y2: [float],
                first_point: (float, float),
                second_point: (float, float),
                perceptron: LearningPerceptron) -> None:
    x = [first_point[0], second_point[0]]
    y = [first_point[1], second_point[1]]
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(x1, y1, '.')
    ax.plot(x2, y2, '.')
    ax.plot(x, y)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.set_title("{}, trainings: {}".format(perceptron.name, perceptron.number_of_training), fontsize=14)
    ax.grid()

    return
