import math
import datetime
import random

# To call API / connect to server (Day 5)
# import requests 

# calling the sqrt method from math module -> bracket sqrt()
print(f"Square root of 25 {math.sqrt(25)}")

# calling the PI property/variable from math module -> no bracket math.pi
print(f"Value of PI is {math.pi}")

today = datetime.date.today() # method of date object
print(f"Today's date is {today}")

# Generate a random integer between 1 to 10
# random.random() -> generate random float between 0 and 1

print("Random number between 1 and 10: ", random.randint(1,10)) 
print(f"Random float between 0 and 1 {random.random()}")