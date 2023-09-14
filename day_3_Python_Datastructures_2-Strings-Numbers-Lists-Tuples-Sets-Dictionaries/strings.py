message = 'My name is Anika Mahzabin'

print(message)

# if there is a 's in your string then use " " this

message = "Lira's world"
print(message)

# if there is a quote in your string then use ' ' this

message = 'Shams said, "Donot disturb me".'
print(message)

#using len function one can get the length of the string

message = 'Hello, World!'
print(len(message))
print(message[0])

#first index is inclusive and last index is exclusive(not included)

print (message [0:3])

#If you don't specify the first index it will automatically take the first-slicing

print(message[:3])

#If you don't specify the last index it will automatically take the last-slicing

print(message[0:])
#we can manupulate a string as lower,upper,append,replace,find,count
new_message = message.lower()

print(new_message)

new_message = message.upper()

print(new_message)

#count words
new_message = message.count('Hello')
print(new_message)

#count letter
new_message = message.count('l')
print(new_message)

#find will say from where/which index a letter or a word starts
#find letter
new_message = message.find('l')
print(new_message)

#find word (returns -1 if it can't find)
new_message = message.find('Hello')
print(new_message)

# replace method takes two arguments, first what i want to replace, second with what i am replacing

new_message = message.replace('Hello','Hi')
print(new_message)

 # adding strings - method 1
greeting = 'hello'
name = 'lira'
 
message = greeting + ', '+ name

print(message)

 # string formatting - method 1
new_message = '{},{}. Welcome!'.format(greeting,name)

print(new_message)

 # string formatting - method 3 (f string method, widely used , most popular, can be only used in 3.6 or higher)

new_message = f'kire {name}, {greeting} nai khobor nai ken tor'

print(new_message)
 #as u can use placeholder inside here so u can do the operations here too this is a very good thing.

new_message = f'kire {name.upper()}, {greeting} nai khobor nai ken tor'

print(new_message)

# to sse how many methods can be used with a string we can use dir function
print(dir(name))

#we can also use help function to know more about string methods

print(help(str))