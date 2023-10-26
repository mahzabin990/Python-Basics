# lamda function = function written in 1 line using lamda keyword accepts any number of arguments, but only has one expression.(think of it as a shortcut)(useful if needed for a short period of time, throw-away)

# lamda parameters : expression

# def double (x) :
#     return x * 2

# print (double(5))

# one parameter

double = lambda x:x * 2
print(double(5))

# two parameters

multiply = lambda x,y : x* y
print(multiply(6,8))

# three parameters 

add = lambda x,y,z : x+y+z
print(add(5,6,7))

# string parameters
 
full_name = lambda first_name, last_name : f'My name is {first_name} {last_name}'
print(full_name('Bro','Code'))

# conditional

age_check = lambda age:True if age >= 18 else False
print(age_check(12))
print(age_check(18))

