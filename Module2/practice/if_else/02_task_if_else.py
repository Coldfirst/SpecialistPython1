# мое решение

  
# Дано целое число. Определить, заканчивается ли оно число цифрой 5?
# Формат входных данных: Целое положительно число
# Формат выходных данных: Если число оканчивается цифрой 5, вывести «YES», в противном случае — вывести «NO».

# TODO: your code here

number = int (input ("число "))
if number == 5:
	print ("заканчивается на 5")
elif number%10==5:
    print ("заканчивается на 5")
else:
    print ("не заканчивается на 5")
