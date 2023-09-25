n = int(input('Enter an even number: '))
half = n // 2

i = 1
while i <= half:
    print('*' * i)
    i += 1

j = half
while j >= 1:
    print('*' * j)
    j -= 1