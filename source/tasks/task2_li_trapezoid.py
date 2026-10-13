from source.quadrature.trapezoid import trapezoid
from source.functions.integral_logarithm import li


def calc_li(b):
    result, relative_tolerance, n = trapezoid(li, 2, b, 10**(-10))

    print(f"\nФункция Li({b})")
    print("-" * 45)
    print(f"{'Значение интеграла:':<28}{result}")
    print(f"{'Относительная погрешность:':<28}{relative_tolerance}")
    print(f"{'Количество отрезков:':<28}{n}")
    print("-" * 45)


calc_li(10**3)
calc_li(10**4)
calc_li(10**5)