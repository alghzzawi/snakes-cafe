from os import pread
from statistics import mean
from tempfile import tempdir


print("""
******************************************
**      Welcome to the Snakes Cafe!     **
**      Please see our menu below.      **
**                                      **
**  To quit at any time, type "quit"    **
******************************************
Appetizers
----------
wings
vookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

**************************************
**  What would you like to order?   **
**************************************
""")

menu = [{
    "type": "Appetizers",
    "name": [
        'wings',
        'vookies',
        'Spring Rolls'
    ]
},
    {
    "type": "Entrees",
    "name": [
            'Salmon',
            'Steak',
            'Meat Tornado',
            'A Literal Garden'
    ]
},
    {
    "type": "Desserts",
    "name": [
            'Ice Cream',
            'Cake',
            'Pie'
    ]
},
    {
    "type": "Drinks",
    "name": [
            'Coffee',
            'Tea',
            'Unicorn Tears'
    ]
}]

def add_to_order(orders,order):
    
    allmenu=[]
    for i in menu:
        for j in i['name']:
            allmenu.append(j)
    
    while order.lower() != "quit":

        if order in allmenu:
            orders.append(order)
            pirnt_orders(allmenu,order)
            order=input(">")
        else:
            print(f'there is no {order} available in menu')
            order=input(">")
    
            

arr=[0,0,0,0,0,0,0,0,0,0,0,0,0]

def pirnt_orders(allmenu,order):
    meal=''
    index = allmenu.index(order)
    arr[index]+=1
    idxs = [idx for idx, val in enumerate(arr) if val != 0] # Array of indecies

    if len(idxs) == 1 :
        number_meals = arr[idxs[0]]
        meal = allmenu[idxs[0]]
        print (f"** You got {number_meals} of {meal} have been added to your order")
    else:
        temp = ''
        for idx in idxs:
            number_meals = arr[idx]
            meal = allmenu[idx]
            temp += f' and {number_meals} of {meal} ' # and 1 of cake and 1 of wings and 1 of tea
        print(f" You got{temp[4:] } have been added to your order") # 4 to skip the first and


if __name__ == "__main__":
    orders=[]
    order=input(">")
    add_to_order(orders,order)