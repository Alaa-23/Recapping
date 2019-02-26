print ('\n\n == Welcome to The While Conditioner == \n\n')

x = int(input('What is your numba?\n ==> '))

print('\n-- Your number is '+str(x))

if x > 5:
    print('And because it is bigger than 5, we will display count down to 0\n')
    while True:
        print(x)
        x -= 1
        if x <= 0:
            print(x)
            print("We've reached 0! BREAAAKING!")
            break

elif x < 5:
    
    print('And because it is smaller than 5, we will display count up to 100\n')
    
    while True:
        x += 1
        
        if x == 100:    
            print(x)
            print("We've reached 100! BREAAKING!!")
            break
        
        if x == 13:
            print('\nFound an even number! I guess I have to skip it!\n')
            continue

        print(x)
        
