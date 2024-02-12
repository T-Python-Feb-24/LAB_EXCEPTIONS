def cel2feh(Celsius):
    return (Celsius * 9/5) + 32

def feh2cel(Fahrenheit):
    return (Fahrenheit - 32) * 5/9

while True:
    try:
        unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
        temp = float(input("Enter the temperature: "))

        if unit.lower() == "c":
            con_temp = round(cel2feh(temp), 2)
            print(f"Temperature in Fahrenheit is -> {con_temp} F")
        elif unit.lower() == "f":
            con_temp = round(feh2cel(temp), 2)
            print(f"Temperature in Celsius ->{con_temp} C")
        else:
            raise TypeError(f"The unit {unit} is Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print(f"Invalid temperature value. Please enter a valid number.")
    except TypeError as e:
        print(e)