
def additoin(x, y):
  x = 10
  y = 20
try:
  x = 10
  y = 20
  print("Addition:", x + b )
  additoin(10, 20)
  print("the operation is successful" )
except NameError:
  print("the operation is fails")
except Exception as e:
  print(e.__class__)
else:
  raise Exception ("we don't found ")


#Bonus 
def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

def main():
  while True:
    try:
       user= input("Enter a temperature and it's unit (e.g., 25 C or 77 F) :")
       temperature,unit= user.split()
       temperature = float(temperature)

    
       if unit.upper() =="C":
        convert=celsius_to_fahrenheit(temperature)
        print(f"the convert from celsius to fahernheit is success, {convert} F ")
      

       elif unit.upper() =="F":
        convert= fahrenheit_to_celsius(temperature)
        print(f"the convert from  fahernheit to calcuis is success, {convert} C ")

       else:
        print("the unit is error")

        break
    
  
    except ValueError:
      print("ValueError message this value is valid")
    
    except TypeError: 
      print("TypeError message this value is valid")
    
    
main()


    
    
      


  



 
