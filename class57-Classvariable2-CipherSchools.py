# class laptop:
#           def __init__(self,brand,model_name,price):
#                     self.brand=brand
#                     self.model_name=model_name
#                     self.price=price
#                     self.fullname=brand + " "+ model_name
#           def apply_discount(self,num):
#                     # self.price
#                     off_price=(num/100)*self.price
#                     return self.price-off_price
# l1=laptop("hp","eswsdcsc",50000)
# print(l1.brand,l1.price,l1.model_name)
# # print(l1.apply_discount(30))
# class circle:
#           pi=3.14
#           def __init__(self,radius):
#                     self.radius=radius
#           def circumference(self):
#                     return 2*circle.pi*self.radius
# circle1=circle(4)
# circle2=circle(7)
# print(circle1.circumference())






class laptop:
          disc=5
          def __init__(self,brand,model_name,price):
                    self.brand=brand
                    self.model_name=model_name
                    self.price=price
                    self.full_name=brand + " " + model_name
          def discount(self):
                    a=(self.disc/100)*self.price
                    return self.price-a
lap1=laptop("lenovo","ideapadgaming3",40000)
# print(lap1.brand,lap1.model_name,lap1.full_name)
lap1.disc=10
print(lap1.discount())
print(lap1.__dict__)












































































