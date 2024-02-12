def celsius1(celsius):
    return(celsius * 9/5) + 32
    

def fahrenheit1(fahrenheit):
    return(fahrenheit - 32) * 5/9
    


    while True:
        try:
            user_input = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
            temperature = float("temperature :" )

            if user_input.upper() == 'C':
                converted_temperature = round(celsius1(temperature),2)
                print(f"temperature in fahrenheit1 is {converted_temperature}F")
            elif user_input.upper() == 'F':
                converted_temperature = round(fahrenheit1(temperature),2)
                print(f"temperature in celsius is {converted_temperature}C")
            else:
                raise TypeError(f"the user input{user_input}is invalid. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError:
            print("Invalid temperature value. Please try again.")
        except TypeError as e:
            print(e)

