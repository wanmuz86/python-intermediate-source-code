class Person:
    # Documentation comment
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        # normally we perform validation on constructor
        # Define validation in class file , even in framework like Django
        
        # ORM - Object Relational Mapping
        # Classs -> Table
        # Object -> Row
        # Property -> column
        # Method -> can be a procedure
        # property -> relationship

        if age <= 0:
            raise ValueError("age must be positive") #throw an error
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I’m {self.name} and I’m {self.age} years old.")

    # Override the built-in __str__ method so that when we print, it is readable
    # for user purposes when we call print

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

    # Override the built-in __repr__ method so when we calll print repr it is readable for DEVELOPER
    # For developer purposes when we all print(repr(e))
    def __repr__(self):
        return f"Debug: Person(name='{self.name}', age={self.age})" # You can use json format here