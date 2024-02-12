#Write a function `celsius_to_fahrenheit(celsius)` that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula `fahrenheit = (celsius * 9/5) + 32`.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#Write a function `fahrenheit_to_celsius(fahrenheit)` that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula `celsius = (fahrenheit - 32) * 5/9`.
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            #Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F").
            input_str = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            #Splits the input string into a temperature value and its unit.
            parts = input_str.split()
            if len(parts) != 2:
                raise ValueError("Invalid input format. Please use the format '<temperature> <unit>'.")
            temp, unit = parts
            temp = float(temp)  # This could raise ValueError if temp is not a number

            if unit.upper() == 'C':
                converted_temp = celsius_to_fahrenheit(temp)
                print(f"Temperature in Fahrenheit: {converted_temp} F")
            elif unit.upper() == 'F':
                converted_temp = fahrenheit_to_celsius(temp)
                print(f"Temperature in Celsius: {converted_temp} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            break  
        #`ValueError`: If the user enters an invalid temperature value, display an error message and prompt the user to try again.
        except ValueError as p:
            print(f"Error: {p}. Please enter a valid numerical temperature.")
        #`TypeError`: If the user enters an invalid unit, display an error message and prompt the user to try again.
        except TypeError as q:
            print(q)
#Call the `main` function to run the program.
main()
