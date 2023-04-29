products={"table" : "стол",
          "school" : "школа",
          "apple" : "яблоко",
          "phone" : "телефон",
          }
print(products)
print("---------------------------------------------")
del products ["school"]
print(products)
print("---------------------------------------------")

products["phone"]=["abrakataba"]
print(products)
print("---------------------------------------------")
products["smarphone"] = "смартфон"
print(products)

friends={"nurlan":10,
         "amir":13,
         "timofey":12,
         "daniyar":13,
         }
print(friends)
del friends["daniyar"]
print(friends)
friends["java"]=[5]
print(friends)