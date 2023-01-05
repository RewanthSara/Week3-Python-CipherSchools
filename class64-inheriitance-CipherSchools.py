class phone:
          def __init__(self,brand,model_name,price):
                    self.brand=brand
                    self.model_name=model_name
                    self.price=price
          def fullname(self):
                    print(f"{self.brand} {self.model_name}")
          def make_a_call(self,number):
                    return f"calling {number}........"
class Smartphone(phone):
          def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
                    phone.__init__(self,brand,model_name,price)
                    self.ram=ram
                    self.internal_memory=internal_memory
                    self.rear_camera=rear_camera

p1=phone("nokia","1100",10000)
sp1=Smartphone("oneplus","10T",40000,"8gb","128gb","64mp")
print(p1.fullname())
print(p1.fullname(),f"and the price is  { p1.price}") 