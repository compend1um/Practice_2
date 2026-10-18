from source.quadrature.monte_carlo import monte_carlo
from source.functions.integral_logarithm import li


def calc_li_monte_carlo(x, eps=10**(-5), rng=42, n=2200):
    result, relative_tolerance, ci, n = monte_carlo(
        li, 2, x, eps, rng, n
    )

    print(f"\nМетод Монте-Карло    Функция Li({x})")
    print("-" * 45)
    print(f"{'Значение интеграла:':<29}{result}")
    print(f"{'Относительная погрешность:':<29}{relative_tolerance}")
    print(f"{'Доверительный интервал:':<29}[{ci[0]}; {ci[1]}]")
    print(f"{'Количество точек:':<29}{n}")
    print("-" * 45)

