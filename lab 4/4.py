#4th lab
#classes
#1


class StringHandler:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())


obj = StringHandler()
obj.getString()
obj.printString()

#2

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


sq = Square(5)
print(sq.area()) 


#3

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rect = Rectangle(4, 6)
print(rect.area()) 


#functions1
#1


def grams_to_ounces(grams):
    return 28.3495231 * grams


print(grams_to_ounces(100))  


#2

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


print(fahrenheit_to_celsius(100))  

#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return "No solution"


print(solve(35, 94))  


#functions2
#1

class Movie:
    def __init__(self, name, imdb, category):
        self.name = name
        self.imdb = imdb
        self.category = category

    def is_highly_rated(self):
        return self.imdb > 5.5

movie1 = Movie("Hitman", 6.3, "Action")
print(movie1.is_highly_rated())  


#2

class MovieDatabase:
    def __init__(self, movies):
        self.movies = [Movie(m["name"], m["imdb"], m["category"]) for m in movies]

    def highly_rated_movies(self):
        return list(filter(lambda movie: movie.is_highly_rated(), self.movies))


movies_data = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"}
]


db = MovieDatabase(movies_data)


print([movie.name for movie in db.highly_rated_movies()]) 


#3

class MovieDatabase:
    def __init__(self, movies):
        self.movies = [Movie(m["name"], m["imdb"], m["category"]) for m in movies]

    def movies_by_category(self, category):
        return list(filter(lambda movie: movie.category == category, self.movies))


print([movie.name for movie in db.movies_by_category("Romance")]) 