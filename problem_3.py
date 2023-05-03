"""
Задание № 3:

Написать функцию, которая будет суммировать входные аргументы и может вызывать сама себя рекурсивно.

Например:
written_func(5)() # print должен вывести 5
written_func(5)(10)() # print должен вывести 15
written_func(15)(30)(-10)() # print должен вывести 35
"""


from typing import Union, Callable


def req_sum(add_amount: int = 0, starting_sum: int = 0) -> Union[int, Callable]:
    """
    Чтобы функция могла вызывать сама себя, необходимо, чтобы она возвращала Callable
    объект (в случае, если аргумент отличен от нуля, иначе возвращает результат). При этом, для суммирования
    нужно как-то хранить результат предыдущих итераций.
    """

    # по сути, объявляем декоратор, который передаст в функцию результат предыдущего суммирования
    def func_returner(current_sum_: int):
        def func(add_amount_: int = 0, current_sum: int = current_sum_):
            current_sum += add_amount_
            if add_amount_:
                return func_returner(current_sum)
            else:
                return current_sum

        return func

    starting_sum += add_amount
    if add_amount:
        return func_returner(starting_sum)
    else:
        return starting_sum


print(req_sum(5)())
print(req_sum(5)(10)())
print(req_sum(15)(30)(-10)())
