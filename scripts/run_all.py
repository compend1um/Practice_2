
__all__ = ['menu']

from source.tasks import task1_1_gaussian_integral
from source.tasks import task1_2_normal_table
from source.tasks import task2_compare_pi
from source.tasks import task2_li_monte_carlo
from source.tasks import task2_li_trapezoid


def pause(): input("\nНажмите Enter, чтобы продолжить...")


def separator(symbol:str, long=86):
    """
    печатает строку-разделитель, путем дублирования указаной строки \n
    допустимо дублирование '= ' (двух знаков сразу)
    так как длина строки-разделителя останется прежней

    :param symbol: строка, которая будет продублирована на всю строку
    :param long: длинна строки в символах
    :return: примеры вывода: ------------------ / = = = = = = = = = = =
    """
    return symbol * int( long / len(symbol) )


def print_menu():

    print(
        "",
        separator("-"),
        f"{'ПРАКТИЧЕСКАЯ РАБОТА 2':^85}",
        f"{'Вычисление определенных интегралов':^85}",
        separator("-"),
        "\n"
        "\t:: TASK 1",
        "\t\t1. Доказать равенство выражения с помощью метода Симпсона",
        "\t\t2. Построить статическую таблицу для стандартного нормального распределения",
        "\n"
        "\t:: TASK 2",
        "\t\t3. Определить Li(10^3), Li(10^4), Li(10^5) методом трапеций",
        "\t\t4. Определить Li(10^3), Li(10^4), Li(10^5) методом Монте-Карло",
        "\t\t5. Сравнить со значениями π(10^3), π(10^4), π(10^5)\n",
        separator("-"),
        "\t\t0. Выйти\n",

        sep="\n",
    )


def menu():

    while True:

        print_menu()

        users_choice = int(input("Select option (0-5): "))
        print(separator("- "),
              "\n")


        if users_choice == 1:

            task1_1_gaussian_integral.compare_gaussian_integral_with_pi()
            pause()

        if users_choice == 2:

            task1_2_normal_table.build_table()
            pause()

        if users_choice == 3:

            task2_li_trapezoid.calc_li_trapezoid(10 ** 3)
            task2_li_trapezoid.calc_li_trapezoid(10 ** 4)
            task2_li_trapezoid.calc_li_trapezoid(10 ** 5)
            pause()

        if users_choice == 4:

            task2_li_monte_carlo.calc_li_monte_carlo(10 ** 3)
            task2_li_monte_carlo.calc_li_monte_carlo(10 ** 4)
            task2_li_monte_carlo.calc_li_monte_carlo(10 ** 5)
            pause()

        if users_choice == 5:

            task2_compare_pi.compare_pi_trapezoid(10 ** 3)
            task2_compare_pi.compare_pi_trapezoid(10 ** 4)
            task2_compare_pi.compare_pi_trapezoid(10 ** 5)
            task2_compare_pi.compare_pi_monte_carlo(10 ** 3)
            task2_compare_pi.compare_pi_monte_carlo(10 ** 4)
            task2_compare_pi.compare_pi_monte_carlo(10 ** 5)
            pause()

        if users_choice == 0:

            break


menu()

