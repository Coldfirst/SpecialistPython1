# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here


# TODO: your code here
cycle = int(input("Длина списка "))
numbers = []
import random
i=1
while i<=cycle:
    numbers.append(random.randint(-100,100)) # значение от 0.0 до 1.0
    i+=1
print(numbers)
