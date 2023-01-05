class Phone:
          def __init__(self,brand,model_name,price):
                    self.brand=brand
                    self.model_name=model_name
                    self.price=price
                    self.complete_specification=f"{self.brand} {self.model_name} and price is {self.price}"
                    
                    if price>0:
                              self.price=price
                    else:
                              self.price=0
                    
          def make_a_call(self,phone_number):
                    print(f"calling {phone_number}....")
          def fullname(self):
                    return f"{self.brand} {self.model_name}"
phone1=Phone("Nokia","1100",-1000)
print(phone1.brand)
print(phone1.model_name)
phone1.price=500
print(phone1.complete_specification)
