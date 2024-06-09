import re

# %%%%%%%%%%%% STARTSWITH METHOD %%%%%%%%%%%%%
hand = open('/home/sumiru/Documents/Python/poem.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('A'):
        print(line)

# %%%%%%%%%%%% REGEX %%%%%%%%%%%%%%%
print('------------------')

hand = open('/home/sumiru/Documents/Python/poem.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^A', line):
        print(line)