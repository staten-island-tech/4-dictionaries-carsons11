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


def spaces():
    x = input("Put yesterday's parking spaces here")
    y = input("Put today's parking spaces here")
    z = 0
    for parking in x:
        if x == y and parking == "C":
            z = z + 1
    print (z)
    print (f"There are {z} parking spaces.")
spaces()

