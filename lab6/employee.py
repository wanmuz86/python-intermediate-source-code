from person import Person

class Employee(Person):
    """Represents an employee who is also a person."""

    # In addition to name and age, we extend the class by adding
    # property employee_id and department
    def __init__(self, name, age, employee_id, department):
        # Call the parent class constructor super().__init__
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    # Override, create the employee version of introduce
    def introduce(self):
       # super().introduce() # call the parent class's version of introduce()
        print(f"Hi, I'm {self.name} (ID: {self.employee_id}) from {self.department} and age {self.age} years old.")

    def give_raise(self, percent):
        """Bonus method example: just prints raise info (no salary field in this lab)."""
        if percent <= 0:
            print("Raise percent must be positive")
            return
        print(f"{self.name} received a percent of {percent}% raise (demo only).")

    def to_dict(self):
        return {
            "name":self.name,
            "age":self.age,
            "employee_id":self.employee_id,
            "department":self.department
        }
        
    # Create the child's version of __str__
    def __str__(self):
        return (
            f"Employee(name='{self.name}', age={self.age}, "
            f"employee_id='{self.employee_id}', department='{self.department}')"
        )
    
    # Create the child's version of __repr__
    def __repr__(self):
        return (
            f"Debug: Employee(name='{self.name}', age={self.age}, "
            f"employee_id='{self.employee_id}', department='{self.department}')"
        )

