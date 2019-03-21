


def The_Decorator(func):
    def wrap(x):
        print('==========')
        func(x)
        print('==========')
    return wrap

@The_Decorator  
def printer(x):
    print(x)
 

x = input('What do you want to decorate? ==> ')
printer(x)

