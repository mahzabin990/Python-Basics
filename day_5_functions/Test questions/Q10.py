bands = [['british','oasis', 'beatles'], ['american','smiths', 'creed', 'nirvana']]
# Suppose you have a list, bands = [['british','oasis', ‘beatles’], ['american',‘smiths’, ‘creed’, ‘nirvana’]]. 
# Write a function that takes in this list and and returns back a dictionary that has a key of the first element in each list and rest as value

def dictionary(x:list):
    ''' This function takes in a list  and returns back a dictionary that has a key of the first element in each list and rest as value'''
    d=[]
    for i in x:
        d.append({i[0]:i[1:]})
    return d

def asked_solution(x:list):
    d = {}
    for band in x:
        d[band[0]] = band[1:]
    return d
       
def main():
	# print(dictionary(bands))
    print(asked_solution(bands))


if __name__ == '__main__': 
    main()