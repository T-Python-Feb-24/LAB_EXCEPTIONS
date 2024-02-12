def additon(x, y):
    x = 10
    y = 20
    print("Addition", x + b)

try:
    additon(10, 20)
except NameError:
    print("You have NAME ERROR: name 'b' is not defined.")
except Exception:
    print("Something went wrong!!")
else:  
    print("The operation is successful.")
