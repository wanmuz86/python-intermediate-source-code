# Lab 2 Day 3 and 4 Document

# Create a new function decorator
#  Accept func as argument
# Needs to return func

# Decorator name is @log_call
def log_call(func):

    # To indicate this is a decorator
    def wrapper(*args, **kwargs): # argument in decorator
        
        # Before executing the function
        print(f"[LOG]: Calling {func.__name__}")
        
        print(f"[LOG]: Argment passed {args}")
        
        # Execute the function
        result = func(*args, **kwargs)

        # After function execution
        print(f"[LOG] Finished {func.__name__}")
        # return the result of function
        return result
    return wrapper

@log_call
def greet(name):
    print(f"Hello {name}")

class Calculator:
    @log_call
    def add(self, a,b):
        return a+b

    @log_call
    def multiply(self, a,b):
        return a*b

class BadCounter:
    history = [] #history list (class variable - shareable between instance)

    def add(self, value):
        self.history.append(value)

class GoodCounter:
    def __init__(self):
        self.history = [] # Unique per instance
    
    def add(self,value):
        self.history.append(value)


def main():
    print("\n-- FUnction Decorator Test--")
    greet("Aina")

    print("\n-- Method Decorator Test--")
    
    calc = Calculator()
    print("Add: ", calc.add(2,3))
    print("Multiply: ",calc.multiply(4,5))

    print("\n-- Class attribute side_effect()--")

    a = BadCounter()
    b = BadCounter()

    a.add(1)
    a.add(2)
    
    # Observe that both a and b will have the same histories, 
    # due to sharing the same class property/variable
    print("a.history ", a.history)
    print("b.history ", b.history) # Unexpected shared of data

    a1 = GoodCounter()
    b1 = GoodCounter()
    a1.add(10)
    a1.add(20)
    print("a1 history ", a1.history)
    print("b1 history ", b1.history)

# Why did b.history change even though we never modified it?
# Because we are declaring history as class property instead of instance property

# Where is history actually stored?
# It is stored in the class, not instance

# How many history lists exist in memory?
# 1 and shareable between all instances

# What kinds of bugs could this cause in real systems? 
# Unexpected data storage...




if __name__ == "__main__":
    main()