# Our App - PyStudentManager
# Functions
print("* Functions")
print("–––––––––––––––––––––––––––")

    # Of course we've alreadt seen some of Python's built in functions

print("Hello World")
str(3) # == "3"
int("15") # == 15
username = input("Enter the user's name: ")

    # Some examples of functions in python:
students = []
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332): # sets a default student_id if one is not provided / ideally would be unique and random
    student = {"name": name, "student_id": student_id }
    students.append(name)

def var_args(name, *args):
    print(name)
    print(args)

def var_kw_args(name, **kwargs): # Allows you to target specific values
    print(name)
    print(kwargs["description"], kwargs["feedback"])

student_list = get_students_titlecase()

add_student(name="Mark", student_id=15)

var_args("Mark", "Loves Python", None, "Hello", True)

var_kw_args("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)

# Topic End
print("–––––––––––––––––––––––––––")
print("\n")




# Function Arguments
