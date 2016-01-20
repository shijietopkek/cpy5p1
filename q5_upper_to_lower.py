#q5_upper_to_lower.py

import re

# get input
input_str = input("Type an uppercase letter: ")

# get output
if not re.match("^[A-Z]*$", input_str):
    print("Error! Only letters A-Z allowed!")

else:
    print("Lowercase letter: " ,input_str.lower())
