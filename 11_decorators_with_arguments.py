# we use this func to pass the argument in a decorator func to call the func 
# no need to make decorator func again n again for string ,list,dict,tuple etc..
# we gonna make one decorator func and change the condition as per the requiremnets
from functools import wraps
def all_data_type(data_type):
    def decorators(any_func):
        @wraps(any_func)
        def inner_func(*args,**kwargs):
            if all([type(i)==data_type for i in args]):
                return any_func(*args,**kwargs)
            print('invalid arguments')
        return inner_func
    return decorators

@all_data_type(str)
def string_join(*args):
    string = ''
    for i in args:
        string+=i  
    return string          
print(string_join('mehraj','sharat'))

# def a func with parameter
# def a second func with parameters 
# add this parametrs in @wraps
# def the inner func with *operators
# and use the list comprehension
# check the condition by using if method
# return the inner func at inner func position 
# and return the second func
# @ in this decorator we have to change as per the condition like the str,tuple,dict etc 
# for that we have to def a func as per you want