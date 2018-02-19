""" Define a function which can print a dictionary
where the keys are numbers between 1 and 3 (both included)
and the values are square of keys. """

def create_dict():
    inp = int(input())
    for i in range(1,inp+1):
        d = dict()
        d[i] = i**2
        print (d)
create_dict()