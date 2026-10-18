from source.quadrature.trapezoid import trapezoid
from source.functions.integral_logarithm import li
from source.functions.primes import primes
from source.quadrature.monte_carlo import monte_carlo

def compare_pi_trapezoid(x):
    result, relative_tolerance, n = trapezoid(li, 2, x, 10**(-10))

    pi_x = primes(x)
    difference = float(result) - pi_x

    print(f"\nСравнение для x = {x}, метод трапеций")
    print("-" * 50)
    print(f"{'Значение Li(x):':<30}{result}")
    print(f"{'Количество простых чисел:':<30}{pi_x}")
    print(f"{'Разница':<30}{difference:.10f}")
    print("-" * 50)


def compare_pi_monte_carlo(x):
    result, relative_tolerance, ci, n = monte_carlo(li, 2, x, 10**(-5), 42, 2200)

    pi_x = primes(x)
    difference = float(result) - pi_x

    print(f"\nСравнение для x = {x}, метод Монте-Карло")
    print("-" * 50)
    print(f"{'Значение Li(x):':<30}{result}")
    print(f"{'Количество простых чисел:':<30}{pi_x}")
    print(f"{'Разница:':<30}{difference:.5f}")
    print("-" * 50)

