def addition(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
        print("The operation is successful")  # This line will not be reached if an exception occurs
    except NameError as e:
        print("An error occurred:", str(e))
        print("The operation failed due to a Name Error.")
    except Exception as e:
        print("An error occurred:", str(e))
        print("The operation failed due to an unknown error.")

addition(10, 20)