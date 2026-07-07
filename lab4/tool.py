# tool.py can be run as imported module and also as script

def greet(name):
    return f"Hello {name}"

def main():
    print(greet("Direct User"))

# Scenario where it is run as a script
if __name__ == "__main__":
    main()
