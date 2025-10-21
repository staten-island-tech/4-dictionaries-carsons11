
""" item1 = {"sad":"you"}
shopping = [
    "item1" = "happy";
]
     """
""" """ 
""" student = {
    'name':'Cadee',
    'age' : '15',
    'grades' : (80,90,100)

}
print (student['name']) """

Thrift_shop = {
    "Basketball": {
        "name": "Basketball",
        "price": 29.99,
        "category": "sports",
    },
    "Action Figure": {
        "name": "Action Figure",
        "price": 3.99,
        "category": "toys",
    },
    "Phone Charger": {
        "name": "Phone Charger",
        "price": 1.99,
        "category": "accessory",
    }
}
print ("Welcome to our fabulous thrift shop. Here are the items that you can buy.")
for i in Thrift_shop:
    print (Thrift_shop[i]['name'])
cart = []
price_cart = []
a = input("Would you like to buy anything? Yes or No: ")
while a == "Yes":    
    b = input("What would you like to buy?")
    cart.append(b)
    price_cart.append(Thrift_shop[b]["price"])
    print (f"This is your total: {price_cart}")
    if a == "No":
        print(sum(price_cart))
    c = input("Would you like to buy anything else? Yes or No: ")
if c == "Yes":
    a == "Yes"
elif c == "No":
    a == "No"




""" x = input("What would you like to buy?: ")
for y in Thrift_shop:
    if x == Thrift_shop[y]["name"]:
        for z in Thrift_shop["item1"]:
            print (Thrift_shop[y][z])  """








    

