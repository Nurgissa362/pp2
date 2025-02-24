#1
def match_a_b(s):
    return bool(re.fullmatch(r'ab*', s))

#2
def match_a_b_2_3(s):
    return bool(re.fullmatch(r'ab{2,3}', s))

#3
def find_lower_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

#4
def find_upper_lower(s):
    return re.findall(r'\b[A-Z][a-z]*\b', s)

#5
def match_a_any_b(s):
    return bool(re.fullmatch(r'a.*b', s))

#6
import re

text = "Hello, how are you? I am fine. Thank you."
result = re.sub(r'[ ,.]', ':', text)
print(result)

#7
def snake_to_camel(s):
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

snake_str = "hello_world_example"
camel_str = snake_to_camel(snake_str)
print(camel_str)

#8
import re

text = "SplitAtUpperCaseLetters"
result = re.findall(r'[A-Z][a-z]*', text)
print(result)


#9
import re

def insert_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

text = "InsertSpacesBetweenWords"
result = insert_spaces(text)
print(result)

#10
import re

def camel_to_snake(s):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', s).lower()

camel_str = "CamelCaseToSnake"
snake_str = camel_to_snake(camel_str)
print(snake_str)


