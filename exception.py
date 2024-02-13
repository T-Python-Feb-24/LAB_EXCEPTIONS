
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

# additoin(10, 20)

try:
    additoin(10 , 20)
except NameError:
    print("b is not defined")
else:
    print("The operation is successful")

