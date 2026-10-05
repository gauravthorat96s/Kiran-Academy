age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age: Age cannot be negative.")

elif age > 120:
    print("Invalid age: Please enter a realistic age.")

elif age >= 18:
    print("You are eligible for voting.")

else:
    print("You are not eligible for voting.")