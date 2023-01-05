def square(a):
          return a**2
s= square 
print(s(7))
print(s.__name__)
print(square.__name__)






def square(a):
          return a**2


l=[1,2,3,4]

def my_map(square,l):
          new=[]
          for ton in l:
                    new.append(square(ton))
          return new
print(my_map(lambda a:a**4,l))




















def square(a):
          return a
l=[1,2,3,4]
b=[i**2 for i in l]
print(square(b))