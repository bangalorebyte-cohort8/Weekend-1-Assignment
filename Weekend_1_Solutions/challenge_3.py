"""You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are numbers.

The sort criteria is:

1: Sort based on name; 2: Then sort based on age; 3: Then sort by score.

The priority is that name > age > score."""

l = list() #creating empty list

while True: #while loop to take continous input

    inp = input('>')
    if not inp : #if no input then break
        break
    inp = inp.replace(' ', '') #replacing white spaces
    inp = inp.split(',') #spliting the input
    #print(inp) # After spliting we get list
    inp[1] = int(inp[1]) #converting the string to int on index 1
    inp[2] = int(inp[2]) #converting the string to int on index 2
    t = tuple(inp) #storing the values in tuple
    l.append(t) #appending tuples to list
    l = sorted(l) #sorting the tuples
    
print(l)