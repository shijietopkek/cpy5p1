#q6_find_ascii_char.py

#get input
number = input("Type an ASCII code: ")

#character of ASCII number
char = chr(int(number))

#generate output
if 0 < int(number) < 127:
    print("Character of ASCII code: ", char)
else:
    print("Invalid answer")




