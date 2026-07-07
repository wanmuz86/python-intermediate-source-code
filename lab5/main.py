from student import Student
from teacher import Teacher
# student = {
#     "name":"Aina",
#     "age":6,
#     # lambda - anonymous function - function without name
#     # suitable for one line code
#     "introduce":lambda:print("Hi, I am Aina")
# }

# # Execute the function ()
# student["introduce"]()

# student2 = {
#     "name":"Ali",
#     "age":7,
#     "introduce":lambda:print("Hi, I am Ali")
# }
# student2["introduce"]()

# # What happens if we forget a key?
# # Normally there is auto complete, or there is no checking if we make a typo


# # How do we ensure consistency across students?
# # No standardization , key mismatch , format mismatch , data type mismatch


# # Can behavior be reused easily? 
# # It cannot be reuse easily. The proper solution is using class

# The type check happen with additional tool (KIV)
s1  = Student("Aina", 6)
s2 = Student("Ali", 7)

s1.introduce()
s2.introduce()

s1.study()

t1 = Teacher("Mr Adam", 40)
t1.introduce()
t1.teach()
# t1.study()