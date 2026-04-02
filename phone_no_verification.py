# Q. Write a Python Program to check if a mobile number is valid or not.

def is_valid_mobile(number):
    # Check if all characters are digit and length is 10
    if number.isdigit() and len(number) == 10:
        return True
    else:
        return False
    
# Taking input from user
mobile = input("Enter a mobile number: ")

if is_valid_mobile(mobile):
    print("Valid Mobile Number.")
else:
    print("Invalid Mobile Number.")