# in this exercise we learn how long will it takes to run the codes

# timr calculate
# import time 
# t1=time.time()
# print('this is line one')
# x=5
# if x ==5:
#     print('x is equal to 5')
# print('this is line two')   
# print('this is line two') 
# print('this is line two') 
# print('this is line two') 
# print('this is line two')  
# t2=time.time()
# print(t2-t1)

# this method use to check the time 
from functools import wraps
import time
def calculate_time(any_func):
    @wraps(any_func)
    def calci(*args,**kwargs):
        print(f"executing.....{any_func.__name__}")
        t1 = time.time()
        return_value = any_func(*args,**kwargs)
        t2=time.time()
        total_time = t2-t1
        print(f"this function took {total_time} seconds")
        return return_value
    return calci



@calculate_time
def func(n):
    return [i**2 for i in range(1,11)]
func(1000)

# first you have to import the wrap from functools and again import the time
# then define the decorator with any parameter
# and use @wrap to parameter
# then define the inner func with *operators 
# if u want the func name then print it formating using the name func in it
# now take the initial time of func and store it in variable
# now make a new variable with parameter contains the *operators
# now take a final time and store it in variable 
# make a third variable with t2-t1
# return the created varaible apart from the time variable
# next return the inner func without calling it ------>means without () <----this 