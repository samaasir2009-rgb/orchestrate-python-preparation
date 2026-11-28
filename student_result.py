name = input("Enter the name of the student:")

marks1 = float(input("Enter the marks for Maths:"))
marks2 = float(input("Enter the marks for English:"))
marks3 = float(input("Enter the marks for Geography: "))

print("\n========== STUDENT REPORT ==========")
print("Student Name:",name)
print("Maths:",marks1)
print("English:",marks2)
print("Geography:", marks3)

total = marks1 + marks2 + marks3
average = total / 3

print("Total Marks:",total)
print("Average Marks",average)

if marks1 >= 35 and marks2 >=35 and marks3 >=35:
    print("Result:Pass")
else:
    print("Result:Fail")
    print("====================================")

    if average >= 90:
        print("A")
    elif average >=70:
        print("B")
    elif average >=60:
        print("C")
    elif average >=35:
        print("D")
    else:
        print("F")