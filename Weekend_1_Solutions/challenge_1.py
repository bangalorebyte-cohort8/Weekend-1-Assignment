"""
Challenge #1

Using the file "words.txt" in this repo, write a function that reads the words in words.txt
and stores them as keys in a dictionary. It doesn’t matter what the values are.
Use the 'in' operator to find if a word is in the dictionary.

"""

doc = open('words.txt') #Opening the file
word_list = [] #Creating an empty list

for word in doc: #for loop to iterate through lines in the file
    word = word.strip('\n') #stripping off white spaces
    word_list.append(word) #appending the words into our list
    
d = {} # The curly brackets, {}, represent an empty dictionary.
for i in word_list: #for loop to iterate line-by-line through the list
    d[i] = i # To add items to the dictionary, you can use square brackets.
print(d)

inp = (input("Enter the word to search in dictionary: ")) #taking user input to check word in dictionary
if inp in d.keys(): #checking the word in dictionary
    print("Word found:", inp) #printing the word if found
else:
    print("Word not found!") #printing message if the word is not found