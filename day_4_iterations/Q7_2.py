n = int(input('Enter an even number: '))
half = n // 2

i = 1

while i <= n:
    if i <= half:
        print('*' * i)
    elif i > half:
        print('*' * (n - i + 1))
    
    i += 1
    