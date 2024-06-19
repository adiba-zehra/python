temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == 'C':
    converted = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {converted}")
elif unit == 'F':
    converted = (temp - 32) * 5/9
    print(f"The temperature in Celsius is: {converted}")
else:
    print("Invalid unit.")
