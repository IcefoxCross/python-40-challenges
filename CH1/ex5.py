import math

print("Welcome to the Multiplication/Exponent Table App")

# Data Input
name = input("\nWhat is your name? ")
message = name.title() + ", Math is cool!"
number = float(input("What number would you like to work with? "))

# Data Output
print(f"\nMultiplication Table for {number}")
print(f"\t1.0 * {number} = {round(number * 1.0,4)}")
print(f"\t2.0 * {number} = {round(number * 2.0,4)}")
print(f"\t3.0 * {number} = {round(number * 3.0,4)}")
print(f"\t4.0 * {number} = {round(number * 4.0,4)}")
print(f"\t5.0 * {number} = {round(number * 5.0,4)}")
print(f"\t6.0 * {number} = {round(number * 6.0,4)}")
print(f"\t7.0 * {number} = {round(number * 7.0,4)}")
print(f"\t8.0 * {number} = {round(number * 8.0,4)}")
print(f"\t9.0 * {number} = {round(number * 9.0,4)}")

print(f"\Exponent Table for {number}")
print(f"\t{number} ** 1 = {round(math.pow(number, 1),4)}")
print(f"\t{number} ** 2 = {round(math.pow(number, 2),4)}")
print(f"\t{number} ** 3 = {round(math.pow(number, 3),4)}")
print(f"\t{number} ** 4 = {round(math.pow(number, 4),4)}")
print(f"\t{number} ** 5 = {round(math.pow(number, 5),4)}")
print(f"\t{number} ** 6 = {round(math.pow(number, 6),4)}")
print(f"\t{number} ** 7 = {round(math.pow(number, 7),4)}")
print(f"\t{number} ** 8 = {round(math.pow(number, 8),4)}")
print(f"\t{number} ** 9 = {round(math.pow(number, 9),4)}")

# Final message
print("\n"+message)
print(f"\t{message.lower()}")
print(f"\t\t{message.title()}")
print(f"\t\t\t{message.upper()}")