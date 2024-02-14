def additoin(x, y):
    '''
function to addition two numbers
    '''
    x = 10
    y = 20
    print("Addition:", x + b)

   
try:
    additoin(10, 20)
       
   
except NameError as e:
        
    print("There is",e.__class__)
except Exception as e:
    print("There is",e.__class__)
else:
    print("the operation is successful")
