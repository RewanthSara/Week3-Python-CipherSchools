class Person:
          count_instance=0
          def __init__(self,first_name,last_name,age):
                    Person.count_instance+=1
                    self.first_name=first_name
                    self.last_name=last_name
                    self.age=age


per1=Person("Khasim","basha",18)
per2=Person("Khasim","basha",18)
per3=Person("Khasim","basha",18)
print(Person.count_instance)