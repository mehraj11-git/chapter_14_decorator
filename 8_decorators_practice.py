from functools import wraps
def print_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        print(f'you are calling {any_func.__name__} functoin')
        print(f"{any_func.__doc__}")
        return any_func(*args,**kwargs)    
    return wrapper_func
@print_func
def add(a,b):
    '''this func takes the two numbers as arguments and return their sum'''
    return a+b
print(add(4,5))

@print_func
def sub(a,b):
    '''this func takes the two numbers as arguments and return their substract'''
    return a-b
print(sub(4,5))