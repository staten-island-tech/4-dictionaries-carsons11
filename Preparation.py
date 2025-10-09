""" def language(x):
    print ("do something")
language("Cadee's computer never seems to work in the morning") """

""" def lang():
    s=0
    t=0
    x = input("Put your sentence here")
    for char in x:
        if char == "s" or char == "S":
            s=s+1
        elif char == "t" or char == "T" :
            t=t+1
    if s >= t:
        print ("French")
    else:
        print ("English")
lang() """


""" def spaces():
    c = int(input("How many parking spaces are there?"))
    x = list(input("Put yesterday's parking spaces here"))
    y = list(input("Put today's parking spaces here"))
    z = 0
    for i in range(c):
        if x[i] == "C" and y[i] =="C":
            z = z + 1
    print (f"There are {z} parking spaces.")
spaces() """


def occupied(n,y,t):
    both = 0
    for i in range(n):
        if (y[i] == "C" and t[i] == "C"):
            both +=1
    return both
print(occupied(5, "CCC..", "C.C.C"))


def HONI():
    