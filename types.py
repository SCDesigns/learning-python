# Integers and Floats

answer = 42
pi = 3.14159
print(answer + pi) # = 45.141.159 // No need to worry about conversion
print(int(pi)) # == 3
print(float(answer)) # == 42.0




# Strings

'Hello World' == "Hello World" == """Hello World"""
"hello".capitalize == "Hello"
"hello".replace("e", "a") == "hallo"
"hello".isalpha() == True
"123".isdigit() == True # Useful when converting to digit
"some,csv,values".split(",") == ["some","csv","values"]

# String Format Function

name = "PythonBo"
machine = "HAL"

"Nice to meeet you {0}. I am {1}".format(name, machine) # where 0 == value name & 1 == value of machine
# Python 3.6 Supports String Interpolation
f"Nice to meeet you {name}. I am {machine}"




# Boolean and None

# - Most often used in IF statements and flagging if something has / hasn't been done
python_course = True
java_course = False
# Capital Letters are necessary in these declarations

int(python_course) == 1
int(java_course) == 0

str(python_course) == "True"

aliens_found = None # Useful as placeholder variable to later have value / equivalent to false




# If Statements

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
"bigger" if a > b else "smaller"




# Loops

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
