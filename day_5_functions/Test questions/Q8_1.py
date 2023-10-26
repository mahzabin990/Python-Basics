# Write a function that calculates factorial of a given number. 
# Execute the function by following the main guard convention. 
# You need to come up with 2 different solutions, 
# one should be using a loop another one should be using recursion.

def factorial(x):
    result =1
    for i in range(1, x+1):
        result = result * i
    return result
if __name__ == '__main__':   
    print(factorial(5))