# Задание 1
Anna_apple = 2  # первая переменная
Pol_apple = 5  # вторая переменная
print('У Пола ', Pol_apple, 'яблок.',
      '\nУ Анны', Anna_apple, 'яблока.')  # вывод переменных в кансоль

# Задание 2
cub_edge = float(input('Введите длину ребра куба в см: '))  # Функция для ввода длины ребра с клавиатуры
print('Объем куба = ', cub_edge ** 3, 'см3',
      '\nПлощадь боковой поверхности куба = ', 4 * cub_edge ** 2, 'см2')  # вывод в кансоль вычислинных значений

# Задание 3
tree = 20  # переменная характеризующая высоту дерева
speed_day = 2  # сколько метров улитка проползает за день
speed_night = 1  # на сколько метров улитка спускается за ночь
print('Улитка взобралась на дерево за ', tree / (speed_day - speed_night) - 1,
      'дней')  # вывод в кансоль за сколько дней улитка проползет 20 метров
