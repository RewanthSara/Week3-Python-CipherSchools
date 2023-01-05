# fruits=["grapes","mango","apple"]
# fruits2=("grapes","mango","apple")
# fruits3={"grapes","mango","apple"}
# print(sorted(fruits))
# print(sorted(fruits3))



guitars=[
          {"model":"yamahaf310","price":8400},
          {"model":"faith naptune", "price":50000},
          {"model":"faith apollo venus" , "price": 35000},
          {"model":"taylor 814ce", "price": 450000}
]



print(sorted(guitars,key =lambda items:items["price"],reverse=True))


