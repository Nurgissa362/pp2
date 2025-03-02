#bultin-functions
import os
import time
import math
from functools import reduce

# Task 1: Multiply all numbers in a list
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4, 5]
print(multiply_list(numbers))  

# Task 2: Count uppercase and lowercase letters
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

s = "Hello World!"
print(count_case(s))  

# Task 3: Check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

s = "madam"
print(is_palindrome(s)) 

# Task 4: Square root after delay
def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

number, delay = 25100, 2123
print(f"Square root of {number} after {delay} milliseconds is {delayed_sqrt(number, delay)}")

# Task 5: Check if all tuple elements are true
def all_true(t):
    return all(t)

t = (True, True, False)
print(all_true(t))  

# Working with files
directory = "test_dir"
filename = "test_file.txt"

# Create directory if not exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Create and write to a file
with open(os.path.join(directory, filename), "w") as f:
    f.write("Hello, this is a test file.")

# Read from the file
with open(os.path.join(directory, filename), "r") as f:
    print(f.read())  # Example Output: "Hello, this is a test file."

# Delete file
os.remove(os.path.join(directory, filename))

# Remove directory
os.rmdir(directory)


#dir-and-files
import os

# 1. List only directories, only files, and both in a specified path
def list_contents(path):
    only_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    only_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_contents = os.listdir(path)
    return only_dirs, only_files, all_contents


path = '.'  
print("Directories:", list_contents(path)[0])
print("Files:", list_contents(path)[1])
print("All:", list_contents(path)[2])

# 2. Check access permissions of a specified path
def check_access(path):
    return {
        "Exists": os.path.exists(path),
        "Readable": os.access(path, os.R_OK),
        "Writable": os.access(path, os.W_OK),
        "Executable": os.access(path, os.X_OK)
    }


path = 'test.txt'  
print("Access:", check_access(path))

# 3. Check if a path exists and get filename and directory portion
def path_info(path):
    if os.path.exists(path):
        return {
            "Directory": os.path.dirname(path),
            "Filename": os.path.basename(path)
        }
    return "Path does not exist"


path = 'test.txt' 
print("Path Info:", path_info(path))

# 4. Count the number of lines in a text file
def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)


file_path = 'example.txt'  
print("Line Count:", count_lines(file_path))

# 5. Write a list to a file
def write_list_to_file(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(str(item) + '\n')

list_data = ["Apple", "Banana", "Cherry"]
file_path = 'output.txt'
write_list_to_file(file_path, list_data)
print(f"List written to {file_path}")

import os
import string
import shutil

# Task 6: Generate 26 text files named A.txt to Z.txt
def generate_text_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w') as f:
            f.write(f"This is file {filename}\n")

generate_text_files()

# Example:  
print(os.listdir())

# Task 7: Copy contents of one file to another
def copy_file(src, dest):
    if os.path.exists(src) and os.path.isfile(src):
        shutil.copy(src, dest)

copy_file("A.txt", "Copied_A.txt")

# Example: 
print(os.path.exists("Copied_A.txt"))

# Task 8: Delete a file by specified path after checking access
def delete_file(filepath):
    if os.path.exists(filepath) and os.path.isfile(filepath):
        if os.access(filepath, os.W_OK):
            os.remove(filepath)

delete_file("Copied_A.txt")

# Example: 
print(os.path.exists("Copied_A.txt"))


