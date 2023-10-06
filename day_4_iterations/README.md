# Iteration

Done Yet?: Yes


# Resources

| Title | URL |
|-------|-----|
| Socratica Generators | https://youtu.be/gMompY5MyPg?si=ovyznxTe6RQYMVd7 |
| While Loop BroCode | https://youtu.be/rRTjPnVooxE?si=Z2hWdw6PSkjKigB5 |
| Corey Schafer Loops | https://youtu.be/6iF8Xb7Z3wQ?si=3UHsrMaenCvLlZSK |
| For Loops by Mosh | https://youtu.be/94UHCEmprCY?si=7yrUuwRc-U7sT0UA |

---

# Notes

---

**We use loops to create repetition

**#for loops**

```python
for number in range(3):
    print('Attempt')

for number in range(3):
    print('Attempt', number)

for number in range(3):
    print('Attempt', number+1)

for number in range(3):
    print('Attempt', number+1,(number+1)*'.')

for number in range(1,4):
    print('Attempt', number,number*'.')

for number in range(1,10,2):
    print('Attempt', number,number*'.')

# for else

successful = True
for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')

# stops after first attempt due to break

successful = True
for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')
        break

# we want to try three times and tell user that we tried three times but still couldn't do it

successful = False
for number in range(3):
    print('Attempt')
    if successful: #As successful is false it will directly execute elase after for
        print('Successful')
        break 
else:
    print('Attempted 3 times and failed')

#nested loops

for x in range(5):
    for y in range(3):
        print(f'({x},{y})')

#iterables
for x in 'python':
    print(x)

for x in [1,2,3,4]:
    print(x)

#print even numbers in range 1 to 10
for x in range(1,10):
    if x % 2 ==0:
        print(x)
# also print how many even numbers you have ?
count = 0
for x in range(1,10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f'We have {count} even numbers')

# break & continue
nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        break # it means after getting 3 it won't iterate through the list anymore!
    print(num)

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        continue # it means after getting 3 it will iterate through the list anymore!
    print(num)

# while loop
while x < 10:
    print(x)
    x += 1

# break in while loops
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
# infinite loop and how to excape?= press 'ctrl c' to excape
x = 0

while True:
    print(x)
    x += 1

# while loop = execute some code WHILE some conditions remains TRUE

# if else
name = input('Enter your name: ')
if name == '':
    print('You did not enter your name')
else:
    print(f'Hello!{name}')

# while

name = input('Enter your name: ')
while name == '':
    print('You did not enter your name')
    name = input('Enter your name: ') # without this line the code will run infinitely
print(f'Hello!{name}')

# age

age = int(input('Enter your age: '))

while age<0 :
    print('Age can not be negative')
    age = int(input('Enter your age: ')) # without this line you will be caught in infinite loop

print(f'You are {age} years old')
```

# Code

---

```python

```

# Questions

> In each coding section, you first need to run and test the code in your local machine. Then copy the final version of the code then paste it in the answer. You are not allowed to use google or other forms of help in any of the questions below.
> 
1. **What do you understand by loop? Demonstrate all the types of looping that python supports. Also illustrate the key differences between them.**
    
    <aside>
    📝 Answer: 
    **Loop** : A process of executing some code multiple times while/for some conditions are true/false.
    
    **For Loop Example: (a code to print even numbers in range 1 to 10)**
    for x in range(1,10):
        if x % 2 ==0:
            print(x)
    
    **While Loop Example:(Print a person’s age while age can not be negative)**
    age = int(input('Enter your age: '))
    while age<0 :
        print('Age can not be negative')
        age = int(input('Enter your age: ')) # without this line you will be caught in infinite loop
    print(f'You are {age} years old')
    
    **Key Differences:
    
    1. For loop is used when the number of iterations is already known.While loop is used when the number of iterations is Unknown.
    2. In case of no condition, the loop is repeated infinite times.In case of no condition, an error will be shown.**
    
    </aside>
    
2. **Which data structures support loop in python?**
    
    <aside>
    📝 Answer: We can use for loop to iterate lists, tuples, strings and dictionaries in Python. On the other hand, Boolean data structures mostly supports while loop.
    
    </aside>
    
3. **Declare a list that contains the name of 5 states from the USA. Use for loop to go through each states and print the sates, each letter uppercase.**
    
    <aside>
    📝 Answer:
    
    ```python
    # paste your code here
    states = ['Mississippi','Florida','Lousiana','Texas','Washington']
    for state in states :
        print(state.upper())
    ```
    
    </aside>
    
4. **Declare a `string` variable then print each letter in it by using while loop.**
    
    <aside>
    📝 Answer:
    
    ```python
    # paste your code here
    name = 'Anika'
    
    i = 0
    while i < len(name):
        print(name[i])
        i = i+1
    
    # for char in name:
    #     print(char)
    ```
    
    </aside>
    
5. **Write a program that prints the numbers from 1 to n. But for multiples of 3, print `Fizz` instead of the number, and for multiples of 5, print `Buzz`. For numbers that are multiples of both 3 and 5, print `FizzBuzz`. You have to come up with 2 separate solutions. One of them should be done using for loop and the other one should be using while loop.**
    
    <aside>
    📝 Answer-1 “For Loop” solution:
    
    ```python
    # paste your code here
    n = int(input('Enter your number: '))
    
    for i in range (1, n+1):
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)
    ```
    
    </aside>
    
    <aside>
    📝 Answer-2 “While Loop” solution:
    
    ```python
    # paste your code here
    n = int(input('Enter your number: '))
    x = 1
    
    while x < n+1:
    
        if x%3 == 0 and x%5 == 0:
            print('FizzBuzz')
        elif x%3 == 0:
            print('Fizz')
        elif x%5 == 0:
            print('Buzz')
        else:
            print(x)
    
        x = x+1
    ```
    
    </aside>
    
6. **Suppose you have the following text. Create two lists out of the text. One should contain all the apples and the other should contain all the oranges. Finally print out how many apples and oranges you found.**
    
    <aside>
    📝 Answer:
    
    ```python
    
    # paste your code here
    my_text = "apple-orange-spam-orange-notspam-orange-mango-apple-apple-orange-apple-grape-orange-apple"
    fruits = my_text.split('-')
    a = []
    o = []
    for fruit in fruits:
        if fruit == 'apple':
          a.append(fruit)
        elif fruit == 'orange':
           o.append(fruit)
    
    print(f'I found {len(a)} apples')
    print(f'I found {len(o)} oranges')
    ```
    
    </aside>
    
7. **Write a program that asks for an even integer, n. n is the number of lines. The program will then keep printing star (*) in such a manner that, the number of stars increases by 1 in each new line. However the increment goes up until half of n. After half of n, the reverse will happen, ie. the stars will decrease by 1 until the n-th line where number of stars will be 1.** 
    
    **Here is an example for n=10**. **Bellow you see the pattern. For n=10, There are 10 lines here. the first line starts with only 1 star. Then in each line one additional stars are added. However from 7th line the stars keep decreasing by 1 until it reaches to one star at the final line.** **Print the following pattern using loop. If required you can use multiple loops.**
    
    <aside>
    🃏 pattern:
    
    ```
    *
    **
    ***
    ****
    *****
    *****
    ****
    ***
    **
    *
    ```
    
    </aside>
    
    <aside>
    📝 Answer:
    
    ```python
    # paste your code here
    number =int(input('Please, enter your even integer number: '))
    if number%2 == 0:
       x = 1
       n = -4
       while x <= number :
          if x <= (number/2):
            print('*'*x)
          elif x > (number/2) :
            print ('*'*(x-(2*n-1)))
          x = x+1
          n=n+1
    else:
       print('You did not enter even number')
    ```
    
    </aside>
    
8. ********Suppose you have a list, `bands = [['british','oasis', ‘beatles’], ['american',‘smiths’, ‘creed’, ‘nirvana’]]`. Loop through the list. If any of the child lists start with the element `american`, print each elements of that list. Make sure that the American bands are capitalized properly.**
    
    <aside>
    📝 Answer:
    
    ```python
    # paste your code here
    bands = [['british','oasis','beatles'], ['american','smiths', 'creed', 'nirvana']]
    for i in bands:
        if i[0] == 'american':
            for a in i:
              print(a.upper())
    ```
    
    </aside>
    
9. ********Suppose you have some data that contains some features of a house that is for rent. Find out the minimum value of each feature and directly printout the processed data. Below you can see the your initial data and final expected output.******** 
    
    *Note that: You are not allowed to use any direct function, indexing or any hard coded way to find out the minimum.*
    
    <aside>
    🃏 Data:
    
    ```python
    {
    	"rent": [34000, 32000, 50000, 22000, 24000, 27000],
    	"house area": [1350, 1300, 1600, 1000, 1200, 1250],
    	"number of bed rooms": [3, 3, 4, 2, 3, 3],
    	"number of wash rooms": [2, 2, 4, 2, 2, 2],
    	"number of varenda": [3, 3, 4, 1, 2, 3]
    }
    ```
    
    </aside>
    
    <aside>
    🃏 Expected output:
    
    ```python
    {
    	"rent": 22000,
    	"house area": 1000,
    	"number of bed rooms": 2,
    	"number of wash rooms": 2,
    	"number of varenda": 1
    }
    ```
    
    </aside>
    
    <aside>
    📝 Answer:
    
    ```python
    # paste your code here
    house = {
    	      "rent": [34000, 32000, 50000, 22000, 24000, 27000],
    	      "house area": [1350, 1300, 1600, 1000, 1200, 1250],
    	      "number of bed rooms": [3, 3, 4, 2, 3, 3],
    	      "number of wash rooms": [2, 2, 4, 2, 2, 2],
    	      "number of varenda": [3, 3, 4, 1, 2, 3]
            }
    min1 = house['rent'][0]
    for i in range(len(house['rent'])) :
        if house['rent'][i] < min1 : # If the other element is min than first element
          min1 = house['rent'][i]
    min2 = house['house area'][0]
    for i in range(len(house['house area'])) :
        if house['house area'][i] < min2 : # If the other element is min than first element
          min2 = house['house area'][i]
    min3 = house['number of bed rooms'][0]
    for i in range(len(house['number of bed rooms'])) :
        if house['number of bed rooms'][i] < min3 : # If the other element is min than first element
          min3 = house['number of bed rooms'][i]
    min4 = house['number of wash rooms'][0]
    for i in range(len(house['number of wash rooms'])) :
        if house['number of wash rooms'][i] < min4 : # If the other element is min than first element
          min4 = house['number of wash rooms'][i]
    min5 = house['number of varenda'][0]
    for i in range(len(house['number of varenda'])) :
        if house['number of varenda'][i] < min5 : # If the other element is min than first element
          min5 = house['number of varenda'][i] 
    
    output = {
    	"rent": min1,
    	"house area": min2,
    	"number of bed rooms": min3,
    	"number of wash rooms": min4,
    	"number of varenda": min5
    }
    
    print(output)
    ```
    
    </aside>
    
10. ********Write a program that counts the frequency of words from a given text. Suppose you have the following text. Your output should be a dictionary. The keys of the dictionary should be all the unique words from the text and values should contain the corresponding counts. Also note that, you should remove all the commas `,` and full-stops `.` and semicolons `;` before you start counting the words. All the operations mentioned in the problem should be done programmatically. At the end of the program, print the dictionary.**
    
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
    punctuations = [',', '.', ';']
    refined_text = text
    for puncuation in punctuations:
       refined_text = refined_text.replace(puncuation, '')
    
    words = refined_text.split()
    unique_words = set(words)
    my_list = list(unique_words)
    # print(my_list)
    count = []
    for i in my_list:
       x = words.count(i)
       count.append(x)
    # print(count)
    # print(len(my_list))
    # print(len(count))
    x=0
    d = {}
    while x  < len(my_list):
       key = my_list[x]
       value =  count[x]
       d[key] = value
       x = x+1
    print(d)
    ```
    
    </aside>
