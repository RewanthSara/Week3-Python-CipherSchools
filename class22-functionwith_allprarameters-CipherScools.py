# def func(name="khasim basha",age="18"):
#           print(name)
#           print(age)
# func("chotu",17)
def fun(name,*args,last_name="khasimbasha",**kwargs ):
          print(name)
          print(args)
          print(last_name)
          print(kwargs)
fun("khasimbasha",4876,42,43,42,a=2,b=5)