import datetime

print("Welcome to the Grocery List App")

groceries = ["Meat", "Cheese"]

# Date Info
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
print(f"Current Date and Time: {day}/{month} {hour}:{minute}")

# Grocery Input
print(f"You currently have {groceries[0]} and {groceries[1]} in your list.")
groceries.append(input("\nType of food to add to the grocery list: ").title())
groceries.append(input("Type of food to add to the grocery list: ").title())
groceries.append(input("Type of food to add to the grocery list: ").title())

# Grocery Info & Sorted
print(f"\nHere is your grocery list:\n{groceries}")
groceries.sort()
print(f"Here is your grocery list sorted:\n{groceries}")

# Shopping Simulation
print("\nSimulating grocery shopping...")
print(f"\nCurrent grocery list: {len(groceries)} items\n{groceries}")
bought = (input("What food did you just buy? ").title())
groceries.remove(bought)
print(f"Removing {bought} from list...")
print(f"\nCurrent grocery list: {len(groceries)} items\n{groceries}")
bought = input("What food did you just buy? ").title()
groceries.remove(bought)
print(f"Removing {bought} from list...")
print(f"\nCurrent grocery list: {len(groceries)} items\n{groceries}")
bought = input("What food did you just buy? ").title()
groceries.remove(bought)
print(f"Removing {bought} from list...")
print(f"\nCurrent grocery list: {len(groceries)} items\n{groceries}")
print(f"\nSorry, the store is out of {groceries.pop()}.")
groceries.insert(0, input("What food would you like instead? ").title())

# Final List
print(f"\nHere is what remains on your grocery list:\n{groceries}")