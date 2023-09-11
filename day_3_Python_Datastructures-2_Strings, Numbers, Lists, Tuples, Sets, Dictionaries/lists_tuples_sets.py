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