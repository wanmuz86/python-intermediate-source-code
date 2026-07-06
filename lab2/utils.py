#The variable that we create here
# isolated from the one created in main.py
value = 10

def add(a, b):
    return a + b +100

def multiply(a, b):
    return a * b

def show_value():
    print("utils value: ", value)

# Why is reload useful in development?
# The module can be reloaded automatically without wasting time

# Why is restarting the program safer in production?
# To ensure all change is reloaded
