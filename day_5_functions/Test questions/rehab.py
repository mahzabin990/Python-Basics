from Q12 import sort, punc


def main():
    my_text = "I, therefore, pray and hope that you'll love me back."
    result = punc(my_text, punctuations=[',', '.', ';', '\''])
    print(result)

if __name__ == '__main__':
    main()
