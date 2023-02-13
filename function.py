# Функции
# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10

print('*' * 10, sep='')
def draw_box():
    for _ in range(14-2):
        print('*', ' '*8, '*', sep = '')
draw_box()
print('*' * 10, sep='')

# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10

def draw_triangle():
    for i in range(1, 11):
        print('*' * i, sep = '')
draw_triangle()

# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.


def draw_triangle(fill, base):
    for i in range(base//2+1):
        for _ in range(i+1):
            print(fill, end='')
        print()
    for j in range(base//2, 0, -1):
        for _ in range(j):
            print(fill, end='')
        print()
fill = input()
base = int(input())
draw_triangle(fill, base)

# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.

def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep='')
name, surname, patronymic = input().upper(), input().upper(), input().upper()
print_fio(name, surname, patronymic)

# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

def print_digit_sum(num):
    sum = 0
    while num != 0:
        last_digit = num % 10
        num = num // 10
        sum += last_digit
    print(sum)
n = int(input())
print_digit_sum(n)

# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях. Формула для преобразования: мили = километры * 0.6214.

def convert_to_miles(km):
    ml = km * 0.6214
    return ml

num = int(input())
print(convert_to_miles(num))

# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

def get_days(month):
    if month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

num = int(input())
print(get_days(num))

# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

def get_factors(num):
    b = list()
    for i in range(1, num+1):
        if num % i == 0:
            b.append(i)
    return b

n = int(input())
print(get_factors(n))

# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

def number_of_factors(num):
    b = list()
    for i in range(1, num+1):
        if num % i == 0:
            b.append(i)
    return len(b)

n = int(input())
print(number_of_factors(n))

# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

def find_all(target, symbol):
    b = list()
    for i in range(len(target)):
        if target[i] == symbol:
            b.append(i)
    return b
s = input()
char = input()
print(find_all(s, char))

# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.

def merge(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))

# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.

def is_valid_triangle(side1, side2, side3):
    if side1 < (side2 + side3) and side2 < (side1 + side3) and side3 < (side1 + side2):
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))

# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.

def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        return True
    else:
        return False

num = int(input())
print(is_prime(num))