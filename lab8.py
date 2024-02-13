
def addition(x, y):
    x = 10
    y = 20
    print("Addition:", x + y)

try:
    addition(10, 20)
except NameError:
    print("The name is error")
except Exception as e:
    print(e.__class__)
else:
    print("The operation is successful")


