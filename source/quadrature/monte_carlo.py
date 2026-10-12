import numpy as np

def monte_carlo(f, a, b, eps, rng, n):
    rng = np.random.default_rng(seed = rng)
    #rng - это сид генерации, нужен по ТЗ :)
    while True:
        x = rng.uniform(a, b, n)
        y = f(x)

        result = (b - a) * np.mean(y)

        sigma_f = np.std(y) # стандартное отклонение (как в тетради у макса)
        tolerance = ((b - a) * sigma_f) / np.sqrt(n)

        ci = (
            result - 1.96 * tolerance, #ci - доверительный интервал, диапазон значений в котором точно находится нужное нам значение площади)))
            result + 1.96 * tolerance,
        )

        if tolerance < eps:
            return float(f"{result:.5f}"), float(f"{tolerance:.5f}"), (float(f"{ci[0]:.5f}"), float(f"{ci[1]:.5f}"))

        n*=4


        #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


