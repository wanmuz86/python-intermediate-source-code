from type_validation_error import TypeValidationError
from required_error import RequiredFieldError
from range_error import RangeError

# To check if fields is empty or not
def require_non_empty_str(field:str, value):
    if not isinstance(value,str):
        raise TypeValidationError(field, "must be a string")
    if not value.strip():
        raise RequiredFieldError(field, "must not be empty")
    return value.strip()

# number given is in range
def require_int_in_range(field:str, value, min_value:int, max_value:int):
    # if the given value is not integer
    if not isinstance(value, int):
        raise TypeValidationError(field, "must be an integer")
    # if not given value is not within the range min_value and max_value
    if not (min_value <= value <= max_value):
        raise RangeError(field, f"must be between {min_value} and {max_value}")
    return value

# verify list of scores to follow the given format
def require_score_list(field:str, value):
    # if it is not a list 
    if not isinstance(value, list):
        raise TypeValidationError(field, "must be a  list of integers(0-100)")
    # for loop with index
    # the first variable (i) -> index 0,1,2,
    # the second variable (s)  -> value  (100,80,90)..
    for i, s in enumerate(value):
        if not isinstance(s, int):
            raise TypeValidationError(field, f"score at index {i} must be an integer")
        if not (0 <= s <= 100):
            raise RangeError(field, f"score at index {i} must be between 0 and 100")
    return value


# Create a function to validate the given input
# name -> str, non-empty
# age -> (5-18)
# scores -> (list[int] each 0-100)

def validate_student_record(data:dict)-> dict:
    if not isinstance(data,dict):
        raise TypeValidationError("data","must be a dictionary")

    name = require_non_empty_str("name", data.get("name")) # data.get("name") / data["name"]
    age = require_int_in_range("age",data.get("age"),5,18)
    scores= require_score_list("scores", data.get("scores",[]))
    
    # If everything is ok we will get this
    # If not an error will be thrown
    # We can use decorator to create a validator
    return {"name":name,"age":age,"scores":scores}