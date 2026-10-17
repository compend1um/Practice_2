from source.quadrature.simpson import simpson
from source.functions.gaussian import gaussian
from numpy import pi


def replace_infinity_to_num(accuracy):
    """
    заменяет бесконечность в вехнем пределе интегрирования
    на достаточно большое число, интегрирование по которое
    не влияет на результат для заданной точности
    """

    new_limit = 0

    while True:

        new_limit += 0.001
        if gaussian(new_limit) / new_limit < accuracy:
            return new_limit


def compare_gaussian_integral_with_pi(
        a=0, b=replace_infinity_to_num(10 ** (-11)), accuracy=10 ** (-10)
):

    result, eps, number_segments = simpson(gaussian, a, b, accuracy)

    print(
        f"Метод Симпсона    Вычисление значения интеграла",
        "-" * 55,
        f"{'Значение интеграла':<43}{result}",
        f"{'Погрешность':<43}{eps}",
        f"{'Количество отрезков':<43}{number_segments}",
        f"{'Замена верхнего предела интегрирования на:':<41} {round(replace_infinity_to_num(10 ** (-11)), 2)}",

        "-" * 55,
        "\n",
        sep="\n"
    )
    right_half = (pi / 2) ** 0.5
    print(
        "Доказательство справедливости равенства",
        "-" * 50,
        f"{'Значение правой части равенства:':<35}{round(right_half, 10)}",
        f"{'Значение левой части равенства:':<35}{result}",
        f"{'Разница:':<35}{abs( float(result) - right_half ):.10f}",
        "-" * 50,
        sep="\n"
    )

