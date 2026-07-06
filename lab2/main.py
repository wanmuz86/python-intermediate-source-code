import utils

value = 20

print("Add:", utils.add(2, 3))
print("Multiply:", utils.multiply(4, 5))


# Both value are isolated

utils.show_value() # this should return 10
print("main value", value) # this should show 20


# Which style is more readable?

# Which style is safer in large projects?
# from module import method
# because we specify the directly the method needed
# just need to be careful with namespace collision
# use as to avoid it

# __dict__ property contains the metadata of the module
# at the bottom we can see the list of property and methods of the module
print(utils.__dict__)

# It return the name of the module = utils
print(utils.__name__)