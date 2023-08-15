def wordFreq():
    string = str(input("Enter a text : "))
    tokens = string.split(" ")
    store = {}
    for i in tokens:
        count = 0
        for j in tokens:
            if i == j:
                count = count + 1
        store[i] = count
    return store

def display( Dict ):
    print("\n\n")
    for i in Dict:
        print(str(i) + "\t\t freq = " + str(Dict[i]))
        
        
Dict = wordFreq()
display(Dict)
