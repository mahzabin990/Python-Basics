# Variables & Data Structures I

Done Yet?: Yes
Timeline: June 18, 2023
Exam: June 18, 2023

<aside>
<img src="https://www.notion.so/icons/arrow-northeast_blue.svg" alt="https://www.notion.so/icons/arrow-northeast_blue.svg" width="40px" /> Go To

[Python Master](https://www.notion.so/Python-Master-8530b135b17949e0a328363c74f6a880?pvs=21)

[Road Map](https://www.notion.so/Road-Map-ed62d78a4fc74318bae9cec5b3804e27?pvs=21)

</aside>

# My Tasks

| Title                                                          |
|:---------------------------------------------------------------|
| Watch The Videos Chronologically                               |
| Why would you require type() function? Answer in Notes section |
| Answer the questions beneath Code section                      |

# Resources

| Title                                | URL                          |
|:-------------------------------------|:-----------------------------|
| Bro Code - variables                 | https://youtu.be/LKFrQXaoSMQ |
| Bro Code - Type casting              | https://youtu.be/Qtq83lAoogM |
| John Elder - Variables               | https://youtu.be/w7fpLmOfLXo |
| John Elder - Data Types              | https://youtu.be/d9iBMdSAQWk |
| Tech w/ Tim - Variables & Data Types | https://youtu.be/OFrLs22MDAw |
| type() Function                      | https://youtu.be/OOSTj5aCCCk |

---

# Notes

---

To check a variable’s type if it is in string,integer,boolean or float…

# Code

---

```python

```

# Questions

1. **What is variables used for?**
    
    <aside>
    📝 Answer: Variables are like a bucket. They can store any type of data. Later to bring that data we just need to call the variable. It’s like a reusable container/bucket for storing value.
    
    </aside>
    
2. **How do you write a comment in python? Show a demonstration below**
    
    <aside>
    📝 Answer: We use ‘#’ this sign before a sentence to make any comment in python.
    
    ```python
    #This variable stores data of time dimension in the netcdf file.
    
    ```
    
    </aside>
    
3. **What are different built-in data types in python? Demonstrate these data types and print each using python.**
    
    <aside>
    📝 Answer: Integers,Floats,Strings,Booleans,
    
    ```python
    age=27 #integer
    cgpa=3.39 #float
    name='anika' #string
    online= True #boolean
    
    print(f'Her age is {age}')
    print(f'Her cgpa is {cgpa}')
    print(f'Her name is {name}')
    print(f'Is she online? : {online}')
    
    ```
    
    </aside>
    
4. **Take an integer `76`  store it to a variable and then turn it to a string and store it in another variable. Show the types of both variables**
    
    <aside>
    📝 Paste your code below
    
    ```python
    v_1 = 76
    v_2 = str(v_1)
    print(type(v_1))
    pribt(type(v_2))
    
    ```
    
    </aside>
    
5. **Take any string and store it in a variable. Turn it to a boolean type and store it to another variable. Show the type of the variable confirming that it is boolean type data structure.**
    
    <aside>
    📝 Paste your code below
    
    ```python
    v_1 = 'lira'
    v_2 = bool(v_1)
    print(type(v_2))
    
    ```
    
    </aside>
    
6. **Demonstrate an example of type casting in python.**
    
    <aside>
    📝 Paste your code below
    
    ```python
    age = 21
    v_1 = str(age)
    print(type(v_1))
    ```
    
    </aside>