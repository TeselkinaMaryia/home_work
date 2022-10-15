from typing import Dict


# 4
def function(seconds: int):  # объявляем функцию с олним параметром
    def days() -> int:  # объявляем функцию без параметра которая буде возвращать число дней
        return seconds // (24 * 60 * 60)  # функция, которая возвращает число

    def hours() -> int: # объявляем функцию без параметра которая буде возвращать количество часов
        return (seconds - days() * (24 * 60 * 60)) // (60 * 60)  # функция, которая возвращает число

    def minuts() -> int:  # объявляем функцию без параметра которая буде возвращать количество минут
        return (seconds - days() * (24 * 60 * 60) - hours() * (60 * 60)) // 60  # функция, которая возвращает число

    def seconds_() -> int:  # объявляем функцию без параметра которая буде возвращать количество секунд
        return (seconds - days() * (24 * 60 * 60) - hours() * (60 * 60) - minuts() * 60) % 60

    print(f'{days()} дней, {hours()} часов, {minuts()} минут,{seconds_()} секунд')


seconds_ = int(input('Введите число секунд: '))  # переменная, которая ссылается на введенное с клавиатуры значение
function(seconds_)  # вызываем функцию
