#date
#1
'''
from datetime import date , timedelta

current_date = date.today()
five_days_ago = current_date - timedelta(days=5)
print(current_date)
print (five_days_ago)
'''
#2
'''
from datetime import date,timedelta
todays_day = date.today()
yesterdays_day = date.today()
tomorrows_day = date.today()

print(yesterdays_day - timedelta(days=1))
print(todays_day)
print(tomorrows_day + timedelta(days=1))
'''

#3
'''
from datetime import datetime

current_datetime = datetime.now()
clean_datetime = current_datetime.replace(microsecond=0)

print(clean_datetime)
'''
4

from datetime import datetime

date1_str = input("Enter the first date : ")
date2_str = input("Enter the second date : ")


date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")


time_difference = abs((date2 - date1).total_seconds()) 


print(f"Difference between the two dates in seconds: {time_difference:.0f}")


#generators
#1 
'''
def square_generator(N):
    for num in range (N+1):
        yield num **2

n = int(input ("Enter a number N: "))

for num in square_generator(n):
    print(num)
'''
#2
'''
def even_numbers(n):
    for  num in range(n+1):
        if(num%2==0):
            yield num

n = int (input("Enter a number n: "))

print(",".join(str(num) for num in even_numbers(n)))
'''
#3
'''
def gen(n):
    for num in range (n+1):
        if num%3 == 0 and num%4 == 0:
            yield num

n = int(input ("Enter a number N: "))

for num in gen(n):
    print(num)
'''
#4
'''
def square_generator(a,b):
    for num in range (a,b+1):
        yield num **2

a = int(input ("Enter a number a: "))
b = int(input ("Enter a number b: "))

for num in square_generator(a,b):
    print(num)
'''
#5
'''
def gen(n):
    for num in range(n,-1,-1):
        yield num

num = int (input ("Enter a num: "))

for n in gen(num):
    print(n)
'''


#math
#1
'''
import math
value = int(input("Enter  degree: "))

converted_value = (value * math.pi)/180

print(f"Radians: {converted_value:.6f}")
'''
#2
'''
height = int(input ("Enter height: "))
base1 = int(input ("Enter 1 base: "))
base2 = int(input ("Enter 2 base: "))

area = ((base1+base2)/2)*height
print(f"Area_Of_Trapezoid: {area}")
'''
#3
'''
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

if n == 4:  
    area = s ** 2
else:
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area}")
'''
#4
'''
base = float(input ("Enter base: "))
length = float(input ("Enter length of side: "))
area = base * length
print (f"Area of the parrallelogram: {area}")
'''