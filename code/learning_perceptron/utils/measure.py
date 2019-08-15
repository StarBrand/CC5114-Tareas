from learning_perceptron.utils import Line


def confusion_matrix(line: Line,
                     x1: [float], y1: [float],
                     x2: [float], y2: [float]) -> (int, int, int, int):
    fp, tp, fn, tn = (0, 0, 0, 0)
    for i, _ in enumerate(x1):
        success = line.above_line(x1[i], y1[i])
        if success:
            tp += 1
        else:
            fp += 1
    for i, _ in enumerate(x2):
        fail = line.above_line(x2[i], y2[i])
        if fail:
            fn += 1
        else:
            tn += 1
    return fp, tp, fn, tn


def accuracy(fp: int, tp: int, fn: int, tn: int) -> float:
    try:
        return (tp + tn) / (fp + tp + fn + tn)
    except ZeroDivisionError:
        return 0


def precision(fp: int, tp: int) -> float:
    try:
        return tp / (tp + fp)
    except ZeroDivisionError:
        return 0


def recall(tp: int, fn: int) -> float:
    try:
        return tp / (tp + fn)
    except ZeroDivisionError:
        return 0


def f1_score(fp: int, tp: int, fn: int) -> float:
    a = precision(fp, tp)
    b = recall(tp, fn)
    try:
        return 2 * ((a * b) / (a + b))
    except ZeroDivisionError:
        return 0
