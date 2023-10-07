# we use *args to pass multiple arguments
def multiply(*numbers):
    print(numbers)
multiply(2,3,4,5)

# we can see this code prints a touple, so we can apply loop here too

def multiply(*numbers):
    total=1
    for number in numbers:
         #total = total*number
         total *= number
    return total
print(multiply(2,3,4,5))

# so this code actually multiplies what we pass