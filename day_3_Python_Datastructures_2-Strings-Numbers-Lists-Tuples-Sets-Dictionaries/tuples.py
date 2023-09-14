## lists are mutable but tuples are immutable
 ## what is mutable??
list_1 = ['History','Math','Physics','CompSci']
list_2 = list_1

list_1[0] = 'Art'

print(list_1)
print(list_2)
#the change made in both the lists

## what is immutable??
tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1
MyList = list(tuple_1)

# Changing 
MyList[0] = 'Art'

# Converting list back to tuple
tuple_1 = tuple(MyList)

print(tuple_1)
print(tuple_2)
#the change made in both the lists
#the change was not made in both the tuples
# tuples doesnot accept item assignment because they are immutable
#it also doesn't support remove,append etc
#it supports other methods without what mutates it