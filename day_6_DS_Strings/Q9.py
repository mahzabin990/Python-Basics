# Write a python script that takes in a phone number as integer and produces a string where country calling code of Bangladesh 
# is provided at appropriate position and format it in international phone number format. You should also include the sim provider
#  name in front of the string too. The function should be able to handle typical 10 digit phone numbers used in Bangladesh. 
# For the sake of this problem only implement logic for “Grameenphone”, “Robi”, “Teletalk” or “Banlalink”. 
# If phone number of any other number of digits, format or sim operator is provided, the function should return None. 
# Break your workflow into 2 or more functions as required. For example, the approach can be defining a function that
#  takes the raw input and returns the formatted phone number without mentioning the sim operator name and another function
#  to add operator name in front of the processed string. Then combine everything in another function that will be executed. 
# You are allowed to use the following Wikipedia page as reference but no googling is allowed. Some examples are provided too.


# Phone Number: 1711594594
# Expected Output: "Grameenphone: +880 1711-594594"

# Phone Number: 24444
# Expected Output: None

# Phone Number: 1950111111
# Expected Output: "Banglalink: +880 1950-111111"

# Phone Number: 8801711594
# Expected Output: None

# def phone_number(x:int):
#     if x[0:2] == '13' or x[0:2] == '17' :
#         print(f'Grameenphone: +880{x}')
#     elif x[0:2] == '14' or x[0:2] == '19' :
#         print(f'Banglalink: +880{x}')
#     elif x[0:2] == '15'  :
#         print(f'TeleTalk: +880{x}')
#     elif x[0:2] == '16' or x[0:2] == '18' :
#         print(f'Robi: +880{x}')

def phone_number(x):
    output = None
    if len(x) == 10:
        if x[0:2] == '13' or x[0:2] == '17' :
            output =  'Grameenphone: +880'+' '+x[0:4]+'-'+x[4:]
        elif x[0:2] == '14' or x[0:2] == '19' :
            output =  'Banglalink: +880'+' '+x[0:4]+'-'+x[4:]
        elif x[0:2] == '15'  :
            output =  'TeleTalk: +880{x}'+' '+x[0:4]+'-'+x[4:]
        elif x[0:2] == '16' or x[0:2] == '18' :
            output =  'Robi: +880{x}'+' '+x[0:4]+'-'+x[4:]
    return output

    
def main():
    x = input('Enter your number: ')
    answer = phone_number(x)
    print(answer)

if __name__ == '__main__':
    main()