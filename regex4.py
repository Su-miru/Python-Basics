import re

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall(r'\S+@\S+', x)
print(y)

y = re.findall(r'^From (\S+@\S+)', x)
print(y)