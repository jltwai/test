#Make functions here for addition subtraction divion multiplication

def plus(x, y):
    return(x + y)


def minus(x, y):
    return(x - y)


def multiply(x, y):
    return(x * y)


def divide(x, y):
    return(x / y)


def minus_multiply(x, y, z):
    result_minus = minus(x, y)
    result_multi = multiply(result_minus, z)
    return result_multi


def divide_plus(x, y, z):
    result_divide = divide(x, y)
    result_plus = plus(result_divide, z)
    return result_plus


def plus_minus(x, y, z):
    result_plus = plus(x, y)
    result_minus = minus(result_plus, z)
    return result_minus


def multiply_divide(x, y, z):
    result_multiply = multiply(x, y)
    result_divide = divide(result_multiply, z)
    return result_divide


#change below to use the functions instead
print(plus(989, 1298))
print(minus(678, 321))
print(multiply(81, 4))
print(divide(888, 4))

print(minus_multiply(4, 5,6))
print(divide_plus(40, 8, 9))
print(plus_minus(3, 2, 1))
print(multiply_divide(5, 6, 10))
