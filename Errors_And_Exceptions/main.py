import Heirarchy_of_Errors as heirarchy
import statistics

def divide_by_zero(b = 0):
    n = 5

    try:
        result = n / b
    except ZeroDivisionError:
        print("Division by zero error, try passing a different value")
    else:
        print(f"{n} divided by {b} is {result}")
    finally:
        print("Thanks for coming")

def too_many_inputs(words):

    try:
        # var: words, should only have 3 words
        name, title, age = words.split()
    except ValueError:
        print(f"Too many words: {words}")
    else:
        print(f"{name} and {title} and {age}.")

def order_matters():
    print(heirarchy.trap)

def error_messages():
    try:
        print(fake_var) #NameError
    except NameError as error:
        print(f"Test Code: {error}")

    print(fake_var)#NameError

def raise_your_head():
    x = 5
    y = 0

    if y == 0:
        raise ZeroDivisionError("Trap. Trap. Trap.")

if __name__ == '__main__':
    #divide_by_zero(2)
    #too_many_inputs("super cali fragi listic expi ali docius") #VALUE ERROR
    #order_matters()
    #error_messages()
    raise_your_head()