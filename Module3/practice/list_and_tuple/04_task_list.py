# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here


numbers = [-10, 2, 7, -2, 5, 3]
s = 0
for el in numbers:
    if el>0:
        s+=el

print (s)
