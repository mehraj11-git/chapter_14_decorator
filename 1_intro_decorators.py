# before you understand the decorator u muat have the func understanding
# this method make the python unique
 

def square(a):
    return a**2
s= square(7)
print(s)
# suppose if u donot call the func in square 
s=square
print(s(7))
# actually both varaibale and square are same 
# you can use s or square this give the same result
# we can know the name of the variable by this method .__name__

print(s.__name__)
print(square.__name__)
print(s)
print(square)
# it means that both are same
