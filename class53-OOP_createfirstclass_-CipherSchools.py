class laptop:
          def __init__(self,brand_name,model_name,price):
                    print("IT IS INIT METHOD")
                    self.brand_name=brand_name
                    self.model_name=model_name
                    self.price=price
laptop1=laptop("Lenovo","ideapadd gaming 3",62000)
print(laptop1.brand_name,laptop1.model_name,laptop1.price)
laptop2=laptop("HP","ideapad gaming 4",60000)
print(laptop2.brand_name,laptop2.model_name,laptop2.price)