"""
from the dictioanry thus created from question_1, 
write a program to accept a key word from  user and return a array of dictinary with item name and its the match rate


eg:

Enter keyword: Pink apple
result:[
    {
        "name": "Granny Smith Apples",
        "mathch rate":80
    }
    {
        "name": "Pink Lady Apples",
        "mathch rate":95
    }
    {
        "name": "Honey Crisp apple",
        "mathch rate":85
    }
]
match rate is percentage

match rate shown below are random not generated using program

Remember user can give any keyword in any format you have to clean it
"""


import json

with open('/home/jazil/exam/rotech_exam/Set 1/data.json','r') as file:
    data=json.load(file)
        
usr_input = input("search a product :")

list =[]
for item in data['items']:
    item_name = (item["name"])
    
    list.append({"name":item["name"]})
    
print(list)