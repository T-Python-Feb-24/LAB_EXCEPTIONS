def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main ():
    
    uservalue=int(input("Enter a temperature"))
    userunit=str(input("Enter its unit (e.g., 25 C or 77 F"))

    if userunit == "c" or userunit == "C" :
        c=celsius_to_fahrenheit(round(uservalue))
        print(c)

    elif userunit == "F" or userunit == "f" :
        m=fahrenheit_to_celsius(round(uservalue))
        print(m)

try:
 main()
except ValueError:
    print("invalid number please try again",main())
except TypeError as r:
    print(r.__class__,"please try again",main())