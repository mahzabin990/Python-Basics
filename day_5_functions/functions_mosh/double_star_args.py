# **args is used to pass keyword arguments whic returns a dictionary

def save_user(**user):
    print(user)

save_user(id=1, name='Lira', age = 27)

# as you can see this returns a dictionary

# to invokw a particular value follow below code:

def save_user(**user):
    print(user['age'])

save_user(id=1, name='Lira', age = 27)