import os
from string import ascii_uppercase

#task 1
import os

# Указываем путь к папке (замени на свой при необходимости)
location1 = r'C:\pp2\lab 6'

# Вывод всех элементов (файлы и папки)
print("Все элементы:", [name for name in os.listdir(location1)])

# Вывод только папок (каталогов)
print("Только каталоги:", [name for name in os.listdir(location1) if os.path.isdir(os.path.join(location1, name))])

# Вывод только файлов
print("Только файлы:", [name for name in os.listdir(location1) if not os.path.isdir(os.path.join(location1, name))])



import os

path = r'C:\pp2\lab 6'  # Указываем правильный путь

print('Path exists:', os.access(path, os.F_OK))      # Проверка существования
print('Path readable:', os.access(path, os.R_OK))    # Проверка на чтение
print('Path writable:', os.access(path, os.W_OK))    # Проверка на запись
print('Path executable:', os.access(path, os.X_OK))  # Проверка на выполнение

import os

path = input('Insert path \n')

if not os.access(path, os.F_OK):
    print("Path does not exist")
else:
    print("Directory part:", os.path.dirname(path))
    print("File name part:", os.path.basename(path))
    print("Directories:", ', '.join([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]))
    print("Files:", ', '.join([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]))

#task 4 

path = r"C:\pp2\lab 6\file.txt"
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as file:
        x = len(file.readlines())
        print("Number of lines:", x)
else:
    print("Файл не найден!")




#task 5

mylist = ['A', 'B', 'C', 'D']
with open(r'C:\pp2\lab 6\file2.txt', 'w', encoding='utf-8') as file:
    for i in mylist:
        file.write(i + '\n')
print("Список успешно записан в файл.")



#task 6

import string
import os

# Указываем путь к папке
folder_path = r"C:\pp2\lab 6"

# Проверяем, существует ли папка, если нет — создаем
os.makedirs(folder_path, exist_ok=True)

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_path = os.path.join(folder_path, f"{letter}.txt")
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(f"This is the file {letter}.txt")
    print("Файлы успешно созданы в:", folder_path)

generate_text_files()


#task 7

with open(r'C:\pp2\lab 6\file.txt', 'r') as file1, open(r'C:\pp2\lab 6\filee.txt', 'a') as file2:
    for line in file1:
        file2.write(line)


#task 8

import os

path = r'C:\pp2\lab 6\file.txt'  # Путь к файлу

if os.access(path, os.F_OK):  # Проверяем, существует ли файл
    os.remove(path)  # Удаляем файл
    print("Файл был удалён.")
else:
    print("Файл не найден.")
