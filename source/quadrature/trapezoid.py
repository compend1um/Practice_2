

def trapezoid(f, a, b, eps):
    n = 1
    while True:
        step = (b - a) / n # определяет длину каждого отрезка
        result = (f(a) + f(b))/2


        for i in range(1, eps):
            x = a + i * step
            result += f(x)

        result = result * step

        tolerance = (((b - a) * step**2) / 12) * #как-то надо сделать max(f''(x)
        if tolerance < eps:
            return result, tolerance, step

        n *= 2