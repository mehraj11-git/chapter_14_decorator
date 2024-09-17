# func returning func(closure)
# for ex : if we wanna return the square we can easily make
# if we wanna return the cube we can easily make the func 
# but now we gonna make the single func who return the cube,sqaure whatever you want

# first define the func and add parameter
# again define the func and add parameter
# and return them


def two_power(x):   #3
    def inner(n):   #2
        return n**x
    return inner
# now here we take the cube of the numbers

cube = two_power(3)
print(cube(5))

# here we do the square of the number 
square = two_power(2)
print(square(4))