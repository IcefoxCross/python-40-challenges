print("Welcome to the Temperature Conversion App")

# Data Input
fahrenheit = float(input("\nWhat is the given temperature in degrees Fahrenheit? "))
celsius = round((fahrenheit - 32) / 1.8, 4)
kelvin = round((fahrenheit + 459.67) / 1.8, 4)

# Data Output
print(f"\nDegrees Fahrenheit:\t{fahrenheit}")
print(f"Degrees Celsius:\t{celsius}")
print(f"Degrees Kelvin:\t\t{kelvin}")