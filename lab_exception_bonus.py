def celsius_to_fahrenheit(celsius):
    fahrenheit = round((celsius * 9/5) + 32, 2)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9, 2)
    return celsius

def main():
    while True:
        try:
            temperature = input("Enter a temprature with its unit C or F (separated by space please): ")
        
            temperature_val, temperature_unit = temperature.split()
            if temperature_val.isnumeric:
                if temperature_unit =="c" or temperature_unit == "C":
                    converted_to_fahrenheit = celsius_to_fahrenheit(float(temperature_val))
                    print(f"Temperture in Fahrenheit: {converted_to_fahrenheit} F")
                    
                elif temperature_unit =="f" or temperature_unit =="F":
                    converted_to_celsius = fahrenheit_to_celsius(float(temperature_val))
                    print(f"Temperture in Celsius: {converted_to_celsius} C")
                    
                else:
                    raise TypeError("Wrong temperature unit! Please try again ('C' for Celsius or 'F' for Fahrenheit only).")
      
        except ValueError:
            print("Wrong temperature value!! Please thry again (only numbers is allowed).")
        except TypeError as e:
            print(e)          
        except Exception:
            print("Something went wrong!! try again.")
        else:
            print("Conversion completed successfully")
            break

# Start The program
print("-------------------- Conversion Temperature Program --------------------")
main()

