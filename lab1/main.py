import my_utils

# calling the greet method from my_utils module
print(my_utils.greet("Hello Python Learner"))

#calling the add method from my_utils module
print("Sum: ", my_utils.add(3,5))

# What happens if my_utils.py is renamed?
# Rename the import and the called to the method

# What if it is moved to another folder?
# Follows sys.path resolution, it needs to be in the folder listed there

# What happens if you delete the __pycache__ folder?
# Does your program still run?
# No problem. code still run but take longer time
