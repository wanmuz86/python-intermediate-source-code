from person import Person
from employee import Employee

def main():
    p = Person("Aina", 20)
    p.introduce() # introduce from Person

    e = Employee("John", 20, "E102", "IT")
    e.introduce() # introduce from Person

    print(e) # Without overriding __str___ you will get the object (unreadable)

    print(repr(e))

    e.give_raise(10)
    print(e.to_dict())

# To make this module imported and ran as script    
if __name__ == "__main__":
    main()