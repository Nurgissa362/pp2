import re

txt = 'wkgmwrgiugeoigajoijwfb'
x = re.search(r'a.*b', txt)  

if x:
    print("Match found:", x.group())
else:
    print("No match found")
