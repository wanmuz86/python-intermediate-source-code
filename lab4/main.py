import tool

# Imported module do not execute script-only code

print(tool.greet("Imported user"))

# Why is __name__ == "__main__" critical for reusable modules?
# To indicate either it is run from a script or run from an import
# Code run from import will not execute the script code

# What would happen without this guard? -> The imported module cannot be executed
