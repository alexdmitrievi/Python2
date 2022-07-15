#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.

from random import randrange
n = 10
a = [randrange(-n, n) for i in range(n)]
print(a)

f = open('file.txt', 'r') 
pro = 1
for line in f:
    pro = a[int(line)] * pro
print(pro)    