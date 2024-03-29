"""
Задание №1:
На вход подается двумерная сетка произвольного размера, «1» - означает «земля», «0» - вода.
Необходимо посчитать количество островов в сетке.
Островом считается соединенные по горизонтали или вертикали участки замели, окружённые водой.
Можно считать, что края сетки окружены водой.

Например:

Input:
    11110
    11010
    11000
    00000

Output: 1

Input:
    11000
    11000
    00100
    00011
Output: 3
"""


def count_islands(grid: list[list]) -> int:
    """
    Мы проходим по всем элементам двумерного массива один раз - если встречаем 1 - это интересующий нас остров.
    Увеличиваем счётчик на единицу. Но остров может состоять больше, чем из одной клетки, поэтому мы проходим
    по клеткам вокруг него и, если встречаем среди них 1, зануляем, тк это всё ещё наш остров, но предварительно
    обходим и эту клетку и тд. Таким образом, мы достигаем учёта соседствующих единиц как один остров,
    что нам и требуется.
    """

    # обозначаем размеры полученной сетки
    num_of_columns = len(grid)
    num_of_rows = len(grid[0])

    def check_around(row: int, column: int):
        # проверяем на выход за границы сетки
        if any(
            [
                row < 0,
                column < 0,
                row >= num_of_columns,
                column >= num_of_rows,
            ]
        ):
            return

        # в случае равенства единице, зануляем и рекурсивно вызываем проверку уже для окрестности этой клетки
        if grid[row][column] == "1":
            grid[row][column] = "0"
            for i, j in [
                (row - 1, column),
                (row, column + 1),
                (row + 1, column),
                (row, column - 1),
            ]:
                check_around(i, j)

    counter = 0

    # проходим по всем клеткам, встречая единицу, увеличиваем счётчик и зануляем весь остров
    for row_ in range(num_of_columns):
        for column_ in range(num_of_rows):
            if grid[row_][column_] == "1":
                counter += 1
                check_around(row_, column_)

    return counter


size = int(input("Введите количество строк сетки: "))
grid = []
for i in range(size):
    row = list(input().strip())
    grid.append(row)

print(count_islands(grid))
