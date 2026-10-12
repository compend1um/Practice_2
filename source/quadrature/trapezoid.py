import numpy as np

def trapezoid(f, a, b, eps):
    n = 1
    result_prev = None
    tolerance = None

    while True:
        x = np.linspace(a, b, n + 1)
        y = f(x)
        step = (b - a) / n
        result = step/2 * ((y[0] + y[-1]) + 2*np.sum(y[1:-1]))

        if result_prev is not None:
            tolerance = abs(result - result_prev) / 3

        if tolerance is not None and tolerance / abs(result) < eps:
            return f"{result:.10f}", f"{tolerance/ abs(result):.10f}", n

        result_prev = result
        n *= 2