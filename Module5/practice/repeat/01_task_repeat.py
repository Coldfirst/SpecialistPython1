# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    pass



def gen_list(size=10, of=1, to=19):
    import random
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(of, to))
    return result_list
print (gen_list())
