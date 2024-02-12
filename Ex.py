

try: 
      def addition(x,y):  
        x=10
        y=20
        print("Addition", x+b)
        print("the operation is successful")
except NameError :
        print("An error occurred:'b' is not found")
except Exception as e:
        print("the operation filed due to a NameError.")

addition(x=10,y=20)
