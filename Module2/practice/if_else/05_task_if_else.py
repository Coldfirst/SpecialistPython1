# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here

# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here


n = int(input("Введите номер месяца"))
if n == 12 or 1 <= n <= 2:
    print("Зима")
elif 3 <= n <= 5:
    print("Весна")
elif 6 <= n <= 8:
    print("Лето")
elif 9 <= n <= 11:
    print("Осень")
else:
    print("Неправильное значение месяца")
