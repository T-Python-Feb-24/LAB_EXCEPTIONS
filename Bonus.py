
# 1. Write a function `celsius_to_fahrenheit(celsius)` that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula `fahrenheit = (celsius * 9/5) + 32`.
def celsius_to_fahrenheit(celsius:int): 
    fahrenheit =round((celsius * 9/5) + 32,2) 
    return fahrenheit 


# 2. Write a function `fahrenheit_to_celsius(fahrenheit)` that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula `celsius = (fahrenheit - 32) * 5/9`.

def fahrenheit_to_celsius(fahrenheit:int):
    celsius = round((fahrenheit - 32) * 5/9,2)
    return celsius

# 3. Write a `main` function that:
#     a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F").
#     b. Splits the input string into a temperature value and its unit.
#     c. Tries to convert the input temperature to its opposite unit using the appropriate function (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
#     d. Handles the following exceptions:
#         - `ValueError`: If the user enters an invalid temperature value, display an error message and prompt the user to try again.
#         - `TypeError`: If the user enters an invalid unit, display an error message and prompt the user to try again.
#     e. If the conversion is successful, print the converted temperature and its unit. 

def main():     
    while True :
        try : 
            userInput = input("Enter a temperature and its unit ('C' for Celsius or 'F' for Fahrenheit) sperate them by a space! (ex:45 F)")  
            inputs =  userInput.split()
            if len(inputs) == 2 :
                temperature, unit = int(inputs[0]) , str(inputs[1])
            else:
                print("please make sure to enter two values (first temperture,then its unit ) spreating them by a space !")
            
            if unit == 'C' or unit =='c':
                print(f"Temperature converted from celsius to fahrenheit is:{celsius_to_fahrenheit(temperature)} F")
                break
            elif unit == 'F'&len(unit)==1  or unit == 'f' &len(unit)==1:
                print(f"Temperature converted from fahrenheit to celsius is:{fahrenheit_to_celsius(temperature)} C")
                break

                
        except ValueError :
            print(ValueError ,'Try again')
        except TypeError: 
            print(TypeError ,'Try again')
        except Exception as e : 
            print ("Try again!")



# 4. Call the `main` function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.

main()

