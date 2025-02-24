import re

#1.
def match_a_b(s):
    return bool(re.fullmatch(r'ab*', s))

print(match_a_b("a"))  #True
print(match_a_b("abbb"))  #True
print(match_a_b("b"))  #False

#2. 
def match_a_b_2_3(s):
    return bool(re.fullmatch(r'ab{2,3}', s))

print(match_a_b_2_3("abb"))  #True
print(match_a_b_2_3("abbb"))  #True
print(match_a_b_2_3("abbbb"))  #False

#3.
def find_lower_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

print(find_lower_underscore("hello_world test_text example_case"))

#4. 

def find_upper_lower(s):
    return re.findall(r'\b[A-Z][a-z]*\b', s)

print(find_upper_lower("Hello World From Python"))

#5. 
def match_a_any_b(s):
    return bool(re.fullmatch(r'a.*b', s))

print(match_a_any_b("acb"))  #True
print(match_a_any_b("a123b"))  #True
print(match_a_any_b("abc"))  #False

#6. 
text = "Hello, how are you? I am fine. Thank you."
result = re.sub(r'[ ,.]', ':', text)
print(result)

#7. 
def snake_to_camel(s):
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

print(snake_to_camel("hello_world_example"))

#8. 
text = "SplitAtUpperCaseLetters"
print(re.findall(r'[A-Z][a-z]*', text))

#9. 
def insert_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

print(insert_spaces("InsertSpacesBetweenWords"))

#10. 
def camel_to_snake(s):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', s).lower()

print(camel_to_snake("CamelCaseToSnake"))
