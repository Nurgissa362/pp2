# Classes
# 1.

class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Введите строку: ")

    def printString(self):
        print(self.text.upper())


string_obj = StringManipulator()
string_obj.getString()
string_obj.printString()

# 2 - task


class Shape:
    def area(self):
        return 0 

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2  


square_obj = Square(5)
print(square_obj.area()) 

#3 - task

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  

rectangle_obj = Rectangle(4, 6)
print(rectangle_obj.area())  

#4-task

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


p1 = Point(2, 3)
p2 = Point(5, 7)
p1.show()
print(f"Distance: {p1.dist(p2)}")
p1.move(4, 6)
p1.show()

#5-task

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")


acc = Account("John Doe", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)  

#6-task

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 17, 19, 23, 24, 29, 33, 37]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)


#functions1

#1
def grams_to_ounces(grams):
    return 28.3495231 * grams


print(grams_to_ounces(100))  

#2
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)


print(fahrenheit_to_celsius(100))  

#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "No solution"


print(solve(35, 94)) 

#4
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))


print(filter_prime([10, 15, 17, 19, 23, 24, 29, 33, 37]))

#5
from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))


print_permutations("abc")

#6
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])


print(reverse_sentence("We are ready")) 

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3])) 
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))  

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


print(spy_game([1,2,4,0,0,7,5]))  
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  

#9
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3


print(sphere_volume(5))  


#10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


print(unique_elements([1, 2, 2, 3, 4, 4, 5]))

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


print(is_palindrome("madam"))  
print(is_palindrome("hello")) 
print(is_palindrome("racecar"))  

#12

def histogram(lst):
    for num in lst:
        print('*' * num)


histogram([4, 9, 7])

#13
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


#14
from task_module import grams_to_ounces, fahrenheit_to_celsius, solve, filter_prime

print(grams_to_ounces(50))
print(fahrenheit_to_celsius(100))
print(solve(35, 94))
print(filter_prime([10, 15, 17, 19, 23, 24, 29, 33, 37]))


#functions2

#1
def is_highly_rated(movie):
    return movie["imdb"] > 5.5


print(is_highly_rated({"name": "Hitman", "imdb": 6.3, "category": "Action"}))  
print(is_highly_rated({"name": "AlphaJet", "imdb": 3.2, "category": "War"}))  

#2
def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

print(high_rated_movies(movies))

#3
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]


print(movies_by_category(movies, "Romance"))

#4
def average_imdb(movies):
    if not movies:
        return 0 
    return sum(movie["imdb"] for movie in movies) / len(movies)


print(average_imdb(movies))

#5
def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)


print(average_imdb_by_category(movies, "Romance"))









