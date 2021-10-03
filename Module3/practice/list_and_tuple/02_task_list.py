# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

# TODO: your code here


# fruits = ["яблоко", "банан", "киви", "ананас", "груша"]
#
# # TODO: your code here
# a=1
# for e in fruits:
#         print (a,e)
#         a+=1

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

for number, fruit in enumerate(fruits, 1):
        print(number, fruit)
