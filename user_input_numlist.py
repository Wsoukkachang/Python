# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0
digit = 1
description = "This script will ask you to enter 10 numbers. \nIf the numbers are even, it will add it to the sum total. INTEGERS ONLY! Enjoy!\n"

# seek user input for ten numbers 
print(description)

def is_numeric(str):
    try:
        float(str)
        return True
    except (ValueError, TypeError):
        return False

for i in range(10):
    userInput = (input("{}) Enter any number: ".format(digit)))
    try:
        if is_numeric(userInput) == True:
            newInput = float(userInput)
            user_list.append(newInput)
            digit += 1
            if newInput % 2 == 0:
                list_sum += newInput
                
    #     elif is_numeric(userInput) == False:
    #         raise TypeError("Only numbers are allowed")
    # except TypeError:
    #     print("Incorrect input. That's not a number!")


# check to see if number is even and if yes, add to list_sum
# print incorrect value warning when ValueError exception occurs

print("\nUser's list: {}".format(user_list))
print("The sum of the even numbers in user's list is: {}.".format(list_sum))