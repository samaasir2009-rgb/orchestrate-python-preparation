print("==============================")
print("       SMART CALCULATOR")
print("==============================")





input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))

print("First number is :" + str(input1))
print("Second number is :" + str(input2))


addition = input1 + input2
subtraction = input1 - input2

print("Addition:", addition)
print("Subtraction:", subtraction)


multiplication = input1 * input2
if input2 != 0:
    division = input1 / input2
    print("Division:", division)
else:
    print("Cannot divide by zero")

print("Multiplication:", multiplication)


print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")




if choice == "1":
    print("Addition:", input1 + input2)

elif choice == "2":
    print("Subtraction:", input1 - input2)

elif choice == "3":
    print("Multiplication:", input1 * input2)

elif choice == "4":
    if input2 != 0:
        print("Division:", input1 / input2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")


print("==============================")
print("     Thank you for using!")
print("==============================")