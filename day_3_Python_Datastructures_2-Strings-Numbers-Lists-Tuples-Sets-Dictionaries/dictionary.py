## dictionaries allow us to work with key value pair
# key is the unique identifier where we can find our data and the value is the data
student = {'name':'Lira','age':'27','courses': ['Math','Compsci']}
print(student)
#how to call specific key?
print(student['name'])
#integer can also be a key
student = {1:'Lira','age':'27','courses': ['Math','Compsci']}
print(student[1])

# we can also use get method to bring the any key , in this case if we call a key that doesn't exist in the dictionary it will return none. It wont give error.

print(student.get('age'))
print(student.get('phone'))

# using update method we can add/update key values

student.update({'age': '25','phone': '3333-5678'})
print(student)

# we can delete key using del

del student['age']
print(student)

# we can also use pop

popped = student.pop('phone')
print(student)
print(popped)

# to see  keys/values/all we have use len

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# we can also use for loop to see them

for key in student:
    print(key)

for key,value in student.items():
    print(key,value)