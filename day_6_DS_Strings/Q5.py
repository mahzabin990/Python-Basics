# Write a Python function to get a string made of the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'


def manipulated_string(y:str):
    if len(y) >= 2:
        x = y[:2]+y[-2:] # added the first two and last two characters of given string incase of length of that string is more than 2 chars
        return x
    elif len(y) < 2:
        return       

if __name__ == '__main__':
    string_1 = 'spilled own beans'
    string_2 = 'a'
    print(manipulated_string(string_1))
    print(manipulated_string(string_2))

  