
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# celsius_to_fahrenheit()

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9

    return celsius


def main():
    temperature = int(input("Enter the temperature : ") )
    unit = input("Enter the unit : ")

    if unit.upper() == "C":
        print("Temperature in Celsius: ")
        print(celsius_to_fahrenheit(temperature))
    elif unit == "F":
        print("Celsius in Temperature: ")
        print(fahrenheit_to_celsius(temperature))
    else:
        print("Try again ")


try :
    main()
except ValueError :
    print("Invalid temperature value, please try again.")
except TypeError:
    print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print(main)

