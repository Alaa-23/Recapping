print('\n    Welcome to the if conditioner!\n')


x = input ('Enter number \n --> ')



print('\n',type(x),'\n')

if x > 5 and type(x) is int:
    print ('\n-- The number is bigger than 5 AND it is an integer!\n')


elif x > 5 and type(x) is float:
    print ('\n-- The number is bigger than 5!\n-- AND a float!')

elif type(x) is str:
    print ('\nOopsie! It is a string after all!!1\n')

else:
    print ('\n-- The number is smaller than 5!\n')