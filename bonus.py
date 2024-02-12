def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            Input = input("Enter the temerature follwoed by measuring unit:")
            temp, unit = Input.split()
            temp = float(temp)

            if unit.upper() == "C":
                conv_temp = celsius_to_fahrenheit(temp)
                print("Temperature in fahrenheit is: ", round(conv_temp, 2), "F")
            
            elif unit.upper() == "F":
                conv_temp = fahrenheit_to_celsius(temp)
                print("Temperature in celsius is: ", round(conv_temp, 2), "C")
            else:
                raise TypeError("Invalid input, please use C or F to enter input.")
            
        except ValueError:
            print("Invalid input, please use real numbers to input the temperature.")
        except TypeError as e:
            print(e)
    
if __name__ == "__main__":
    main()
            


