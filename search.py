fhand = open('/home/sumiru/Documents/Python_projects/Python_(freeCodeCamp)/poem.txt')

for line in fhand:
    line = line.rstrip()
    print(line)