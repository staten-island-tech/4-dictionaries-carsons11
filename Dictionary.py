
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
"item1":{
        "name": "Basketball",
        "price": 29.99,
        "category": "sports",
    },
"item2":{
        "name": "Action_figure",
        "price": 3.99,
        "category": "toys",
    },
"item3":{
        "name": "Phone_charger",
        "price": 1.99,
        "category": "accessory",
    }
}
print ("Welcome to our fabulous thrift shop. Here are the items that you can buy.")
for index, item in enumerate(Thrift_shop):
    print (index, ":", item["name"])
x = input("What would you like to buy?: ")
for y in Thrift_shop:
    if x == Thrift_shop[y]["name"]:
        for z in Thrift_shop["item1"]:
            print (Thrift_shop[y][z]) 








    

