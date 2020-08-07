print("Welcome to the Favorite Teachers Program")

# Teacher Input
fav_teachers = []
fav_teachers.append((input("\nWho is your first favorite teacher? ")).title())
fav_teachers.append((input("Who is your second favorite teacher? ")).title())
fav_teachers.append((input("Who is your third favorite teacher? ")).title())
fav_teachers.append((input("Who is your fourth favorite teacher? ")).title())

# Teacher Display
print(f"\nYour favorite teachers are: {fav_teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(fav_teachers)}")
print(f"Your favorite teachers in reverse alphabetical are: {sorted(fav_teachers, reverse=True)}")
print(f"\nYour top two teachers are: {fav_teachers[0]} and {fav_teachers[1]}.")
print(f"Your next two favorite teachers are: {fav_teachers[2]} and {fav_teachers[3]}.")
print(f"Your least favorite teacher is: {fav_teachers[-1]}.")
print(f"You have a total of {len(fav_teachers)} teachers.")

# New Favorite
fav_teachers.insert(0, (input(f"\nOops, {fav_teachers[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher? ")).title())

# Teacher Display
print(f"\nYour favorite teachers are: {fav_teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(fav_teachers)}")
print(f"Your favorite teachers in reverse alphabetical are: {sorted(fav_teachers, reverse=True)}")
print(f"\nYour top two teachers are: {fav_teachers[0]} and {fav_teachers[1]}.")
print(f"Your next two favorite teachers are: {fav_teachers[2]} and {fav_teachers[3]}.")
print(f"Your least favorite teacher is: {fav_teachers[-1]}.")
print(f"You have a total of {len(fav_teachers)} teachers.")

# Remove Favorite
fav_teachers.remove((input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list? ")).title())

# Teacher Display
print(f"\nYour favorite teachers are: {fav_teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(fav_teachers)}")
print(f"Your favorite teachers in reverse alphabetical are: {sorted(fav_teachers, reverse=True)}")
print(f"\nYour top two teachers are: {fav_teachers[0]} and {fav_teachers[1]}.")
print(f"Your next two favorite teachers are: {fav_teachers[2]} and {fav_teachers[3]}.")
print(f"Your least favorite teacher is: {fav_teachers[-1]}.")
print(f"You have a total of {len(fav_teachers)} teachers.")