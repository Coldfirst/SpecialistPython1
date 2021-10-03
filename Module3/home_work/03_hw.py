# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

#
# numbers = []
# # print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# # TODO: your code here
#
# cycle = int(input("Длина списка "))
# numbers = []
# import random
# i=1
# while i<=cycle:
#     numbers.append(random.randint(-100,100)) # значение от 0.0 до 1.0
#     i+=1
# print(numbers)
#          0   1  2  3    4    5
# numbers = [39, 3, 7, 67, -54, -48]
# i=0
# s=0
# while i<len (numbers):
#     el = numbers [i]
#     s+=el
#     i+=1
# print (s)

numbers = [39, 2, 7, 68, -54, -48]
s = 0
for el in numbers:
    if el>0 and el%2==0:
        s+=el

print (s)
