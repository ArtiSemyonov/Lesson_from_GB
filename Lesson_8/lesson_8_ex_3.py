def type_variable(func):
    def wrapper(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}')
        result = func(*args)
        return result

    return wrapper


@type_variable
def mul(x, y):
    return x + y


print(mul(1.3, 3))
