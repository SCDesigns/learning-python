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

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name):
    students.append(name)

student_list = get_students_titlecase()

add_student("Mark")

# Topic End
print("–––––––––––––––––––––––––––")
print("\n")
