def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b) #name 'b' is not defined
    
try:
  additoin(10, 20)
except NameError as d:
  print("Name not defind in :",d.__class__)
except ValueError:
  print("ivalid value")
else:
  print("the operation is successful")