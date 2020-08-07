print("Welcome to the Basketball Roster Program")

# Roster Entry
roster = []
roster.append((input("\nWho is your point guard? ")).title())
roster.append((input("Who is your shooting guard? ")).title())
roster.append((input("Who is your small forward? ")).title())
roster.append((input("Who is your power forward? ")).title())
roster.append((input("Who is your center? ")).title())

# Roster Info
print("\n\tYour starting 5 for the upcoming basketball season:")
print(f"\tPoint Guard:\t\t{roster[0]}")
print(f"\tShooting Guard:\t\t{roster[1]}")
print(f"\tSmall Forward:\t\t{roster[2]}")
print(f"\tPower Forward:\t\t{roster[3]}")
print(f"\tCenter:\t\t{roster[4]}")

# Injured Player
injured_player = roster.pop(2)
print(f"\nOh no, {injured_player} is injured.")
print(f"Your roster only has {len(roster)}.")
added_player = (input(f"Who will take {injured_player}'s spot? ")).title()
roster.insert(2, added_player)

# Roster Info
print("\n\tYour starting 5 for the upcoming basketball season:")
print(f"\tPoint Guard:\t\t{roster[0]}")
print(f"\tShooting Guard:\t\t{roster[1]}")
print(f"\tSmall Forward:\t\t{roster[2]}")
print(f"\tPower Forward:\t\t{roster[3]}")
print(f"\tCenter:\t\t{roster[4]}")

# Final Info
print(f"\nGood luck {added_player}, you will do great!")
print(f"Your roster now has {len(roster)}.")