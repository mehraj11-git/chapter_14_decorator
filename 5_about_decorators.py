# decorators enhance the functionality of the other func 
# for ex 
# @ use for decorator 
def decorator_func(any_func):
    def wrapper_func():
        print('this is awesome func')
        any_func()
    return wrapper_func
    
@decorator_func
def func():
    print('this is func 1')
var = decorator_func(func)
var()
@decorator_func
def func2():
    print('this is func 2')
func2()
# now i can call them t=and they print it 
# but i want this as well to print
# 'this is awesome func'
# for this we use the decorators 
# decorator are the func who enhance the functionality of other func
# @ we use this func to avoid the lengthy code





