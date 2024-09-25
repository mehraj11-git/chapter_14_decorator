#  def add_all(*args):
#     total = 0
#     for i in args:
#         total+=i
#     return total
# print(add_all(1,2,3,4,5))    

# suppose if there is a list in this line (1) then we have to use the decorator to solve this

from functools import wraps
def only_int_allow(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        data_types=[]
        for i in args:
            data_types.append(type(i)==int)
        if all(data_types):
            return any_func(*args,**kwargs)
        else:
            print('invallid arguments')    
    return wrapper_func


@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total+=i
    return total
print(add_all(1,2,3,4,5,))     #(1) 

# first import the wraps from functools
# def a func with parameters 
# add this parametrs in @wraps
# def the inner func with *operators
# make a empty list
# whenever we make empty list we use for loop ,hence we do
# append the whatever u want to append in the empty list
# check the condition by using if method
# return the inner func at inner func position 

# now the short form of codes we use comprehension method here

from functools import wraps
def only_int_allows(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        if all([type(i)==int for i in args ]):
            return any_func(*args,**kwargs)
        print('invallid arguments') 
    return wrapper_func    
        

@only_int_allows
def add(*args):
    total = 0
    for i in args:
        total+=i
    return total
print(add(1,2,3,4,5,[1,2,6,7]))


