# Integers and Floats
print("* Integers & Floats")
print("–––––––––––––––––––––––––––")

answer = 42
pi = 3.14159
print(answer + pi) # = 45.141.159 // No need to worry about conversion
print(int(pi)) # == 3
print(float(answer)) # == 42.0

# Topic End
print("–––––––––––––––––––––––––––")
print("\n")




# Strings
print("* Strings")
print("–––––––––––––––––––––––––––")

'Hello World' == "Hello World" == """Hello World"""
print("hello".capitalize()) # == "Hello"
print("hello".replace("e", "a")) # == "hallo"
print("hello".isalpha()) # == True
print("123".isdigit()) # == True # Useful when converting to digit
print("some,csv,values".split(",")) # == ["some","csv","values"]

# String Format Function

name = "PythonBo"
machine = "HAL"

print("Nice to meeet you {0}. I am {1}".format(name, machine)) # where 0 == value name & 1 == value of machine
# Python 3.6 Supports String Interpolation
print(f"Nice to meeet you {name}. I am {machine}")

# Topic End
print("–––––––––––––––––––––––––––")
print("\n")




# Boolean and None
print("* Boolean & None")
print("–––––––––––––––––––––––––––")

# - Most often used in IF statements and flagging if something has / hasn't been done
python_course = True
java_course = False
# Capital Letters are necessary in these declarations

print(int(python_course)) # == 1
print(int(java_course)) # == 0

print(str(python_course)) # == "True"

aliens_found = None # Useful as placeholder variable to later have value / equivalent to false

# Topic End
print("–––––––––––––––––––––––––––")
print("\n")




# If Statements
print("* If Statements")
print("–––––––––––––––––––––––––––")

number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

# Python uses identation instead of {} braces to establish code blocks
# if and else both end with a ":" colon, a requirement in

# Truthy and Falsy

number = 5
if number:
    print("Number is defined and truthy")

text = "Python"
if text:
    print("Text is defined and truthy")

# Example 2
python_course = True
if python_course: # No need to compare to True
    print("This will execute")

aliens_found = None
if aliens_found:
    print("This will NOT execute")

# Not If
if number != 5:
    print("This will NOT execute")

if not python_course:
    print("This will also NOT execute")

# Multiple If Conditions

number = 3
if number == 3 and python_course:
    print("This will execute")

if number == 17 or python_course:
    print("This will also execute")

# Ternary If Statements
a = 1
b = 2
print("bigger" if a > b else "smaller")

# Topic End
print("–––––––––––––––––––––––––––")
print("\n")




# Loops
print("* Loops")
print("–––––––––––––––––––––––––––")

student_names = ["Mark","Katrina","Jessica"]

# For Loop
for name in student_names:
    print("Student name is {0}".format(name))
# Python behaves like a for-each and iterrates over each item with no need for boundaries

# If you want begining and end points

x = 0
for index in range(10): # Range is the number of times we want our for loop to execute
    x += 10
    print("The Value of x is {0}".format(x))

# What if we want to begin at a specific point? Increase by a specific amount?
# range(BEGINING, END, INCREMENT)
# Ex: range(5, 10, 2) = [5, 7, 9]

# Exit loop before it finishes???

# Break & Continue

student_names2 = ["Mark","Katrina","Jessica","Not a Robot","Alyssa","Craig","Demi","Tyler"]

for name in student_names2:
    if name == "Not a Robot":
        continue
        print("Found him! " + name)
        print("Currently testing " + name)

# While Loops

x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1

# Infinite Loops
"""If the condition is always true it while will be an infinite loop"""

# Topic End
print("\n")




# Dictionaries
print("* Dictionaries")
print("–––––––––––––––––––––––––––")

    # Allow you to store key value pairs similar to JSON data

student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}
    # Useful for web dev as they can be converted to JSON

all_students = [
    { "name": "Mark", "student_id": 15163 },
    { "name": "Katarina", "student_id": 63112 },
    { "name": "Jessica", "student_id": 30021 },
]

    # how do we retrieve certain data?

print(student["name"])

    # In order to prevent KeyErrors, ie key not found

print(student.get("last_name", "Unknown")) # == "Unknown"

    # View all available keys OR values

print(student.keys()) # = ["name", "student_id", "feedback"]
print(student.values()) # = ["Mark", 15163, None]

    # We can update values like so

student["name"] = "James"
print(student["name"])

    # And delete with

del student["name"]

# Topic End
print("–––––––––––––––––––––––––––")
print("\n")
