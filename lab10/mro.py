class School:
    name = "Universiti Teknikal Melaka" 
    # class variable/property
    # class variable is shareable between instance
    # Called directly from the class => School.name

    #instnace variable is declared inside init

class Student(School):
    def __init__(self,name):   # this is instance variable
        self.name = name

s = Student("Aina")
print(s.name) # Aina
print(Student.name) #  Universiti Teknikal Melaka
print(School.name) # Universiti Teknikal Melaka
del s.name  # Remove instance variable name
print(s.name)  # Get it from the parent

del School.name
print(s.name)
print(Student.__mro__)

# Why does the output change?
# Because instance s do not have name anymore


# Where did Python find a name after deletion?
# It will look at class first, since it is not there it look at parent class


# What happens if School.name is removed?
#  It will throw an error, attribute not found

