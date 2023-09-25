# while loop = execute some code WHILE some conditions remains TRUE

name = input('Enter your name: ')
while name == '':
    print('You did not enter your name')
    name = input('Enter your name: ')
print(f'Hello!{name}')
 