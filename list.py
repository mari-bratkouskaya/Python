<<<<<<< HEAD
# На вход программе подается одно число nn. Напишите программу, которая выводит список [1, 2, 3, ..., n].
=======
"""# На вход программе подается одно число nn. Напишите программу, которая выводит список [1, 2, 3, ..., n].
>>>>>>> c61738054c8c8dbacb23bbaff51e42cef408e5b7

n = int(input())
print(list(range(1, n+1)))

# На вход программе подается одно число nn. Напишите программу, которая выводит список, состоящий из nn букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

n = int(input())
abc = list(chr(i) for i in range(97, 97 + n))
print(abc)

# Дополните приведенный код, используя индексатор, так чтобы он вывел 17-ый элемент списка primes.

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])

# Дополните приведенный код, используя индексатор, так чтобы он вывел последний элемент списка primes.

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[-1])

# Дополните приведенный код, используя срезы, так чтобы он вывел первые 6 элементов списка primes.
# Примечание. Результатом вывода должна быть строка [2, 3, 5, 7, 11, 13].

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])

# Дополните приведенный код, так чтобы он вывел сумму минимального и максимального элементов списка numbers.

numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(min(numbers) + max(numbers))

# Дополните приведенный код так, чтобы он вывел среднее арифметическое элементов списка evens.

evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)

# Дополните приведенный код так, чтобы элемент списка имеющий значение Green заменился на значение Зеленый, а элемент Violet на Фиолетовый. Далее необходимо вывести полученный список.

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'
print(rainbow)

# Дополните приведенный код так, чтобы он вывел элементы списка languages в обратном порядке.
# Примечание. Для вывода списка воспользуйтесь функцией print().

languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])

# Дополните приведенный код, используя операторы конкатенации (+) и умножения списка на число (*), так чтобы он вывел список:
# [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13].

numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
numbers4 = list(numbers1*2 + numbers2*9 + numbers3)
print(numbers4)

# Дополните приведенный код, чтобы он:
# Вывел длину списка;
# Вывел последний элемент списка;
# Вывел список в обратном порядке (вспоминаем срезы);
# Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
# Вывел список с удаленным первым и последним элементами.
# Примечание. Каждый вывод осуществлять с новой строки.

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных строк список и выводит его.

n = int(input())
b = list()
for i in range(n):
    a = input()
    b.append(a)
print(b)

# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

abc = list((chr(i)*(i-96)) for i in range(97, 123))
print(abc)

# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.

n = int(input())
b = list()
for i in range(n):
    a = int(input())
    c = a**3
    b.append(c)
print(b)

# На вход программе подается натуральное число n. Напишите программу, которая создает список состоящий из делителей введенного числа.

n = int(input())
b = list()
for i in range(1, n+1):
    if n % i == 0:
        b.append(i)
print(b)

# На вход программе подается натуральное число n≥2, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1,1 и 2,2 и 3 и т.д.).

n = int(input())
b = list()
c = 0
for i in range(n):
    a = int(input())
    c += a
    b.append(c)
    c = a
print(b[1:])

# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

n = int(input())
b = list()
for i in range(n):
    a = int(input())
    b.append(a)
del b[1::2]
print(b)

# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
l = list()
for i in range(n):
    a = input()
    l.append(a)
k = int(input())
b = ''
for j in l:
    if len(j) >= k:
        b += j[k - 1]

print(b)

# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает список из символов всех строк, а затем выводит его.

n = int(input())
l = list()
for i in range(n):
    a = input()
    l.extend(a)

print(l)

# Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
counter = 0
for num in numbers:
    counter += num**2
print(counter)

# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого введенного числа x выводит значение функции f(x)=x2+2x+1, каждое на отдельной строке.

n = int(input())
list = []
for i in range(n):
    x = int(input())
    list.append(x)
print(*list, sep ='\n')
print()
for num in list:
    print((num + 1)**2, sep = '\n')

# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
# На вход программе подается натуральное число n, а затем n различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

n = int(input())
list = []
for i in range(n):
    x = int(input())
    list.append(x)
list.remove(min(list))
list.remove(max(list))
print(*list, sep = '\n')

# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

n = int(input())
list = []
for i in range(n):
    x = input()
    if x not in list:
        list.append(x)
print(*list, sep='\n')

# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

n = int(input())
list = []
for i in range(n):
    text = input()
    list.append(text)
find = input()
for j in list:
    if find.lower() in j.lower():
        print(j)

# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

n = int(input())
list = []
for i in range(n):
    num = int(input())
    list.append(num)
for j in list:
    if j < 0:
        print(j)
for a in list:
    if a == 0:
        print(a)
for z in list:
    if z > 0:
        print(z)

# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

s = input()
words = s.split()
print(*words, sep = '\n')

# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.

s = input().split()
for i in range(len(s)):
    print(s[i][0], end = '.')

# В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ  "\",  затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).
# На вход программе подается одна строка с корректным именем файла в операционной системе Windows. Напишите программу, которая разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.

s = input()
numbers = s.split('\\')
print(*numbers, sep = '\n')

# На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.

s = input().split()
for i in s:
    print(int(i)*'+')

# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.

s = input().split('.')
for i in s:
    if int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')

# На вход программе подается строка текста и строка разделитель. Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.

words = input()
s = input()
print(s.join(words))

# На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

s = input().split()
count = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            count += 1
print(count)

# Дополните приведенный код, чтобы он:
# Заменил второй элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print()

numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers += [4, 5, 6]
numbers.pop(0)
numbers *= 2
numbers.insert(3, 25)
print(numbers)

# На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

s = input().split()
s = [int(i) for i in s]
a = s.index(min(s))
b = s.index(max(s))
s[a], s[b] = s[b], s[a]
print(*s)

# На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

s = input().lower().split()
print('Общее количество артиклей:', s.count('a')+s.count('an')+s.count('the'))

# На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию. 

s = [int(i) for i in input().split()]
s.sort()
print(*s)
s.sort(reverse = True)
print(*s)

# Дополните приведенный код, используя списочное выражение так, чтобы получить новый список, содержащий строки исходного списка с удаленным первым символом.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i[1:] for i in keywords]
print(new_keywords)

# Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк исходного списка.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(i) for i in keywords]
print(lengths)

# Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i for i in keywords if len(i) >= 5]
print(new_keywords)

# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел палиндромов от 100 до 1000.

palindromes = [i for i in range(100, 1001) if i % 10 == i // 100]
print(palindromes)
<<<<<<< HEAD

# На вход программе подается натуральное число n. Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 1 до n, а затем выводит его элементы построчно, то есть каждый на отдельной строке.

squares = [i ** 2 for i in range(1, int(input())+1)]
print(*squares, sep = '\n')

# На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выведет кубы указанных чисел также на одной строке.

cubes = [int(i) ** 3 for i in input().split()]
print(*cubes)

# На вход программе подается строка текста, содержащая слова. Напишите программу, которая выводит слова введенной строки в столбик.

s = [i for i in input().split()]
print(*s, sep = '\n')

# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.

s = [i for i in input() if i in '0123456789']
print(*s, sep='')

# Оптимизируйте приведенный код, реализующий алгоритм пузырьковой сортировки.

a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
n = len(a)
flag = False

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = False
        else:
            flag = True
    if flag:
        break
print(a)
=======
"""
# На вход программе подается натуральное число n. Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 1 до n, а затем выводит его элементы построчно, то есть каждый на отдельной строке.

squares = [i ** 2 for i in range(int(input()))]
print(''.join(squares), sep='/n')

>>>>>>> c61738054c8c8dbacb23bbaff51e42cef408e5b7
