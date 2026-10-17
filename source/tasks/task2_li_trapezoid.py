from source.quadrature.trapezoid import trapezoid
from source.functions.integral_logarithm import li

def calc_li_trapezoid(x):
    result, relative_tolerance, n = trapezoid(li, 2, x, 10**(-10))

    print(f"\nМетод трапеций    Функция Li({x})")
    print("-" * 45)
    print(f"{'Значение интеграла:':<29}{result}")
    print(f"{'Относительная погрешность:':<29}{relative_tolerance}")
    print(f"{'Количество отрезков:':<29}{n}")
    print("-" * 45)


calc_li_trapezoid(10**3)
calc_li_trapezoid(10**4)
calc_li_trapezoid(10**5)