# Write a function that accepts two strings. 
# Then it should return a single string where the given strings are separated by a space 
# and the first two characters of each string are swapped.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def manipulated_string(x:str,y:str):
    if len(x) >= 2 and len(y) >=2 :
        a = x.replace(x[:2],y[:2])
        b = y.replace(y[:2],x[:2])
        return a,b
    elif len(y) < 2:
        return       
    
def main():
    string_1 = 'abc'
    string_2 = 'xyz'
    string_3 = 'a'
    print(manipulated_string(string_1,string_2))
    print(manipulated_string(string_2,string_3))

if __name__ == '__main__':
    main()