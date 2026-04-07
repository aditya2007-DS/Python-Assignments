# A program to calculate sum and average of first n numbers.

n = int(input("Enter the first 'n' numbers: "))

total = 0

for i in range(1, n+1):
    total = total + i

average = total / n

print("Sum = ", total)
print("Average = ", average)