# Q. Write a Python program for students' marks system

s1 = int(input("Enter marks in Maths: "))
s2 = int(input("Enter marks in Electrical Engg.: "))
s3 = int(input("Enter marks in Mechanics: "))
s4 = int(input("Enter marks in Chemistry: "))

total = (s1+s2+s3+s4)

avg = total/4

print("Total marks: ", total)
print("Average: ", avg)

if ( s1<40 or s2<40 or s3<40 or s4<40 ):
    print("Result: Fail!")

else:
    if avg >= 90:
        print("Grade: A+")

    elif avg >= 80:
        print("Grade: A")

    elif avg >= 70:
        print("Grade: B+")

    elif avg >= 60:
        print("Grade: B")

    elif avg >= 50:
        print("Grade: C")

    elif avg >= 40:
        print("Grade: D")

    print("Result: Pass!")
