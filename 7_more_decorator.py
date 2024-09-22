from functools import wraps 
def decorator_func(any_func):
    @wraps (any_func)
    def wrapper_func(*args,**kwargs):
        """this is wrapper func"""
        print('this is awesome func')
        return any_func(*args,**kwargs)
    return wrapper_func

@decorator_func
def add(a,b):
    '''this is add func'''
    return a+b
print(add.__doc__)
print(add.__name__)
# here we wasnt to call to the add func but it call the wrap func 
# for that we have to add the 'from functools import wraps
# and then add the @wrap below the first def func 


# we will use the doc string in it
# we can write the doc string by using the triple quote '''esfhheg''' or """rieukeuo""" 
