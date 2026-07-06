import sys

# Where python looks for any imported module
# by priority 
# it looks to our current project folder first (custom module)
# then -> inside python folder (built-in / system module)
#  then -> site-packages folder (downloaded module)

# What might happen if a module exists in two locations?
# follow the priority, for ex, it will take the one in our folder before the rest

for path in sys.path:
    print(path) 