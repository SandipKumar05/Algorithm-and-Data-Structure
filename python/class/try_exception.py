
class CustomError(Exception):
    ...
    pass

def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional
        # Part as Answer 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ")
    except CustomError:
        print("This is our custom exception")
    except Exception as e:
        print(" there is some isssue",e)