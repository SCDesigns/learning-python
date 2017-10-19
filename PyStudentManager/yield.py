students = []

def read_file():
    try:
        f = open("students.txt", "r")
        for students in f.readlines(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")

def read_students(f):
    for line in f:
        yield line

read_file()
print(students)