import re

x = 'We just received $10.00 for cookies.'
y = re.findall(r'\$[0-9.]+', x)
print(y)