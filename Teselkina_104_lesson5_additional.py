from array import array

# 1
array_string = ['string1', 'string20', 'string300', 'string4000', 'string50000']  # массив состоящий из строк
print('Элементов в массиве ', len(array_string))  # вывод в кансоль значений
for i in array_string:  # для каждого элемента массива
    print('Длина слова', i, ' - ', len(i))  # вывод в кансоль текста и количества символов в строке
print()  # перевод на новую строку

# 2
array_2 = array('i', [1, 2, 3, 4, 5, 6, 7, -1, -5, -11, -3, -13, 1, 155, 16, 8188, -13])
# массив состоящий из целых чисел
for negative_digit in array_2:  # для каждого элемента в массиве
    if negative_digit < 0:  # условие: если элемент меньше 0
        print(negative_digit, 'Индекс первого вхождения этого числа ', array_2.index(negative_digit))  # вывод в кансоль
        break  # оператор, который досрочно прерывает цикл
for max_digit in array_2:  # для каждого элемента из массива
    if max_digit == max(array_2):  # если число = максимальному числу в массиве
        print('Максимальное число массива ', max_digit)  # вывод в кансоль максимального число
        break  # оператор, который досрочно прерывает цикл
for min_digit in array_2:  # для каждого элемента из массива
    if min_digit == min(array_2):  # условие: усли число = минимальному числу в массиве
        print('Минимальное число массива ', min_digit)  # вывод в кансоль
        break  # оператор, который досрочно прерывает цикл
print('Произведение максимального и минимального чмсел = ', max(array_2) * min(array_2))  # вывод в кансоль
print()

# 4
list_1 = ['Text', 0, 98, 'M', -45, 5.6, 'Hiiii)']  # лист состоящий из различных типов данных
print(f'Исходный массив {list_1}. \nНовый массив  {list_1[::-1]}')
# встроенная функция, которая выводит в кансоль текст, первый список и перевернутый список
