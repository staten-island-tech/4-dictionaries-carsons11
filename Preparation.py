""" def language(x):
    print ("do something")
language("Cadee's computer never seems to work in the morning") """

def lang():
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
lang()

