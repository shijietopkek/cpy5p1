
# get input
value = input("Please enter a value between 0 and 1000 : ")

def process_input ():

    global value
    try:
        value = int(value)
        if value>0 and value<1000:
            return True
        else:
            return False
    except ValueError:
        return False

# Determine sum of all digits in integer
if process_input():

    result = 0
    for i in range(len(str(value))):
        result += value%10 
        value = value//10 

#output result
print("Sum of digits in integer:", result)

    

          
          
    
    



