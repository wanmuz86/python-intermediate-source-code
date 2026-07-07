
# Class Structure - UML Diagram

## Class Hierarchy

```
┌─────────────────────────────────────┐
│           Person                    │
├─────────────────────────────────────┤
│ Attributes:                         │
│  - name: str                        │
│  - age: int                         │
├─────────────────────────────────────┤
│ Methods:                            │
│  - __init__(name, age)              │
│  - introduce()                      │
└─────────────────────────────────────┘
            △
            │ inherits
            │
    ┌───────┴────────┐
    │                │
    │                │
┌───────────────┐  ┌──────────────┐
│   Student     │  │    Teacher   │
├───────────────┤  ├──────────────┤
│ Attributes:   │  │ Attributes:  │
│ (inherited)   │  │ (inherited)  │
│ - name: str   │  │ - name: str  │
│ - age: int    │  │ - age: int   │
├───────────────┤  ├──────────────┤
│ Methods:      │  │ Methods:     │
│ (inherited)   │  │ (inherited)  │
│ - __init__()  │  │ - __init__() │
│ - introduce() │  │ - introduce()│
├───────────────┤  ├──────────────┤
│ - study()     │  │ - teach()    │
└───────────────┘  └──────────────┘
```

## Detailed Specifications

### Person (Base Class)
**Purpose:** Base class that defines common attributes and methods for all person types.

| Attribute | Type | Description |
|-----------|------|-------------|
| name | str | Person's name |
| age | int | Person's age |

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__` | name, age | Constructor to initialize person attributes |
| `introduce` | - | Prints introduction with person's name |

---

### Student (Inherits from Person)
**Purpose:** Represents a student with study capabilities.

**Inherited Attributes:**
- name (str)
- age (int)

**Inherited Methods:**
- `__init__(name, age)`
- `introduce()`

| Method | Parameters | Description |
|--------|-----------|-------------|
| `study` | - | Prints that the student is studying |

---

### Teacher (Inherits from Person)
**Purpose:** Represents a teacher with teaching capabilities.

**Inherited Attributes:**
- name (str)
- age (int)

**Inherited Methods:**
- `__init__(name, age)`
- `introduce()`

| Method | Parameters | Description |
|--------|-----------|-------------|
| `teach` | - | Prints that the teacher is teaching |

---

## Inheritance Relationship

- **Person** is the parent/base class
- **Student** and **Teacher** are child classes that inherit from Person
- Both Student and Teacher classes inherit all attributes and methods from Person
- Student adds the `study()` method for student-specific behavior
- Teacher adds the `teach()` method for teacher-specific behavior

## Design Pattern

This demonstrates the **Inheritance** design pattern where:
- Common functionality is abstracted into the base class (Person)
- Specialized classes (Student, Teacher) extend the base class
- Code reusability is achieved through inheritance
- Each subclass adds its own specific behavior without duplicating common code
