class Phone:
          def __init__(self,brand,model_name,price):
                    self.brand=brand
                    self.model_name=model_name
                    self.price=price
          def make_a_call(self,phone_number):
                    print(f"calling {phone_number}....")
          def fullname(self):
                    return f"{self.brand} {self.model_name}"
          def send_message(self):
                    pass #twillio
 #_name # convention of private name
 #__name__ #dundr/magicmethod
phone1=Phone("nokia","1100",1000)
phone1.price=-1111
print(phone1.price)
print(phone1.__dict__)
