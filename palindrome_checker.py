# Q. Write a Python program to check Palindrome number.

num = input("Enter a number: ")

# Reversing the number using slicing
rev = num[::-1]

# Checking if original and reversed number are same
if rev == num:
    print("The number is a Palindrome.")
else:
    print("The number is not a Palindrome.")