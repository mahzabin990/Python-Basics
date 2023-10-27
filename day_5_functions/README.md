# Functions

Done Yet?: Yes

Learning Objectives

- DRY
- Functions
- Arguments
- Args and kwargs
- Lambda
- Convert scattered code to function
- If name = main
- Recursion
- Decorators
- Map function with callback



# Resources

|# |Title|URL|
|---|-----|---------|
|1| DRY Concept: Don’t Repeat Yourself.|https://youtu.be/IGH4-ZhfVDk |
|2| Functions - Mosh|https://youtu.be/u-OmVr_fT4s?si=6R4hN0MEMOaR0Rkp |
|3| Functions - Corey Schafer|https://youtu.be/9Os0o3wzS_I?si=Rpui0c6izpLwfbvx |
|4| Lambda - BroCode|https://youtu.be/YestSrXCqY8?si=CRxtbY1TrYOmb6Y8 |
|5| Recursion |https://youtu.be/m1Fjdnj_Mds?si=iuvk7yM-Nv8X0O-c |
|6| If __ name __…|https://youtu.be/NB5LGzmSiCs?si=Ii8QiLsKpPmHQfui |
|7| dir() and help() - Tech with Tim|https://youtu.be/jjh_P5wg-ww?si=V1sXRJqIGNaRy4O0 |

---

# Notes

---

# **DRY - Don’t Repeat Yourself…**

# **parameters : input that we define for our function**

# **arguments: actual value for a given parameter**

```python
def greet(first_name,last_name):
    print (f'Hi {first_name} {last_name}')
    print('Welcome aboard.')

greet('Anika','Mahzabin')

# here first_name, last_name are parameters
# Anika, Mahzabin are arguments
```

# Two types of function :

1- perform a task | example : print function

2- return a value | example : round function

***** Why use return? = If you use return then you can store the value in a variable.**

****** if you don’t use return then if you want to store the function in variable the value will be none**

# I sound complicated, check below:

# Type -1 :

```python
def greet(name):
    print(f'Hi! {name}')
x = greet('Anika')
print(x)

# it will print x as a none but will print(inside the function) the string
```

# **Type - 2 :**

```python
def greet(name):
    return f'Hi! {name}'

x = greet('Anika')
print (x)

# it will print x as a string
```

# Keyword argument

```python
def increment(number,by):
    return number + by
    result = increment(2,1)
print(result)

# key word argument (basically fixing an argument value while invoking the function)

print(increment(2,by = 1))
```

# Default argument

we use it when we want to set some default argument values in the function that can be changed while invoking the function

```python
def increment(number,by=5):
    return number + by

# default word argument (basically fixing an argument value in the begining but it can be changed invoking the function)

# default

print(increment(2)) # as I haven't mentioned the increment it will take default 5 

# changed

print(increment(2,1))

# on another note, default parameters will be in the last after the required parameters
```

# *args

```python
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
```

# **args

```python
# **args is used to pass keyword arguments whic returns a dictionary

def save_user(**user):
    print(user)

save_user(id=1, name='Lira', age = 27)

# as you can see this returns a dictionary

# to invokw a particular value follow below code:

def save_user(**user):
    print(user['age'])

save_user(id=1, name='Lira', age = 27)

```

# Scope

# scope refers to where a variable is defined

# String method on function

```python
def hello_func():
    return 'Hello Function!'

print(hello_func().upper())
```

# Doc string

```python
'''Write a doc string here. Briefly mention what the function does''' 
#   your code
#   optional return
def get_area(radius, pi=3.14):
    '''radius: radius of circle
    returns the area'''
    a = pi * radius**2
    return a

```

# **Python lamda**

```python
# lamda function = function written in 1 line using lamda keyword accepts
#                  any number of arguments, but only has one expression.
#                  (think of it as a shortcut)
#                  (useful if needed for a short period of time, throw-away)

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
```

# Recursion

```python

# With recursion you can invoke the same function within that function
def EvenNums(num):

   #print(num)

    if num == 2:
        return num
    else:
        return EvenNums(num-2)
    
print(EvenNums(8))

def EvenNums_2(num):

    print(num)

    if num == 2:
        return num
    else:
        return EvenNums_2(num-2)
    
EvenNums_2(8)

# Shams's example
def fact_rec(x):
    if x==1:
        return 1
    elif x>1:
        return x * fact_rec(x-1)
    
print(fact_rec(5))
```

# Dir_Help

```python
import pandas as pd
# print(help(pd))
# print(dir(pd))

# print(help(pd.read_csv))

print(pd.read_csv('heart-disease.csv'))
```

# Main Guard

```python
def multiply(x,y):
    print(__name__)
    return x*y

if __name__ == '__main__':
    print(multiply(6,9))
```

# Code

---

```python
# Mosh Exercise:
# Mosh Exercise:
# if the input is only divisible by 3 then it will give fizz
# if the input is only divisible by 5 then it will give buzz
# if the input is divisible by both 5 and 3 then it will give fizzbuzz
def fizz_buzz(input):
```

Lamda

# Questions

> In each coding section, you first need to run and test the code in your local machine. Then copy the final version of the code then paste it in the answer. You are not allowed to use google or other forms of help in any of the questions below unless explicitly specified in the question itself.
> 
1. **What do you understand by function? How would you define one? How do you invoke a function?**
    
    <aside>
    📝 Answer: I think python functions are very similar like math functions, where I can perform some operations and return the result value also can print it. We usually invoke a function using it’s defining name with passing an argument inside a parenthesis. Invoking a function also refers to calling a function.
    
    ****
    
    </aside>
    
2. **What is the DRY concept and it’s benefits? How functions can help to align with DRY concept?**
    
    <aside>
    📝 Answer: DRY means Don’t Repeat yourself. And it helps to keep the code short and simple. Functions help to get done some steps together just invoking it which helps to prevent the code repetition eventually aligns with the DRY concept.
    
    ****
    
    </aside>
    
3. **Is it possible to define a function without a return statement? If so, what would the function return?** 
    
    <aside>
    📝 Answer: ~~It is possble to define a function without a return statement if the main objective of that function is printing something unless that function will return none.~~
    
    Correct Answer: Yes. It is possible to define a function without a return statement. In that case the function will return `None`
    
    </aside>
    
4. ************What do you understand by arguments of a function? What is the keyword argument?************
    
    <aside>
    📝 Answer:
    
     Arguments are basically the parameters that we are passing through a function.
    
     key word argument (basically fixing an argument value while invoking the function) Example:
    
    ```python
    def increment(number,by=1):
        return number + by
    result = increment(2,1)
    print(result)
    
    print(increment(2,by=5))
    ```
    
    </aside>
    
5. **What is an anonymous function? Demonstrate an example.**
    
    <aside>
    📝 Answer:  Lambda functions are anonimous functions as while creating them it’s not necessary to define a name.
    
    Example :
    
    ```python
    add = lambda x,y : x+y
    print(add(5,7))
    ```
    
    </aside>
    
6. **What is the purpose of using  `if __name__ == '__main__':` in python?**
    
    <aside>
    📝 Answer: **`if __name__ == '__main__':` In my understanding the purpose of it is to prevent running some codes which are not necessary when we are using the program as a import module.**
    
    </aside>
    
7. **Demonstrate a generalized work flow of “Python Main Guard Convention”.** 
    
    <aside>
    📝 Answer:
    
    ```python
    def divide(x,y):
    	z = x/y
    	return z
    
    def main():
    	**print(divide(90,9))**
    
    **if __name__ == '__main__':
    		main()
    
    # here the 90/9 will not be executed when we we will 
    # import this code as a module in another program. 
    # That's why main guard is used.**
    ```
    
    </aside>
    
8. ****************************************************Write a function that calculates factorial of a given number. Execute the function by following the main guard convention. You need to come up with 2 different solutions, one should be using a loop another one should be using recursion.****************************************************
    
    <aside>
    📝 Answer using Loop:
    
    ```python
    
    # paste your code here
    def factorial(x):
        result =1
        for i in range(1, x+1):
            result = result * i
        return result
    
    if __name__ == '__main__':   
        print(factorial(5))
    ```
    
    </aside>
    
    <aside>
    📝 Answer using Recursion:
    
    ```python
    
    # paste your code here
    def factorial(x):
        if x==1:
            return 1
        elif x>1:
            return x * factorial(x-1)
    
    if __name__ == '__main__': 
    	print(factorial(5))
    ```
    
    </aside>
    
9. **Explore the built-in `map` function from the internet. Now apply the map function on the following list in such a way that makes the first and the last character of each element upper case and the rest should be smaller case. Then printout the newly created object.**
    
    <aside>
    🃏 Given:
    
    ```python
    states = ["missisippi", "luiSiana", "fLoRida", "texas", "Alabama"]
    ```
    
    </aside>
    
    <aside>
    📝 Answer:
    
    ```python
    # paste your code here without lambda
    states = ["missisippi", "luiSiana", "fLoRida", "texas", "Alabama"]
    
    def format(x:str):
        y = x.lower()
        string = y[0].upper() + y[1:len(y)-1] + y[-1].upper()
        return string
    
    def main():
    	 formatted = map(format,states)
        print(list(formatted))
    
    if __name__ == '__main__': 
        main()
    # paste your code here with lambda
    
    states = ["missisippi", "luiSiana", "fLoRida", "texas", "Alabama"]
    
    formatted = lambda x : (x.lower())[0].upper() + (x.lower())[1:len(x)-1] + (x.lower())[-1].upper()
    
    x = []
    for s in states:
      x.append(formatted(s))
    
    if __name__ == '__main__': 
        print(x)
    # paste your code here with lambda and map
    
    states = ["missisippi", "luiSiana", "fLoRida", "texas", "Alabama"]
    
    x = map(lambda x : (x.lower())[0].upper() + (x.lower())[1:len(x)-1] + (x.lower())[-1].upper(), states)
    
    if __name__ == '__main__': 
        print(list(x))
    ```
    
    </aside>
    
10. ********Suppose you have a list, `bands = [['british','oasis', ‘beatles’], ['american',‘smiths’, ‘creed’, ‘nirvana’]]`. Write a function that takes in this list and and returns back a dictionary that has a key of the first element in each list and rest as value.**
    
    <aside>
    📝 Answer:
    
    ```python
    # paste your code here
    
    bands = [['british','oasis', 'beatles'], ['american','smiths', 'creed', 'nirvana']]
    # Suppose you have a list, bands = [['british','oasis', ‘beatles’], ['american',‘smiths’, ‘creed’, ‘nirvana’]]. 
    # Write a function that takes in this list and and returns back a dictionary that has a key of the first element in each list and rest as value
    
    def dictionary(x:list):
    	''' This function takes in a list  and returns back a dictionary that has a key of the first element in each list and rest as value'''
    
    	for i in x:
        d = {x[i][0]:x[i][1:]}
        return d
    def main():
    	print(dictionary(bands))
    
    if __name__ == '__main__': 
        main()
    ```
    
    </aside>
    
11. **Write a function that takes infinite numbers of arguments and then printout the sum of the arguments.**
    
    <aside>
    📝 Answer:
    
    ```python
    # paste your code here
    def add(*numbers):
        result = 0
        for num in numbers:
            result += num
        print(result)
    
    if __name__ == '__main__': 
    	add(2,3,4,6,7,8,9,1,3,4,34)
    ```
    
    </aside>
    
12. T**here is a built-in function in python called sorted. This function is used to sort an iterable. You may use internet to explore the function. Below, you have a long text. First, you will write a function that accepts a text and gets rid of the punctuations such as `[',', '.', ';']` and returns back the cleaned text. Then write a function accepts a text and splits the text into words and returns back the words. Write a third function that accepts a list and sorts the list based on the first character of each element and returns back the sorted list.**
    
    As for output, you will print the sorted list. Use the other functions you have written in order to produce such output.
    
    <aside>
    🃏 Text:
    
    ```
    Astronomy is an ancient science, long separated from the study of terrestrial physics. In the Aristotelian worldview, bodies in the sky appeared to be unchanging spheres whose only motion was uniform motion in a circle, while the earthly world was the realm which underwent growth and decay and in which natural motion was in a straight line and ended when the moving object reached its goal. Consequently, it was held that the celestial region was made of a fundamentally different kind of matter from that found in the terrestrial sphere; either Fire as maintained by Plato, or Aether as maintained by Aristotle. During the 17th century, natural philosophers such as Galileo, Descartes, and Newton began to maintain that the celestial and terrestrial regions were made of similar kinds of material and were subject to the same natural laws. Their challenge was that the tools had not yet been invented with which to prove these assertions.
    
    ```
    
    </aside>
    
    <aside>
    📝 Answer:
    
    ```python
    text = 'Astronomy is an ancient science, long separated from the study of terrestrial physics. In the Aristotelian worldview, bodies in the sky appeared to be unchanging spheres whose only motion was uniform motion in a circle, while the earthly world was the realm which underwent growth and decay and in which natural motion was in a straight line and ended when the moving object reached its goal. Consequently, it was held that the celestial region was made of a fundamentally different kind of matter from that found in the terrestrial sphere; either Fire as maintained by Plato, or Aether as maintained by Aristotle. During the 17th century, natural philosophers such as Galileo, Descartes, and Newton began to maintain that the celestial and terrestrial regions were made of similar kinds of material and were subject to the same natural laws. Their challenge was that the tools had not yet been invented with which to prove these assertions.'
    
    def punc(x:str):
        punctuations = [',', '.', ';']
        for puncuation in punctuations:
            x = x.replace(puncuation, '')
        return x
    
    def word(y:str):
        words = y.split()
        return words
    
    def sort(z:list):
        sort_mylist = sorted(z)
        return sort_mylist
    
    def main():
    		refined_text = punc(text)
        words_list = word(refined_text)
        sorted_list = sort(words_list)
        print(sorted_list)
    
    if __name__ == '__main__': 
        main()
    ```
    
    </aside>
