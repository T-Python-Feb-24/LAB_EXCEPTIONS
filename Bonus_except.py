def celsius_to_fahrenheit(celsius:float)->float:
    fahrenheit:float = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit)->float:
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    temp_and_unit = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
    temp = ''
    unit = ''
    after_convert:float = 0.0
    for i in temp_and_unit:
        if i.isdigit() or i == '.':
            temp += i
        elif i in ['C', 'F', 'c', 'f']:
            unit = i
    temp = float(temp)
    if unit == 'f' or unit == 'F':
        after_convert = round(fahrenheit_to_celsius(temp), 2)
        print(f'Temperature in Celsius: {after_convert} C')
    elif unit == 'c' or unit == 'C':
        after_convert = round(celsius_to_fahrenheit(temp))
        print(f'Temperature in Fahrenheit: {after_convert} F')
    else:
        print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

while True:
    try:
        main()
    except ValueError:
        print('enter invalid data')
    except TypeError:
        print('enter invalid data')
    except Exception as e:
        print('enter invalid data')

    