import numpy as np

def monte_carlo(f, a, b, eps, rng, n):
    rng = np.random.default_rng(seed = rng)
    #rng - это сид генерации, нужен по ТЗ :)
    while True:
        x = rng.uniform(a, b, n)
        y = f(x)

        result = (b - a) * np.mean(y)

        sigma_f = np.std(y, ddof=1) # стандартное отклонение (как в тетради у макса)
        tolerance = ((b - a) * sigma_f) / np.sqrt(n)

        ci = (
            result - 1.96 * tolerance, #ci - доверительный интервал, диапазон значений в котором точно находится нужное нам значение площади)))
            result + 1.96 * tolerance,
        )
        relative_tolerance = tolerance/abs(result)

        if relative_tolerance < eps:
            return f"{result:.5f}", f"{relative_tolerance:.5f}", (f"{ci[0]:.5f}", f"{ci[1]:.5f}"), n

        n*=2


        #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


