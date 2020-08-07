import math

print("Welcome to the Right Triangle Solver App")

# Data Input
first_leg = float(input("\nWhat is the first leg of the triangle? "))
second_leg = float(input("What is the second lef of the triangle? "))
hypotenuse = round(math.sqrt(math.pow(first_leg, 2) + math.pow(second_leg, 2)), 3)
area = round(first_leg * second_leg * 1/2, 3)

# Data Output
print(f"\nFor a triangle with legs of {first_leg} and {second_leg} the hypotenuse is {hypotenuse}")
print(f"For a triangle with legs of {first_leg} and {second_leg} the area is {area}")