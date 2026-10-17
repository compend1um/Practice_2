from source.quadrature.simpson import simpson
from source.functions.gaussian import gaussian
import pandas as pd
from pathlib import Path
from numpy import pi


# функция, по которой строится таблица:
# функция гаусса под интегналом симпсона, умноженная на корень из единицы, деленной на два пи
def function(z):
    value, _, _ = simpson(gaussian, 0, z, 10 ** (-5))
    return round(
        1 / ( (2 * pi)**0.5 ) * float(value)
        , 5) # точность 5 знаков после точки


def build_table():

    # range не работает с float: генерим десятки, переходим к единицам
    grid_step_lines = [i / 10 for i in range(0, 35, 1)]
    grid_step_columns = [i / 100 for i in range(0, 10, 1)]

    table = {column_value:[] for column_value in grid_step_columns}

    for column_value in grid_step_columns:
        for line_value in grid_step_lines:

            # по вертикали единицы и десятые, по горизонтали - сотые
            # в ячейке - значение функции от х, получаемого сложеним столбца и строчки
            value = function(column_value + line_value)
            table[column_value].append(value)

    df = pd.DataFrame(table, index=grid_step_lines)

    print(
        "=" * 85,
        "Статистическая таблица для стандартного нормального распределения вида",
        "Метод численного интегрирования Симпсона",
        "Точность: 10 ** (-5)",
        "-" * 85,
        df,
        sep="\n"
    )

    # реализовал систему динамического подбора пути:
    # __file__ определяет местоположение текущего .py
    # каждый .parent отбрасывает путь в папку назад.
    # (таким образом выбираемся из tasks/ в project/ )
    # и прокладываем путь в папку с таблицами
    df.to_csv(Path(__file__).resolve().parent.parent.parent /"data"/"output"/"normal_table.csv")
    df.to_excel(Path(__file__).resolve().parent.parent.parent /"data"/"output"/"normal_table.xlsx")
    print("\n",
          "=" * 85, "\n"
          "Таблица сохранена в форматах .csv .excel\n"
          "в папке project/data/output/normal_table",
          sep="")

