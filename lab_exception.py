def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
#^^ the error is SyntaxError we can fix it like this -> print("Addition:", x + y)

try:
    additoin(10, 20)
except NameError:
    print('the exception/error is a NameError ')
except Exception as e:
    print(e)
else:
    print('the operation is successful ')
