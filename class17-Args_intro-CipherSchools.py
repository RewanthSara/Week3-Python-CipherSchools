def total(a,b):
          return (a**b)
print(total(5,2))




def total(*args):
          print(args)
          print(type(args))
print(total(23,432,42,322.243,42,242,545,43))



def keyword(*khasimbasha):
          return sum(khasimbasha)
print(keyword(21,1223,2311,2314))