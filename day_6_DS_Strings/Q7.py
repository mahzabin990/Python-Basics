# Write a function that takes in a string and remove characters that have odd index values in the given string


def even_indexed_string(x:str):
        string_2 = x[::2]
        return string_2
    
def main():
    string_1 = 'Iloveyoushifat'
    print(even_indexed_string(string_1))


if __name__ == '__main__':
    main()