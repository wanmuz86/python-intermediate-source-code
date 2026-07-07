from person import Person;

#Without inheritance
# capital letter singular for class
# class Student:
#     #constructor 
#     # properties
#     def __init__(self, name, age):
#         # We can also specify the data type for standardization
#         self.name : str = name
#         self.age : int = age
    
#     def introduce(self):
#         print(f"Hi, I am {self.name}") # self refer to the instance # reusability

# With inheritance
class Student(Person):
    def study(self):
        print(f"{self.name} is studying")


# Prompt use to copilot to generate the UML

# have a look at @person.py @student.py @teacher.py , provide the uml diagram of this classes and write in in structure.md