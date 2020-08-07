print("Welcome to the Letter Counter App")
# Data Input
name = input("\nWhat is your name? ").strip()
print(f"\nHello {name.title()}!")
print("I will count the number of times that a specific letter occurs in a message.")
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occurrences of? ")
# Data Output
letter_count = message.lower().count(letter.lower())
print(f"{name.title()}, your message has {letter_count} {letter}'s in it.")