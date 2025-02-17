#4th lab
#date
#1
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print(new_date.date())




#2
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)



#3
from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 0, 0)
date2 = datetime(2024, 2, 12, 14, 30, 0)

difference = (date2 - date1).total_seconds()
print(difference)


#4
from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 0, 0)
date2 = datetime(2024, 2, 12, 14, 30, 0)

difference = (date2 - date1).total_seconds()
print(difference)





#generators
#1
def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2

for num in generate_squares(5):
    print(num)


#2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter n: "))
print(",".join(map(str, even_numbers(n))))




#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(50):
    print(num)



#4

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for num in squares(3, 7):
    print(num)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i


for num in countdown(5):
    print(num)



#math
#1
import math

def degree_to_radian(degree):
    return round(degree * (math.pi / 180), 6)

print(degree_to_radian(15)) 


#2
def trapezoid_area(height, base1, base2):
    return ((base1 + base2) * height) / 2

print(trapezoid_area(5, 5, 6))  


 #3
import math

def polygon_area(sides, length):
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))

print(polygon_area(4, 25)) 


#4
def parallelogram_area(base, height):
    return base * height
print(parallelogram_area(5, 6))  
