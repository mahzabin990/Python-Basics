n = int(input('Enter your number: '))
x = 1

while x < n+1:

    if x%3 == 0 and x%5 == 0:
        print('FizzBuzz')
    elif x%3 == 0:
        print('Fizz')
    elif x%5 == 0:
        print('Buzz')
    else:
        print(x)

    x = x+1




