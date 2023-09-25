number =int(input('Please, enter your even integer number: '))
if number%2 == 0:
   x = 1
   n = -4
   while x <= number :
      if x <= (number/2):
        print('*'*x)
      elif x > (number/2) :
        print ('*'*(x-(2*n-1)))
      x = x+1
      n=n+1
else:
   print('You did not enter even number')
   
     
