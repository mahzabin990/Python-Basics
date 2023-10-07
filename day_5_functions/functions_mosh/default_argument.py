def increment(number,by=5):
    return number + by

# default word argument (basically fixing an argument value in the begining but it can be changed invoking the function)

# default

print(increment(2)) # as I haven't mentioned the increment it will take default 5 

# changed

print(increment(2,1))

# on another note, default parameters will be in the last after the required parameters