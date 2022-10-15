from typing import Dict


# 4
def function(seconds: int):  # объявляем функцию с олним параметром
    def days() -> int:  # объявляем функцию без параметра которая буде возвращать число дней
        return seconds // (24 * 60 * 60)  # функция, которая возвращает число

    def hours() -> int:  # объявляем функцию без параметра которая буде возвращать количество часов
        return (seconds - days() * (24 * 60 * 60)) // (60 * 60)  # функция, которая возвращает число

    def minuts() -> int:  # объявляем функцию без параметра которая буде возвращать количество минут
        return (seconds - days() * (24 * 60 * 60) - hours() * (60 * 60)) // 60  # функция, которая возвращает число

    def seconds_() -> int:  # объявляем функцию без параметра которая буде возвращать количество секунд
        return (seconds - days() * (24 * 60 * 60) - hours() * (60 * 60) - minuts() * 60) % 60

    print(f'{days()} дней, {hours()} часов, {minuts()} минут,{seconds_()} секунд')


# 5
def count_letters(string: str):  # объявляем функцию с одним параметром
    def count_vowels() -> int:  # объявляем функцию без параметра, которая возвращает число
        vowels = 0  # переменная, которая ссылается на 0
        for letter in string:  # цикл: для каждой буквы в слове
            if letter in ['a', 'e', 'y', 'u', 'i', 'o']:  # если буква в данном списке
                vowels += 1  # добавляем 1 к значению переменной
        return vowels  # функция, которая возвращает количество гласных

    def count_consonants() -> int:  # объявляем функцию без параметра, которая возвращает число
        consonants = 0  # переменная, которая ссылается на 0
        for letter in string:  # цикл: для каждой буквы в слове
            if letter not in ['a', 'e', 'y', 'u', 'i', 'o']:  # если буква не в списке
                consonants += 1  # добавляем 1 к значению переменной
        return consonants  # функция, которая возвращает количество согласных

    print(f'Количество гласных в {string} - {count_vowels()}, а согласных - {count_consonants()}')


# 6
def sum_(num: int):  # объявляем функцию с одним параметром
    num_1: int = num  # переменная, которая ссылается на число
    num_2: int = int(str(num) * 2)  # переменная, котрая ссылается на удвоенное число
    num_3: int = int(str(num) * 3)  # переменная, которая ссылается на утроенное число
    print(f'{num_1} + {num_2} + {num_3} = {num_1 + num_2 + num_3}')  # вывод в кансоль


# 7
def math_(x_: int) -> int:  # объявляем функцию с одним параметром, которая возвращает число
    if -5 <= x <= 5:  # условие
        y: int = x ** 2  # переменная, которая ссылается на значение вычисленное в уравнении
        return y  # функция, которая возвращает число
    elif x < -5:  # альтернативное условие
        y: int = 2 * abs(x) - 1  # переменная, которая ссылается на число
        return y  # функция, которая возвращает число
    elif x > 5:  # альтернативное условие
        y: int = 2 * x
        return y


# 4
seconds_: int = int(input('Введите число секунд: '))  # переменная, которая ссылается на введенное с клавиатуры значение
function(seconds_)  # вызываем функцию

# 5
string_: str = input('Введите слово: ')  # переменная, которая ссылается на вводимое с клавиатуры слово
count_letters(string_)  # вызываем функцию и передаем ей один аргумент

# 6
num_: int = int(input('Введите число: '))  # переменная, которая ссылается на вводимое с клавиатуры число
sum_(num_)  # вызываем функцию

# 7
for x in range(-10, 11):  # цикл: для каждого числа в последовательности от -10 до 10
    print(math_(x))  # вывод в кансоль работы функции
