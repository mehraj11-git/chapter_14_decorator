# but here there is a small prblmm in this func
# suppose if our func takes the argument than this decorator func need to be change
# for that we use *args and **kwargs method

def decorator_func(any_func):
    def wrapper_func(*args,**kwargs):
        print('this is awesome func')
        return any_func(*args,**kwargs)
    return wrapper_func

@decorator_func
def func(a):
    print(f'this is func with argument {a}')

func(7)


# suppose if ur func contain more than one argument


@decorator_func
def add(a,b):
    return a+b
print(add(2,3))  #this will give the result NONE
# to get the proper answwer we have to return the any_func

# we learn the using the *operators and about returning the func
