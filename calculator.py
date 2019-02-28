

print('  === Welcome To The Calculator === \n\n')


while True:
    
    print('\n\n Check these: \n')
    print('  [1] Addition (+)')
    print('  [2] Subtraction (-)')
    print('  [3] Multiplication (*)')
    print('  [4] Division (/)')
    print('  [q] Quit')
    choice = input('You only need to enter the number/operator of the operation: ')

    if choice in ['1','+']:
        print("-- You've choosen addition!\n")
        x = float(input('Enter your first number: '))
        y = float(input('Enter your second number: '))
        print('\nYour result is: '+str(x+y))
        continue_choice = input('\nDo you want to do another operation? (Y/n)')
        if continue_choice in ['y','Y','']:
            continue
        else:
            break

    elif choice in ['2','-']:
        print("-- You've choosen subtraction!\n")
        x = float(input('Enter your first number: '))
        y = float(input('Enter your second number: '))
        print('\nYour result is: '+str(x-y))
        continue_choice = input('\nDo you want to do another operation? (Y/n)')
        if continue_choice in ['y','Y','']:
            continue
        else:
            break

    elif choice in ['3','*']:
        print("-- You've choosen multiplication!\n")
        x = float(input('Enter your first number: '))
        y = float(input('Enter your second number: '))
        print('\nYour result is: '+str(x*y))
        continue_choice = input('\nDo you want to do another operation? (Y/n)')
        if continue_choice in ['y','Y','']:
            continue
        else:
            break

    elif choice in ['4','/']:
        print("-- You've choosen divison!\n")
        x = float(input('Enter your first number: '))
        y = float(input('Enter your second number: '))
        print('\nYour result is: '+str(x/y))
        continue_choice = input('\nDo you want to do another operation? (Y/n)')
        if continue_choice in ['y','Y','']:
            continue
        else:
            break
            

    elif choice == 'q':
        break