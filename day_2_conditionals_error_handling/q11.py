
try:
    custome_no=int(input('please enter the customer number:'))
    if int(custome_no)==18 or int(custome_no) > 18:
      print('We are serving both coffee and chocolate milk.')
    elif  int(custome_no) < 18:
      print('We are serving only chocolate milk.')
except:
    print('Please enter the number correctly')