# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

#names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here




# TODO: your code here

# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "ИринаИринаИрина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
longest=names[0]
for name in names:
    if len (name) > len (longest):
        longest = name

print (longest)
