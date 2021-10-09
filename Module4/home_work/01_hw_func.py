# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
def lucky_ticket(ticket_number):
    # TODO: your code here

    pass
    num=str(ticket_number)
    sum1=int(num[0])+int(num[1])+int(num[2])
    sum2=int(num[3])+int(num[4])+int(num[5])
    if sum1 == sum2:
        result="+"
    else:
        result="-"
    return result

# Тест
print(lucky_ticket(123006))
print(lucky_ticket(912321))
print(lucky_ticket(436751))
