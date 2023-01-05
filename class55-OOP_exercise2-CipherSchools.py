class laptop:
          discount1=10
          def __init__(self,brand,model_name,price):
                    self.brand=brand
                    self.model_name=model_name
                    self.price=price
          def discount(self):
                    less=(laptop.discount1/100)*self.price
                    return self.price-less
l1=laptop("LENOVO","IDEAPAD GAMING 3",60000)
print(l1.brand,l1.model_name,l1.price)
print(l1.discount())