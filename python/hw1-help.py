Написать программу, которая выводит на экран все четные числа в диапазоне от 0 до заданного пользователем числа.

```python
n = int(input("Введите число: "))

for i in range(0, n+1, 2):
    print(i)
```



Написать программу калькулятор, которая позволяет пользователю выполнять арифметические операции (+, -, *, /) над двумя заданными числами.

```python
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '*':
    res = a * b
elif op == '/':
    res = a / b
else:
    print("Ошибка: неверная операция!")

print("Результат: ", res)
```



Написать программу, которая находит максимальное число из трех заданных пользователем чисел.

```python
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

max = a

if b > max:
    max = b

if c > max:
    max = c

print("Максимальное число: ", max)
```



Написать программу, которая проверяет, есть ли заданное пользователем число в заданном списке.

```python
n = int(input("Введите число: "))
lst = [1, 2, 3, 4, 5]

if n in lst:
    print("Число найдено в списке!")
else:
    print("Число не найдено в списке!")
```



Написать программу, которая конвертирует температуру в градусах Цельсия в температуру в градусах Фаренгейта.

```python
c = float(input("Введите температуру в градусах Цельсия: "))

f = 9/5 * c + 32

print("Температура в градусах Фаренгейта: ", f)
```



Написать программу, которая принимает строку от пользователя и выводит на экран каждый символ строки в отдельной строке.

```python
s = input("Введите строку: ")

for c in s:
    print(c)
```



Написать программу, которая считывает содержимое текстового файла и выводит его на экран.

```python
filename = input("Введите имя файла: ")
f = open(filename, 'r')
content = f.read()
print(content)
f.close()