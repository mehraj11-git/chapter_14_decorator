# map func

def square(a):
    return a**2
l = [1,2,4,6]
print(list(map(square,l)))

def my_map(func,l):
    new_list=[]
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(square,l))
print(my_map(lambda a : a**3,l))


# in this exercise first we take the item of the l into func
# for that we have to start the for loop in l
# and make a empty list (new_list =[]) cuz,we have to append the func item in that list 
# we can use lambda func

# list comprehension method
def my_map2(func,l):
    return[func(item) for item in l]

print(my_map2(lambda a : a**3,l))