# in this exercise we will learn how can we return func from func

def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func
var = outer_func()
var()


# first we will make func which didnot take anything and again we have to make another func without anything in it
# then print it and comeout from the loop and return the second def func without excute it
# and store it in a variable
# look i dont excute the inner func (second func )
def func(msg):
   def inner():
      print(f'message is {msg}')
   return inner
var = func("hello there !")
var()