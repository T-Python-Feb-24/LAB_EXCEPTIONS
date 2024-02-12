
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    while True:
        try:
            cal = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            temp, unit = cal.split()

            if unit == 'F':
                F_to_C = fahrenheit_to_celsius(float(temp))
                print(f"Temperature in Celsius: {round(F_to_C, 2)} C")
                break
            elif unit == 'C':
                C_to_F = celsius_to_fahrenheit(float(temp))
                print(f"Temperature in Fahrenheit: {round(C_to_F, 2)} F")
                break
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        except ValueError:
            print("Invalid temperature value. Please enter valid number")
        except Exception as e:
            print(e.__class__)
        
main()