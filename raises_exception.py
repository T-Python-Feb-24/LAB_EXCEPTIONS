def additoin(x, y):
    '''unsuccessful operation'''

    try:
        x = 10
        y = 20
        print("Addition:", x + 'b')
    except NameError as e:
        print(f"Error: {e}. Please make sure all variables are correctly defined.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("the operation is successful")

additoin(10, 20)
############################################################################################################
print("-"*50)
def additoin2 (x , y):
    '''successful operation'''
    try:
        x = 10
        y = 20
        print("Addition:", x + 5)
    except NameError as e:
        print(f"Error: {e}. Please make sure all variables are correctly defined.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("the operation is successful")

additoin2(10,20) 
