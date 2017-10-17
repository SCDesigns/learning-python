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
