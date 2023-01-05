def func (a,b):
          return a+b/2
print(func(4,2))













def funct(*args):
          total=0
          for num in args:
                    total+=num
          return (total)
l=[32,23,34,54,34,33]
print(funct(*l))











def functio(**kwargs):
          print(kwargs)
          print(type(kwargs))
print(functio(name="kjhasim basha",ahe=29))















