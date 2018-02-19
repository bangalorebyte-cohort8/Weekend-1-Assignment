"""You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are numbers.

The sort criteria is:

1: Sort based on name; 2: Then sort based on age; 3: Then sort by score.

The priority is that name > age > score."""

l = list()

while True:

    inp = input('>')
    if not inp :
        break
    inp = inp.replace(' ', '')
    inp = inp.split(',')
    t = tuple(inp)
    l.append(t)
    l = sorted(l)
    
print(l)