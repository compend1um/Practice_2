def trapezoid(f, a, b, eps):
    n = 1
    result_prev = None
    tolerance = None

    while True:
        step = (b - a) / n
        result = (f(a) + f(b)) / 2

        for i in range(1, n):
            x = a + i * step
            result += f(x)

        result *= step

        if result_prev is not None:
            tolerance = abs(result - result_prev) / 3

        if tolerance is not None and tolerance < eps:
            return result, f"{tolerance:.11f}", n

        result_prev = result
        n *= 2