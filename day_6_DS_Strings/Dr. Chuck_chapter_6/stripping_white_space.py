# sometimes we want to remove white space at the beginning or end of a string
# lstrip() and rstrip() removes white space from laeft and right
# strip() removes both begining and ending white space

greet = ' Hello Bob '
x = greet.lstrip()
y = greet.rstrip()
z = greet.strip()

print(x)
print(y)
print(z)