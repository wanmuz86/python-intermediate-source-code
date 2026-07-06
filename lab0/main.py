# Lab 1  - recap (Installation + Hello)

# Declaring a variable of type String
# character, sentence or or wor

name = "Wan"
language = "Python"

print("Name: ", name)
print("Favourite language: ", language)


#Lab 3 - String operation

text = "Hello Python"

print(len(text)) # How many characters are there

# Retrieve character by inex
# Index start from 0
print(text[0]) # H
print(text[1]) # e

# Slicing character 
# From until but not including
print(text[0:5]) # From index 0 , until index 5 but not including index 5 " " => Hello

# Concatenation # Lab 3 - Step 5
first = "Hello"
second = "World"

result = first + " " + second
print(result)

# Spring formatting (f)
# Lab 4 - Step 4

age = 30

print(f"First name: {first}")
print(f"Last name: {second}") # The variable will be replaced automatically

print(f"Age is {age+10}")


# Number operation -  Lab 5 (simplified version)

num1 = 10
num2 = 3

sum = num1+num2
print(sum)

minus = num1-num2
print(minus)

division = num1/num2
print(division)

product = num1 * num2
print(product)

modulo = num1 % num2 # 10 divide by 3 - Remainder is 1
print(modulo)

powerOf = num1 ** num2  # 10^3
print(powerOf)

integerDiv = num1 // num2 
print(integerDiv)

# to transform String to number you use int() or float() # Lab 4,5 and 6
ageString = "30"
print(type(ageString)) #str

ageInt = int(ageString)
print(type(ageInt)) # int

# if elif else (Lab 7)

if age < 12:
    print("You are not allowed to watch the movie")
elif age >= 12 and age < 18: # and , or , not
    print("You are allowed to enter with parent")
    print("This is another line for example")
else:
    print("You are allowd to watch the movie")

# for loop - lab 9

for i in range(1,6): # From 1 until 5
    print(i)

for i in range(5,0,-1): # 3rd argument is the step
    print("*"*i)

# Print only the even number
for i in range(1,10):
    if i % 2 == 0:
        print(i)

# Lab 11 - function

# Defining a function
def add(a,b):
    return a+b

#Invoking/Calling a function
print(add(10,3))

# Lab 13 - Collection (List)
# More one items
# Best practice - list is plural
# small letter, plural, undercase
# student_names
# List is mutable

items = [1,2,3,4,5]  # A list with 5 items

print(len(items)) # (How many items are there) - 5

items.append(6) #Add an item at the end of the list
print(items)

# For loop to iterate the variable right away
for item in items:
    print(item)

# Extra info on Set - Lab 15
# More than one items but cannot be repeated
# union and inter method

# Dictionary - Lab 16
# Store using key, value
# Dictionary is mutable
info = {"name":"Wan","age":40,"profession":"Trainer"}

print(info["name"])
print(info["age"])
print(info["profession"])

print(f"My name is {info["name"]}, I am {info["age"]} years old and I am {info["profession"]}")

info["profession"] = "IT Consultant and Trainer"
print(info)  # The info is updated with the new profession
info["location"] = "Melaka"
print(info)

# Tuple
# Immutable collection (value cannot be changed once it is declared)

scores = (40,30,80,90,100) # Declaring a tuple (immutable)
print(scores[0])
print(scores[1])
print(scores[-1]) # Last one (usage in index)
print(scores[1:-1]) # Until second last (usage in slicing)
print(scores[1:]) # Until last (usage in slicing)
print(scores[:-1]) # From beginning (0) until second last 