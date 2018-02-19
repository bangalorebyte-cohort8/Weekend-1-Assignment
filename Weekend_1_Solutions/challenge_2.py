""" Define a function which can print a dictionary
where the keys are numbers between 1 and 3 (both included)
and the values are square of keys. """

def create_dict(): #function to create our dictionary
    inp = int(input("Enter a number: ")) #taking user inputs
    for i in range(1,inp+1): #for loop to iterate over the input
        d = dict() #creating empty dictionary
        d[i] = i**2 #adding iterated keys and the squared values to the dictionary
        print (d) #printing dicionary
create_dict() #calling function