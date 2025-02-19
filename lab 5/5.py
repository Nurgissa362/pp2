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
