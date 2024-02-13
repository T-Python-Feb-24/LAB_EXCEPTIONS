def additoin(x, y):
   try:
     x = 10
     y = 20
     print("Addition:", x + b )
     print("the operation is successful" )
   except NameError:
      print("the operation is fails")
   except Exception as e:
     print(e.__class__)
additoin(10, 20)

