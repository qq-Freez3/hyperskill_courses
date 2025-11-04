import time

#Generally, you want to use return and not print to make code modifiable

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('func takes', round(end - start, 6), 'seconds')
    return wrapper

def practice_decorator(func):
    def wrapper(name):
        print("Before function call")
        return func(name)
    return wrapper

def price_string(func):
    def wrapper(price):
        return "$" + str(func(price))

    return wrapper

def html_title(func):
    def wrapper(*args, **kwargs):
        return f"<title>{str(func(*args, **kwargs))}</title>"
    return wrapper
#----------------------------------------#
@price_string
def get_discount(price): #needs to return instead of print
    return price - (price * 0.10)

@timer
def test_function():
    print("dooba gabba")

@practice_decorator
def business_greeting(business):
    return f"Hello from {business}"

@html_title
def clean_verse(verse):
    string = verse.strip()
    return string

if __name__ == '__main__':
    test_function()
    print(business_greeting("Subaru"))
    print(get_discount(100))
    print(clean_verse("dooba gabba"))