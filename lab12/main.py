from app_error import AppError
from validation_error import ValidationError
from validators import validate_student_record

# higher-level context wrapper
# to get where does the error come from

class StudentRecordBuildError(AppError):

    pass

def build_student_record(data:dict)->dict:
    # Anything that can causes error, needs to be called within try , except block
    try:
        return validate_student_record(data)
    except ValidationError as e:
        raise StudentRecordBuildError("Failed to build student record") from e


def test_cases():
    print("\n--- Test Cases ---")

    good = {"name":"Aina","age":7,"scores":[80,90,85]}
    bad_name = {"name":"","age":7, "scores":[80]}
    bad_age = {"name":"Ali", "age":3, "scores":[70]}
    bad_scores = {"name":"Mira", "age":8, "scores":[95,150]}

    cases = [("GOOD",good),("BAD_NAME",bad_name),("BAD_AGE",bad_age),("BAD_SCORES",bad_scores)]
    
    # for loop for tuple
    for label, data in cases:
        print(f"\n Case: {label}")
        try:
            record = build_student_record(data)
        except StudentRecordBuildError as e:  # Only those who have error fall here
            print("Build error",e)
            print("Root cause: ",repr(e.__cause__))
        else:     # Only those who success fall here
            print("Validated record:", record)
        finally: # Both scenario will fall here
            print("Done case: ",label)

def main():
    test_cases()

if __name__ == "__main__":
    main()