class Person:
          count_instance=0
          def __init__(self,first_name,last_name,age):
                    Person.count_instance+=1
                    self.first_name=first_name
                    self.last_name=last_name
                    self.age=age
          @classmethod
          def count_instances(cls):
                    return f"You have created {cls.count_instance} instances of person class"
          def fullname(self):
                    return f"{self.first_name} {self.last_name}"
print(Person.count_instances())

per1=Person("Khasim","basha",18)
per2=Person("Khasim","basha",18)
per3=Person("Khasim","basha",18)
print(Person.count_instance)
print(per1.fullname())