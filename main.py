# fork this challenge to your own repl
#share this challenge with another person in the room.

#Day 3 Python Challenge

# The task is as follows: You are going to create a program that first asks the user to enter text. It can be any text, an entire article, a paragraph, a sentence, a poem, whatever you want. Then the program will ask the user to enter three random letters (we ask for three seperate letters). From that moment on, our code is going to process that information and result in five different types of analysis:

# 1. How many times each of those letters they have chosen appears. To achieve this, I advise you to store those letters in a list, and then use a method of strings that allows you to count how many times a substring appears within the string. One thing to keep in mind is that when searching for letters, there can be upper and lower case and this will affect the result. So, to make sure that absolutely all letters are counted, you should pass both the original text and the letters to be searched to lowercase.
# enter code here, don't forget to comment your ideas so you dont forget
# Beggining
paragraph1 = input("Enter any sentence: ")
print(paragraph1)
paragraph2 = input("Enter any sentence: ")
print(paragraph2)
paragraph3 = input("Enter any sentence: ")
print(paragraph3)
letter1 = input("Enter any letter: ")
print(letter1)
letter2 = input("Enter any letter: ")
print(letter2)
letter3 = input("Enter any letter: ")
print(letter3)

paragraph1l = paragraph1.lower()
paragraph2l = paragraph2.lower()
paragraph3l = paragraph3.lower()

# First Part
# use tuples:
print(paragraph1l.count(letter1))
print(paragraph1l.count(letter2))
print(paragraph1l.count(letter3))

print(paragraph2l.count(letter1))
print(paragraph2l.count(letter2))
print(paragraph2l.count(letter3))

print(paragraph3l.count(letter1))
print(paragraph3l.count(letter2))
print(paragraph3l.count(letter3))

# Making them lists
paragraphs = ['paragraph1l', 'paragraph2l', 'paragraph3l']

# 2. How many words are in the whole text? To achieve this part, remember that there is a string method that allows us to transform it into a list. And then there is a function that allows us to find out the length of a list.
# enter code here, don't forget to comment your ideas so you dont forget
# my_tuple = (paragraph1)
# print(my_tuple.count(" "))
print(len(paragraph1.split()))
print(len(paragraph2.split()))
print(len(paragraph3.split()))
print(len(letter1.split()))
print(len(letter2.split()))
print(len(letter3.split()))


# 3. What are the first and last letters of the text? Here, we will clearly use indexing.
# enter code here, don't forget to comment your ideas so you dont forget
# Notes "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
# first_letter = (paragraph1[:1:])
# print(first_letter)
# last_letter = (paragraph1[-2:-3:-1])
# print(last_letter)

# first_letter2 = (paragraph2[:1:])
# print(first_letter2)
# last_letter2 = (paragraph2[-2:-3:-1])
# print(last_letter2)

# first_letter3 = (paragraph3[:1:])
# print(first_letter3)
# last_letter3 = (paragraph3[-2:-3:-1])
# print(last_letter3)



# 4. The system will show us how the text would look like if we inverted the order of the words. Is there any method that allows us to invert the order of a list? And another one that allows us to join these elements with spaces in between?
# enter code here, don't forget to comment your ideas so you dont forget



# 5. The system will tell us if the word ???python??? is inside the text. This part can be a bit complicated to imagine, but I'll give you a hint: you can use Booleans to make your enquiry and a dictionary to find ways to express your answer.

# bool = 'paragraphs' = python
# print(bool)
