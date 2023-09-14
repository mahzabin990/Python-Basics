cs_courses = {'Art','History','Science','Art'}
print(cs_courses)
# As u see sets throe away duplicates
print('Art' in cs_courses)

art_courses=['Art','Scociology','rocket Science']

# in two sets we can use intersection to get the common courses

print(cs_courses.intersection(art_courses))

# we can also see the difference using difference method

print(cs_courses.difference(art_courses))

# to see all the courses we can use union method

print(cs_courses.union(art_courses))

## How to create empty set???

#emptyset= {}, this is wrong this means empty dictionary

empty_set = set()  
print(empty_set)