import re

# %%%%%%%%%% FIND METHOD %%%%%%%%%%%%%
hand = open('/home/sumiru/Documents/Python/poem.txt')
for line in hand:
    line = line.rstrip()
    if line.find('Remember') >= 0:
        print(line)


# %%%%%%%%%%% REGEX FUNCTION %%%%%%%%%%%%
print('-------------------------')

hand = open('/home/sumiru/Documents/Python/poem.txt')
for line in hand:
    line = line.rstrip()
    if re.search('Remember', line):
        print(line)