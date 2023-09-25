successful = True
for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')


# stops after first attempt due to break

successful = True
for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')
        break

# we want to try three times and tell user that we tried three times but still couldn't do it

successful = False
for number in range(3):
    print('Attempt')
    if successful: #As successful is false it will directly execute elase after for
        print('Successful')
        break 
else:
    print('Attempted 3 times and failed')