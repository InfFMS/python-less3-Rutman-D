# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
from math import sqrt
x = int(input())
m = 0
M = 0
n = 0

while x != 0:
    for i in range(x):
        if x == 2**i:
            M+=x
            m+=1
            break
    #print(m, M)
    x = int(input())

if M != 0:
    n = M/m
    print(n)
else:
    print("Нет")
