fhand = open('/home/sumiru/Documents/Python_projects/Python_(freeCodeCamp)/poem.txt')

for line in fhand:
    line = line.rstrip()
    if not '?' in line:
        continue
    print(line)
