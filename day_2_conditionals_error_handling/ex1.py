#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
rate=10
new_rate=1.5*10
hours = int(input('Enter hours:'))

if int(hours) > 40:
    P = hours*new_rate
    print('Pay:',P)
elif int(hours)==40 or int(hours) < 40:
    P = hours*rate
    print('Pay:',P)