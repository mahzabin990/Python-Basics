courses = ['History','Math','Physics','CompSci']

print(courses)
print(len(courses))
print(courses[0])
# 1 brings the last one
print(courses[-1])
# if u give  a index that doesnt exist u will get a index error
# print(courses[4])
# first index is inclusive and last one is exclusive
print(courses[0:2])
# if we don't give anything at the beginning it will be same
print(courses[:2])
# if we don't give anything at the end it will indicate end
print(courses[2:])
courses.append('Art')
print(courses)

# if you want to add something at a specific index use index
courses.insert(0,'Art')
print(courses)
#we can also insert a list into a list
lira=['girl','harsd-working','beautiful','brave']
courses.insert(0,lira)
print(courses)
# to just add the elements use extend method
courses.extend(lira)
print(courses)
# to remove an item you can use remove method
courses.remove('beautiful')
print(courses)
# if you use pop method then the last element of the list will be removed
courses.pop()
print(courses)
# if you assign it in a variable then it will return the popped item
popped = courses.pop()
print(popped)
print(courses)
# to sort alphabetically or numerically (ascending) use sort method
lor=['Anika','Sabbir','Al-Amin']
lor.sort()
print(lor)

# ascending to descending use reverse
lor.sort(reverse=True)

# we can use sorted function to sort the list

sorted_courses = sorted(lor)
print(sorted_courses)

# to print min/max/sum of a list
nums=[1,2,3,5,7,9,8]
print(min(nums))

#if you want to find a index of a certain value you can use index method for this
print(courses.index('Math'))
# if we want to check if any element is in our list?
print('Art' in courses)
print('Math' in courses)
# to see the all the items of a list we can use for loop
for item in courses:
    print(item)
# using enumerate function we can see the items with their index

for index,item in enumerate(courses):
    print(index,item)

# we can also fix from where to start:
for index,item in enumerate(courses, start=1):
    print(index,item)

# we can use join method to convert list to string
lor=['Anika','Sabbir','Al-Amin']
lor_str = ','.join(lor)
print(lor_str)

# string to list?
new_list = lor_str.split(',')
print(new_list)