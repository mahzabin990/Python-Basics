age = int(input('Enter your age: '))

while age<0 :
    print('Age can not be negative')
    age = int(input('Enter your age: ')) # without this line you will be caught in infinite loop

print(f'You are {age} years old')