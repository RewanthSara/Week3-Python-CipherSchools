class person:
          def __init__(self,first_name,last_name,age):
                    self.first_name=first_name
                    self.last_name=last_name
                    self.age=age
          def full_name(self):
                    return f"{self.first_name} {self.last_name}"
          def is_above_18(self):
                    if self.age>18:
                              return True
p1=person("khasim","basha",24)
# print(p1.first_name,p1.last_name,p1.age)
print(p1.full_name())
print(p1.is_above_18())