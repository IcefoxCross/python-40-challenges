print("Welcome to the Grade Sorter App")

grades = []

# Data Input
grades.append(int(input("\nWhat is your first grade? (0-100): ")))
grades.append(int(input("What is your second grade? (0-100): ")))
grades.append(int(input("What is your third grade? (0-100): ")))
grades.append(int(input("What is your fourth grade? (0-100): ")))
print(f"\nYour grades are: {grades}")

# Data Sorting
grades.sort(reverse=True)
print(f"\nYour grades from highest to lowest are: {grades}")

# Dropping lowest grades
print("\nThe lowest two grades will now be dropped.")
print(f"Removed grade: {grades.pop()}")
print(f"Removed grade: {grades.pop()}")

# Final printing
print(f"\nYour remaining grades are: {grades}")
print(f"Nice work! Your highest grade is a {grades[0]}.")