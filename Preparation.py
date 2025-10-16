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



def password(x):
    uppercase = 0
    lowercase = 0
    digits = 0
    if len(x) >= 8 and len(x) <= 13:
        for char in x:
            if char.islower():
                lower += 1 
            elif char.isupper():
                upper += 1 
            elif char.isdigit():
                digits += 1
    if lowercase >= 3 and uppercase >= 2 and digits >= 1:
        print ("Valid")
    if x < 8 or x > 12:
        print ("Invalid")
password(44531)

def wizard(o,n, duels):
    owner = o
    number_of_owners = 1
    for i in duels:
        if duels[1] == owner:
            owner = duels[0]
            number_of_owners += 1
    for i in range(n):
        if duels[i][1] == owner