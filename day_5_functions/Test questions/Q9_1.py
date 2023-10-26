states = ["missisippi", "luiSiana", "fLoRida", "texas", "Alabama"]

def format(x:str):
    y = x.lower()
    string = y[0].upper() + y[1:len(y)-1] + y[-1].upper()
    return string


if __name__ == '__main__': 
    formatted = map(format,states)
    print(list(formatted))

