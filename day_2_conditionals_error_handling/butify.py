# # and opeerator
# x = 5
# y = True

# criteria_is_meet = x>2 and y

# if criteria_is_meet: #both of theb statements are true .
#   print (True)
# else:
#   print('not satisfied your condition')

try:
    customer_age=int(input('Please enter the customer age:'))
    if int(customer_age)==18 or int(customer_age) > 18:
      print('We are serving both coffee and chocolate milk.')
    elif  int(customer_age) < 18:
      print('We are serving only chocolate milk.')
except:
    print('Please enter the number correctly')