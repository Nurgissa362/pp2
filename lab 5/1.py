import re

pattern = r"a+b*"  # "a" должно быть обязательно, "b" может быть ноль или более раз
text = input("Введите строку: ")  # Позволяет вводить текст

match = re.search(pattern, text)

if match:
    print("Совпадение найдено:", match.group())
else:
    print("Совпадение не найдено")
