def celsius_to_fahrenheit(celsius):
    '''
    celisus to fahrenheit Converter
    '''
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# print(celsius_to_fahrenheit(celsius= float(input("Enter the temperature in celsius:"))),"in fahrenheit.")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
# print(fahrenheit_to_celsius(fahrenheit=int(input("Enter the temperature in fahrenheit:")))," in celsius.")


def main():
    while True:
        try:
            insert_temperature=input("Enter a temperature and its unit (e.g., '25 C' or '77 F)':")
            temperature,unit=insert_temperature.split()
            if unit.lower() =='c':
                print(f"Temperature in Fahrenheit: {round(celsius_to_fahrenheit(float(temperature)),2)} F")
                   
            elif unit.lower()=='f':
                print(f"Temperature in Celsius: {round(fahrenheit_to_celsius(float(temperature)),2)} C")
                
        except TypeError:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            print("try again")       
        except ValueError:
            print("Invalid value. Please enter number.")   
        

main()
