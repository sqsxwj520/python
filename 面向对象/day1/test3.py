import re

pattern = '[A-Za-z\d+/]{2,4}={0,2}'

regex = re.compile(pattern)

print(regex.fullmatch('YW=='))
print(regex.fullmatch('YW*='))
print(regex.fullmatch('=YW='))
