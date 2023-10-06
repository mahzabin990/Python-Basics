# How to create a function?

#
# def <function name>(arguments):
#   '''Write a doc string here. Briefly mention what the function does''' 
#   your code
#   optional return
#
# if you don't use return, the function will
# by default return None
#

# Here's a normal function
def foo(a):
    '''takes a, and modifies it, then
    return it'''
    output = f"This is a foo named: {a}"
    return output

# Example-2: A bit more realistic example
# Write a function for finding area of a circle

def get_area(radius, pi=3.14):
    '''radius: radius of circle
    returns the area'''
    a = pi * radius**2
    return a

def calculate_property(radius, property="area", pi=3.14):
    if property == 'area':
        return pi * radius ** 2
    elif property == "dia":
        return radius * 2
    elif property == "peri":
        return 2 * pi * r

# Demonstration of keyword arguments
def greet(name="user"):
    return f"Hi {name}"

def main():
    # print(get_area(12, pi=3.1416))
    # print(greet("Anika"))
    print(calculate_property(12, property="dia", pi=3.141))



if __name__ == "__main__":
    main()
