def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        try:
            user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            temperature, unit = user_input.split()
            temperature = float(temperature)

            if unit.upper() == 'C':
                converted_temperature = celsius_to_fahrenheit(temperature)
                converted_unit = 'Fahrenheit'
            elif unit.upper() == 'F':
                converted_temperature = fahrenheit_to_celsius(temperature)
                converted_unit = 'Celsius'
            else:
                raise TypeError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

            print(f"The converted temperature is {converted_temperature} {converted_unit}.")
            break

        except ValueError:
            print("Invalid temperature value. Please try again.")
        except TypeError as e:
            print(str(e))
main()
