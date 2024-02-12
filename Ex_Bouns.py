def celsius1(celsius):
    return(celsius * 9/5) + 32
    

def fahrenheit1(fahrenheit):
    return(fahrenheit - 32) * 5/9
    

def main():
    while True:
        try:
            user_input = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
            temperature = float(temperature)

            if user_input.upper() == 'C':
                converted_temperature = celsius1(temperature)
                converted_unit = 'Fahrenheit'
            elif user_input.upper() == 'F':
                converted_temperature = fahrenheit1(temperature)
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
