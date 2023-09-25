# paste your code here
my_text = "apple-orange-spam-orange-notspam-orange-mango-apple-apple-orange-apple-grape-orange-apple"
x = my_text.split('-')
a = []
o = []
for i in x:
    if i == 'apple':
      a.append(i)
    elif i == 'orange':
       o.append(i)

print(f'I found {len(a)} apples')
print(f'I found {len(o)} oranges')