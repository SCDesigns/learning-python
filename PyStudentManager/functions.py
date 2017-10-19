# Our App - PyStudentManager
# Yield
print("* Yield")
print("–––––––––––––––––––––––––––")

    # Some examples of functions in python:
students = []
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332): # sets a default student_id if one is not provided / ideally would be unique and random
    student = {"name": name, "student_id": student_id }
    students.append(student)

def save_file(student):
    try:
        f = open("students.txt", "a") # a denotes we want to "append" said file
        f.write(student + "\n")
        f.close() # necessary to close file to prevent any memory leaks and tell the OS so that we are done with the file
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readLines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)

# Topic End
print("–––––––––––––––––––––––––––")
print("\n")
