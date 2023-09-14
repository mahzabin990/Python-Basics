bands =('oasis', 'beatles', 'smiths', 'creed', 'nirvana')
x = bands[3]
print(x[1])
print(bands[0:3])

# bands[3]='blur'
# this is not possible in case of tuples cause they are immutable , so alternate way is to change it to a list then do the assignment and then again change it to tuple.

y = list(bands)

y[3] = 'blur'

z = tuple(y)

print(z)