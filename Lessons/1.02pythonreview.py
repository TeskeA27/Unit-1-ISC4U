# grade = int(input("Enter in a grade (0-100): "))

# if grade >= 90:
    # print("A")
# elif grade >= 80:
    # print("B")
# elif grade >= 70:
    # print("C")
# elif grade >= 60:
    # print("D")
# else:
    # print("F")






# age = int(input("Enter your age: "))


# if age < 3:
#     print("Ticket Price: Free")
# elif age <= 12:
#     print("Ticket Price: $8")
# elif age <= 17:
#     print("Ticket Price: $12")
# elif age <= 64:
#     print("Ticket Price: $15")
# else:
#     print("Ticket Price: $10")



# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if num1 > num2:
#     print("First number is larger")
# elif num2 > num1:
#     print("Second number is larger")
# else:
#     print("Both numbers are equal")



# age = int(input("Enter your age: "))
# license = input("Do you have a driver's license? (yes/no): ").lower().strip()

# if age >= 21 and license == "yes":
#     print("You can rent a car")
# elif age >= 21 and license != "yes":
#     print("You need a license to rent a car")
# elif age < 21 and license == "yes":
#     print("You must be 21 or older to rent a car")
# else:
#     print("You must be 21 or older and have a license")



# size = input("What size pizza do you want? (small/medium/large): ").lower().strip()
# extra_cheese = input("Do you want extra cheese? (yes/no): ").lower().strip()

# price = 0

# if size == "small":
#     price = 10
# elif size == "medium":
#     price = 14
# elif size == "large":
#     price = 18
# else:
#     print("Invalid pizza size entered.")

# if price > 0:
#     if extra_cheese == "yes":
#         price += 2
    
#     print(f"Your total price is: ${price}")



# gpa = float(input("Enter student's GPA (0.0-4.0): "))
# volunteer_hours = int(input("Enter volunteer hours: "))

# if gpa >= 3.5:
#     if volunteer_hours >= 50:
#         print("Full scholarship!")
#     elif volunteer_hours >= 25:
#         print("Partial scholarship")
#     else:
#         print("Academic scholarship only")
# elif gpa >= 3.0:
#     if volunteer_hours >= 50:
#         print("Community service scholarship")
#     else:
#         print("Not eligible for scholarship")
# else:
#     print("Not eligible for scholarship")



# count = int(input("Enter a starting number: "))
# while count > 0:
#     print(count)
#     count -= 1 

# print("Blastoff!")



# secret_number = 42
# attempts = 0
# guess = None
# while guess != secret_number:
#     guess = int(input("Guess the secret number: "))
#     attempts += 1 
    
#     if guess > secret_number:
#         print("Too high!")
#     elif guess < secret_number:
#         print("Too low!")
#     else:
#         print("Correct!")

# # Print total attempts after exiting the loop
# print(f"It took you {attempts} guess(es) to find the secret number!")



# n = int(input("Enter a number (n): "))

# total = 0

# for i in range(1, n + 1):
#     total += i

# print(f"The sum of all numbers from 1 to {n} is: {total}")



# num = int(input("Enter the multiplication number: "))
# limit = int(input("Enter the ending multiplier number: "))

# print(f"\n--- Multiplication Table for {num} ---")


# for i in range(1, limit + 1):
#     result = num * i
#     print(f"{num} x {i} = {result}")
