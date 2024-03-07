"""
create a new  array of dictionary by extracting data from data,json
new dictionay thus created should be as shown below


[
    {
     "name": "Organic Honeycrisp Apples Bag",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    },
    {
     "name": "Granny Smith Apples",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    }
    .
    .
    .
    .
     "
]


Remember to extract all items above illustrated are just sample
"""

import json 

with open('/home/jazil/exam/rotech_exam/Set 1/data.json','r') as file:
    data=json.load(file)
    
    array = []
    for i in data['items']:
        dict ={
            "name":i.get('name'),
            "categories":i.get("categories"),
            "image":i.get("images"),
            "base_price":i.get("base_price"),
            "availability_status":i.get("availability_status")
        }
        array.append(dict)
print(array)