def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


red: str = "\033[31m"
green: str = "\033[32m"
defcolor: str = '\033[m'
try:
    additoin(10, 20)
except NameError as e:
    print(f"{red}Variable {e.name} not defind", end=defcolor)

else:
    print(f"{green}The operation is successful ", end=defcolor)
