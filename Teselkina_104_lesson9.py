from typing import Tuple, Set, FrozenSet, List


# 1
def duplicates(tuple_: tuple) -> bool:
    # объявляем функцию с одним параметром(будет передаваться аргумент типа кортеж), которая будет возвращать True/False
    for elem in tuple_:  # цикл: для каждого элемента в кортеже
        count_elem = tuple_.count(elem)
        # переменная, которая ссылается на значение работы функции - количество повторений в кортеже
        if count_elem > 1:  # условие: если колчество повторений больше одного
            return True  # функция, которая возвращает True
        else:  # альтернативное условие
            return False  # функция, которая возвращает False


# 2
def work_with_set(my_set_: set, my_frozenset_: frozenset) -> tuple[set, set]:
    # объявляем функцию с двумя параметрами, которая будет возвращать кортеж из двух множеств
    new_set: Set = my_set_.union(my_frozenset_)  # переменная, которая ссылается на объединение двух множеств
    intersection_: Set = my_set_ & my_frozenset_  # переменная, которая ссылается на пересечение двух множеств
    return new_set, intersection_  # функция, которая возвращает кортеж, состоящий из двух множеств


# DZ/ 1
def home_task_1(tuple_2_: tuple) -> int:  # объявляем функцию с одним параметром, которая будет возвращать цклое число
    tuple_sum: int = sum(tuple_2_)  # переменная, которая ссылается на сумму чисел кортежа
    return tuple_sum  # функция, которая возвращает целое число


# DZ/ 2
def home_task_2(long_word_: tuple):
    # объявляем функцию с одним параметром, которая будет возвращать сколько каждого элемента в кортеже
    list_: List = []  # переменная, которая ссылается на пустой список

    for elem in long_word_:  # цикл: для каждого элемента в кортеже
        if elem not in list_:  # условие: если элемента нет в списке
            list_.append(elem)  # метод, который добавляет елемент в конец списка
            cont_elem: int = long_word_.count(elem)
            # переменная, которая ссылается на целое число - количество данного элемента в кортеже
            print(f'{elem} - {cont_elem}', end=' ')  # встроенная функция, которая выводит в кансоль информацию


# DZ/ 3
def temperature(week_temp_: tuple) -> int:  # объявляем функцию с одним параметром, которая будет возвращать целое число
    days: int = len(week_temp_)  # переменная, которая ссылается на количество дней (количество данных о температуре)
    sum_temp: int = sum(week_temp_)  # переменная, которая ссылается на значение суммы всех температур в картеже
    mean_temp: float = sum_temp / days  # переменная, которая ссылается на значение средней температуры
    return int(mean_temp)  # функция, которая возвращает целое число


# 1
my_tuple: Tuple[int, ...] = tuple([int(input('Введите число: ')) for _ in range(1, 10)])  # переменная типа кортеж
print(duplicates(my_tuple))  # вызываем функцию и выводим в кансоль результат ее работы

# 2
my_set: Set[int] = set([int(input('Введите число для множества: ')) for _ in range(1, 10)])
# пеоеменная, которая ссылается на множество состоящее из целых чисел, которые вводятся с клавиатуры
my_frozenset: FrozenSet[int] = frozenset(
    [int(input('Введите число для неизменяемого множества: ')) for _ in range(1, 10)])
# переменная, которая ссылается на неизменяемое множетсво, которое вводитьяся с клавиатуры
print(f'Новое множество и пересечение из двух множеств - {work_with_set(my_set, my_frozenset)}')
# вызываем функцию и выводим в кансль результат ее работы

# DZ/1
tuple_2: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # переменная, которая ссылается на кортеж из целых чисел
print(f'Сумма элементов кортежа - {home_task_1(tuple_2)}')  # вызываем функцию и выводим результат ее работы в канслль

# DZ/2
long_word: Tuple[str, ...] = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и',
                              'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
# переменная, которая ссылается на кортеж состоящий из строк
home_task_2(long_word)  # вызываем функцию

# DZ/3
week_temp: Tuple[int, ...] = (26, 29, 34, 32, 28, 26, 23)
# переменная, которая ссылается на кортеж состоящий из целых чисел
print(f'Средняя температура - {temperature(week_temp)}')  # вызываем функцию и выводим результат ее работы в кансоль