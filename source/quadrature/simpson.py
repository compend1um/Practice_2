import numpy as np

def simpson(func, a, b, accuracy):
    """

    :param func: функция
    :param a: нижний предел интегрирования
    :param b: верхний предел интегрирования
    :param eps: требуемая точность
    :return: (value, error_estimate, n)

    value — приближённое значение интеграла,
    error_estimate — оценку погрешности этого значения,
    n — число разбиений (или итераций), которое потребовалось для достижения точности
    """

    number_segments = 2 # чётное количество равных отрезков для разбиения [a, b]
    previous_result = None
    eps = None

    while True:

        step = (b - a) / number_segments

        x_values = np.linspace(a, b, number_segments + 1)
        y_values = func(x_values)

        result = (step / 3) * (y_values[0] + 2 * np.sum(y_values[2: -1: 2]) +
                             4 * np.sum(y_values[1: -1: 2]) + y_values[-1])

        if previous_result is not None:
            eps = abs(result - previous_result) / 15
            if eps < accuracy:
                return f"{result:.10f}", f"{eps:.10f}", number_segments

        previous_result = result
        number_segments *= 2

    return result


