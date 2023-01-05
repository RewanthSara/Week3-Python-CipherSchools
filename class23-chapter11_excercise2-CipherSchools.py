def func(l,**kwargs):
          if kwargs.get('reverse_str') == True:
                    return [name[::-1].title() for name in l]
          else:
                    return [name.title() for name in l]
names=["khasim","basha"]
print(func(names))









































# def func(a,**kwargs):
#           if kwargs.get("reverse_str"==True):
#                     return [name[::-1].title() for name in l]
#           else:
#                     return [name.title()  for name in l]
# names=["khasim","basha","chotu"]
# print(func(names))