#Реализуйте алгоритм перемешивания списка

from random import randrange

a = [0,1,2,3,4,5,6,7,8,9]
for i in range(9,-1,-1):
    tmp = a[i]
    r = randrange(0, i+1)
    a[i] = a[r]
    a[r] = tmp 
print(a)
    