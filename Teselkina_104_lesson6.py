from array import array
import random

# 1
num = 1  # переменная, которая ссылается на значение 1
while num <= 10:  # цикл: пока число <= 10
    print(f'Квадрат числа {num} = ', num ** 2)
    # встроенная функция, которая выводит в кансоль текст и значение математической операции
    num += 1  # добавление к переменной 1

# 2
digit_ = 1  # Переменная, которая ссылается на значение 1
product = 1  # Переменная, которая ссылается на значение 0
while digit_ <= 125:  # цикл: пока число меньше или равно 125
    if digit_ % 2 == 0:  # условие: если число четное
        product *= digit_  # умножаем число на значение переменной
    digit_ += 1  # добавояем 1 к числу
print(f'Произведение всех четных чисел от 0 до 125 = {product}')  # вывод в кансоль

# 3
digit_1 = 15  # переменная, которая ссылается на значение 1
while digit_1 >= 1:  # цикл: пока число больше или равно 1
    print('\t' * (15 - digit_1), digit_1)  # Вывод в кансоль числа
    digit_1 -= 1  # прибавляем 1 к числу

# 4.1
num_1 = int(input('Введите начало диапазона: '))  # переменная. которая ссылается на вводимое с клавиатуры значение
num_2 = int(input('Введите окончание диапахона: '))  # переменная. которая ссылается на вводимое с клавиатуры значение
list_ = []  # переменная типа список
while num_1 or num_2 < 0:  # цикл: пока 1 или 2 число, вводимые с клавиатуры меньше 0
    for i in range(num_1, num_2):  # цикл: для каждого значения в диапазоне
        if i < 0:  # условие: если число отрицательное
            list_.append(i)  # добавление значения в конец списка
    break  # досрочно прерывает цикл
print(*list_, sep=',')  # вывод в кансоль

# 4.2
digit_1 = int(input('Введите целое число: '))  # Переменная, которая ссылается на вводимое с клавиатуры значение
digit_2 = int(input('Введите второе целое число: '))  # Переменная, которая ссылается на вводимое с клавиатуры значение
while digit_1 < digit_2 and digit_1 < 0:  # цикл: пока первое число меньше второго и меньше 0
    print(digit_1, end=',')  # Вывод в кансоль
    digit_1 += 1  # добавление 1 к значению числа

# 5
digit_3 = 1  # переменная, которая ссылается на значение 1
list_1 = []  # переменная типа список
while digit_3 <= 100:  # цикл: пока число меньше 100
    if digit_3 % 7 == 0:  # условие: если число кратно 7
        list_1.append(digit_3)  # добавляем число в конец списка
    digit_3 += 1  # прибавляем к числу 1
print(f"""
        Последовательность чисел от 1 до 100 кратных 7 - {list_1}.'
        Длина полученного списка - {len(list_1)}
        """)  # вывод в кансоль

# 6
float_num_1 = float(input('Введите вещественное число: '))
# переменная, которая ссылается на вводимое с клавиатуры вещественное число
float_num_2 = float(input('Введите второе вещественное число: '))
# переменная, которая ссылается на вводимое с клавиатуры вещественное число
operation = input('Введите операцию (+, -, *, /): ')  # переменная, которая ссылается на вводимую операцию
while True:  # цикл: пока истина
    if float_num_1 == 0:  # условие: если введен 0
        break  # досрочно прерывает цикл
    elif operation == '+':  # условие: если введен конкретный знак операции
        print(f'{float_num_1} + {float_num_2} = ', float_num_1 + float_num_2)  # вывод в кансоль
    elif operation == '-':  # условие: если введен конкретный знак операции
        print(f'{float_num_1} - {float_num_2} = ', float_num_1 - float_num_2)  # вывод в кансоль
    elif operation == '*':  # условие: если введен конкретный знак операции
        print(f'{float_num_1} * {float_num_2} = ', float_num_1 * float_num_2)  # вывод в кансоль
    elif operation == '/':  # условие: если введен конкретный знак операции
        if float_num_2 != 0:  # условие: если второе чило не равно 0
            print(f'{float_num_1} / {float_num_2} = ', float_num_1 / float_num_2)  # вывод в кансоль
        else:
            print('Ошибка!!!! Деление на 0')  # вывод в кансоль
    break  # досрочно прерывает цикл

# 7.1
arr_ = array('i', [12, 13, 16, 19, 76, 75, 47, 388595, 7676, 7575894, 778595, 2774890, 22, 8583, 8994, 38993, 28939])
# массив состоящий из целых чисел
sum_even = 0
count_even = 0
count_odd = 0
for num_arr in arr_:  # для каждого элемента в массиве
    if num_arr % 2 == 0:  # условие: если элемент - четное число
        count_even += 1  # +1 к значению переменной (отображает количество четных чисел)
        sum_even += num_arr  # + значение числа к переменной
    elif num_arr % 2 != 0:  # условие: если элемент - нечетное число
        count_odd += 1  # + 1 к значению переменной (количество нечетных чисел)

    if num_arr == arr_[-1]:  # если мы доходим до последнего числа массива
        if count_even > count_odd:  # если количество четных чисел больше количества нечетных в массиве
            print('Сумма всех четных чисел массива', sum_even)  # вывод в кансоль

        elif count_even < count_odd:  # условие: если количество четных чисел меньше количества четных
            print('Произведение 13 и 6 чисел массива', arr_[12] * arr_[5])  # вывод в кансоль
        else:  # если ни одно условие не является истинным
            print('Четных и нечетных чисел в массиве поровну')  # вывод в кансоль

# 7.2
arr_1 = array('i', [113, 13, 1435, 19, 76, 75, 47, 3885, 7676, 757894, 778, 277480, 2209, 858, 894, 38, 289, 1478, 10])
# массив состоящий из целых чисел
count_operation = 1
sum_even_1 = 0
count_even_1 = 0
count_odd_1 = 0

while count_operation <= len(arr_1):
    # пока количество операций меньше или равно значению количества элементов в массиве
    if arr_1[count_operation - 1] % 2 == 0:
        # условие: если элемент в массиве с индексом = количество операций - 1 делится на 2 без остатка
        count_even_1 += 1  # +1 к значению переменной (отображает количество четных чисел)
        sum_even_1 += arr_1[count_operation - 1]  # +значение элемента к переменной
    elif arr_1[count_operation - 1] % 2 != 0:  # условие: если элемент - нечетное число
        count_odd_1 += 1  # +1 к значению переменной (отображает количество нечетных чисел)

    if arr_1[count_operation - 1] == arr_1[-1]:  # условие: если элемент - последнее число массива
        if count_even_1 > count_odd_1:  # условие: если количество четных чисел больше количества нечетных
            print('Сумма всех четных чисел массива', sum_even_1)  # вывод в кансоль
        elif count_even_1 < count_odd_1:  # условие: если количества четных чисел меньше количесьва нечетных
            print('Произведение 13 и 6 чисел массива', arr_1[12] * arr_1[5])  # вывод в кансоль
        else:  # если ни одно условие не является верным
            print('Четных и нечетных чисел в массиве поровну')  # вывод в кансоль
    count_operation += 1  # +1 к значению переменной (отображает количество операций)

# домашняя работа

count_try = 1  # переменная, которая ссылается на значение 1 (номер попытки)
number = random.randint(1, 10)  # компьютер рандомно выбирает значение от 1 до 10 и записывает это число в переменную
color_digit = random.randint(1, 2)  # в переменную записывается число, которое выбрал компьютер
if color_digit == 1:  # условие: переменная = 1
    color_color = 'красный'  # переменной присваивается значение - красный
else:  # если условие не верное
    color_color = 'черный'  # переменной присваивается значение - черный

while count_try <= 5:  # цикл: пока поременная (количество попыток) меньше или равно 5

    try_1 = input('Введите номер от 1 до 10 и цвет (красный/ черный): ')
    # переменная, которая ссылается на значение введенное с клавиатуры
    if try_1[:try_1.find(' ')] == str(number) and try_1[try_1.find(' ') + 1:] == color_color:
        # условие: если первый элемент строки (число) совпадает с тем, что выбрал компьютер
        # и подстрока, которая начинается после пробела и заканчивается в конце = слову записанную в переменную
        print('You win!')  # Вывод в кансоль
        break  # досрочно прерывает цикл
    else:  # если условие не выполняется
        print('Try again')  # вывод в кансоль

    if count_try == 5:  # условие: если переменная (количество попыток) = 5
        print(f'Computer choose: {number} {color_color}')  # вывод в кансоль то, что загадал компьютер

    count_try += 1  # прибавляем 1 к переменной