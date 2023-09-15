# Python Conditionals

Done Yet?: Yes

<aside>
<img src="https://www.notion.so/icons/arrow-northeast_blue.svg" alt="https://www.notion.so/icons/arrow-northeast_blue.svg" width="40px" /> Go To

[Python Master](https://www.notion.so/Python-Master-8530b135b17949e0a328363c74f6a880?pvs=21)

[Road Map](https://www.notion.so/Road-Map-ed62d78a4fc74318bae9cec5b3804e27?pvs=21)

</aside>

# My Tasks

* Learn Conditionals following the videos with the book

# Resources

| Title                             | URL                                       |
|:----------------------------------|:------------------------------------------|
| 0. Chapter-3 of Book by Dr. Chuck | https://www.py4e.com/html3/03-conditional |
| 1. Dr. Chuck - Conditionals 1     | https://youtu.be/2aA3VBdcl6A              |
| 2. Dr. Chuck - Conditionals 2     | https://youtu.be/OczkNrHPBps              |
| 3. CS - Conditionals & Booleans   | https://youtu.be/DZwmZ8Usvnk              |

---

# Notes

---

…

# Code

---

```python

```

# Questions

---

> In each coding section, you first need to run and test the code in your local machine. Then copy the final version of the code in the answer. You are not allowed to use google or other forms of help in any of the questions below.
> 

1. **What is meant by Boolean Datatype?**
    
    <aside>
    📝 Answer: Boolean datatypes are expressions expressing true or false. They belong to a class bool.
    
    </aside>
    
2. **What are boolean operators?**
    
    <aside>
    📝 Answer: Boolean operators take boolean inputs and return boolean results.
    
    </aside>
    
3. **List out all possible boolean operators available in python.**
    
    <aside>
    📝 Answer: and,or,not
    
    </aside>
    
4. **Demonstrate a sample execution of each of the boolean operators in python. You must use comments to properly explain each line.** 
    
    <aside>
    📝 Answer:
    
    ```python
    # and opeerator
    x=5
    y=True
    
    if x>2 and y: #both of theb statements are true .
      print (True)
    else:
      print('not satisfied your condition')
    #or operator
    x=5
    y=False
    
    if x>2 or y: #only one statement is true and other is wrong
      print (True)
    else:
      print('not satisfied your condition')
    #not operator
    x=5
    y=False
    
    if x>2 and not y:# y is false, in this statement not true makes it false
      print (True)
    else:
      print('not satisfied your condition')
    
    ```
    
    </aside>
    
5. **What does the term *Exception* mean in python?**
    
    <aside>
    📝 Answer: errors that occur after processing the test.
    
    </aside>
    
6. **What is a *Traceback Error*? Mention two possible ways to handle errors in python?**
    
    <aside>
    📝 Answer: A traceback error can occur when there is a exception in the code. I can handle this error using try/except method.
    
    </aside>
    
7. **Demonstrate an example of *Exception* in python.**
    
    <aside>
    📝 Answer:
    
    ```python
    
    Name='Lira'
    try:
        N=int(Name)
    except:
        N=-1
    print('My',N)
    ```
    
    </aside>
    
8. **Complete the 1st exercise in the book.**
    
    <aside>
    📝 Answer:
    
    ```python
    rate = 10
    new_rate = 1.5*10
    hours = int(input('Enter hours:'))
    
    if int(hours) > 40:
        P = hours*new_rate
        print('Pay:',P)
    elif int(hours)==40 or int(hours) < 40:
        P = hours*rate
        print('Pay:',P)
    ```
    
    </aside>
    
9. **Complete the 2nd exercise in the book.**
    
    <aside>
    📝 Answer:
    
    ```python
    rate=10
    new_rate=1.5*10
    try:
        hours = int(input('Enter hours:')) 
        if int(hours) > 40:
          P = hours*new_rate
          print('Pay:',P)
        elif int(hours) == 40 or int(hours) < 40:
          P = hours*rate
          print('Pay:',P)
    except:
        print('Error, please enter numeric input')
    
    ```
    
    </aside>
    
10. **Suppose you work at sales in a coffee shop, meaning you take orders from customers. Your coffee shop only sales coffee and chocolate drinks. To order a coffee the customer needs to be 18 or above. Otherwise he/she is allowed to have a chocolate drink.** 
    
    **Convert this scenario into python code. Also make sure that this code can also handle errors. So if any error occurs, it should print a custom message that you wrote. For example, if anyone enters a name instead of a number, your program should print something like: “Please enter the number correctly”.**
    
    <aside>
    📝 Answer:
    
    ```python
    # Paste your code here.
    
    try:
        customer_age=int(input('Please enter the customer age:'))
        
        if  int(customer_age) >= 18:
          print('We are serving both coffee and chocolate milk.')
        elif  int(customer_age) < 18:
          print('We are serving only chocolate milk.')
    except:
        print('Please enter the number correctly')
    ```
    
    </aside>
    

---