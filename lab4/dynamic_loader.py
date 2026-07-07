import importlib

# Define the module to be imported using string
module_name = "math"

# Import only when we want to use it
# lazy load - load when it is needed (used a lot in front end) 
math_module = importlib.import_module(module_name)

print(math_module.sqrt(49))

# TO import the custom module
module_name = "tool"
module = importlib.import_module(module_name)
print(module.greet("Dynamic User"))