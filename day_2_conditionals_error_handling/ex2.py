 #Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
rate=10
new_rate=1.5*10
try:
    hours = int(input('Enter hours:')) 
    if int(hours) > 40:
      P = hours*new_rate
      print('Pay:',P)
    elif int(hours)==40 or int(hours) < 40:
      P = hours*rate
      print('Pay:',P)
except:
    print('Error, please enter numeric input') 
 


