#4
import re

txt = 'WFIWFNWFRRDoerjoiernwif'
x = re.findall('[A-Z]{1}[a-z]+', txt)
print(x)
