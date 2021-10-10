# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    pass


def palindrome(number):
    our_number = str(number)
    return our_number == our_number[::-1]

# Тестируем функцию
print(palindrome(1234))
print(palindrome(3443))
print(palindrome(1))
