states = ["missisippi", "luiSiana", "fLoRida", "texas", "Alabama"]

x = map(lambda x : (x.lower())[0].upper() + (x.lower())[1:len(x)-1] + (x.lower())[-1].upper(), states)

if __name__ == '__main__': 
    print(list(x))