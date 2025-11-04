def personality(x):
    if x % 10 == 0:
        return "x ends with 0"
    else:
        return "x doesn't end with 0"

def random_dancing(a, b, c):
    return (a + b) * c
#--------------------------------------#

def multiplier(n): #just look
    return lambda x: n * x

if __name__ == '__main__':
    lamb_personality = lambda x: "x ends with 0" if x % 10 == 0 else "x doesn't end with 0"
    print(lamb_personality(25), personality(25))

    a = 1; b = 2; c = 3
    result = (lambda x, y, z: (x + y) * z)(a, b, c)
    print(result, random_dancing(a, b, c))
    #-----------------------------------#

    print(f"Test: {multiplier(2)(5)}")
    doubler = multiplier(2)
    tripler = multiplier(3)
    print(f"Lamb Test: {doubler(5)}")
    print(f"Lamb Test: {tripler(5)}")