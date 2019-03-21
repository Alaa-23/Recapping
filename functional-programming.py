def do_twice(func,arg):
    return(func(func(arg)))

def add_five(x):
    return x + 5 

print (do_twice(add_five,5))