class Person:
          count_instance=0
          def __init__(self,first_name,last_name,age):
                    Person.count_instance+=1
                    self.first_name=first_name
                    self.last_name=last_name
                    self.age=age
          @classmethod
          def from_string(cls,string):
                    first,last,age=string.split(",")
                    cls(first,last,age)
          @classmethod
          def count_instances(cls):
                    return f"You have created {cls.count_instance} instances of person class"
          @staticmethod
          def hello():
                    print("hello this is  khasim ")
          
          def fullname(self):
                    return f"{self.first_name} {self.last_name}"
print(Person.count_instances())

per1=Person("Khasim","basha",18)

per2=Person("Khasim","basha",18)
per3=Person.from_string("Khasim,basha,18")
print(Person.count_instance)
print(Person.hello())