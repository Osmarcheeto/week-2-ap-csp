
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
# greeting = "Hello"
# name = "World"

# # ----------------------------------------
# # Basic String Operations
# # ----------------------------------------

# # 1. Concatenation: Combining strings using the + operator
# message = greeting + " " + name
# print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
name =  "OSMAR"
# # # Convert all characters to lowercase
# # print("Lowercase:", phrase.lower())  # Output: python is fun!
# # print("lowercase:", name.lower())
# # # Convert all characters to uppercase
# # print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
# print("Uppercase name:", name.upper())
# print("Uppercase name:", name.capitalize())
# # # Check if all characters are uppercase
# print("Is Uppercase?", phrase.isupper())  # Output: False

# # # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14

# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------
chicago_mayor = "Johnson"
# # Indexing: Access characters by position (0-based index)clear
print("First character of mayor", chicago_mayor[0])
print("Last letter of mayor's name:", chicago_mayor[-1])
# print("First character:", phrase[0])  # Output: P
# print("Last character:", phrase[-1])  # Output: !
# get john
print("First four letters of mayors name:", chicago_mayor[0:7])
print("First 3 letters of Name is", name[0:3])
poppins = "supercalifragilisticexpialidocious"
print(poppins)
print("Uppercase", poppins.upper())
print("Print out super", poppins[0:5])
print("Print out docious", poppins[27:34])
print(len(poppins))
declaration_of_independece = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness." 
# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!

# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

# sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
# words = sentence.split()
# print("Split result:", words)

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)
