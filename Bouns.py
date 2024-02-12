def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main ():
    
  
    try:
         uservalue=int(input("Enter a temperature : "))
         userunit=str(input("Enter its unit , C or F : "))

         if userunit == "c" or userunit == "C" :
          c=celsius_to_fahrenheit(uservalue)
          print(round(c))
 
         elif userunit == "F" or userunit == "f" :
          m=fahrenheit_to_celsius(uservalue)
          print(round(m))
    except ValueError:
       print("invalid number please try again")
    except TypeError as r:
       print(r.__class__,"please try again")
    else:
       print("Conversion completed successfully ^_^ ")


main()
