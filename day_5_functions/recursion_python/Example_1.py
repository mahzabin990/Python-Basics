
# With recursion you can invoke the same function within that function

def EvenNums(num):

   #print(num)

    if num == 2:
        return num
    else:
        return EvenNums(num-2)
    
print(EvenNums(8))

def EvenNums_2(num):

    print(num)

    if num == 2:
        return num
    else:
        return EvenNums_2(num-2)
    
EvenNums_2(8)