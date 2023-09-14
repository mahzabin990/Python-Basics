student = {'name':'Lira','age':'27','courses': ['Math','Compsci'],'status':'married','country':'BD','session':'spring'}
y=[]

for key,value in student.items():
    x = key,value
    y.append(x)
print(y[2])

for key in student:
    print(key)

del student['session']
student.update({'hair': 'long'})
print(student)
  