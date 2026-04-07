# A program to check whether a number is an Armstrong numner or onot.

n = int(input("Enter any number: "))
power = len(str(n))
temp = n

sum = 0
while temp>0:
    d = temp%10
    sum = sum+d**power
    temp = temp//10

if sum == n:
    print("The given number is an Armstrong number.")

else:
    print("The given number is not an Armstrong number.")