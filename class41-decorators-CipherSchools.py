
def decorator_function(any_function):
          def wrapper_function():
                    print("this is awesome function")
                    any_function()
          return wrapper_function
def func1():
          print("this is function `1`")
# this function is awesome
@decorator_function
def func2():
          print("this is function `2`")
# this function is awesome
var=decorator_function(func1)
var()
func2()




def decorator_functon(any_function):
          def wrapper_function():
                    print("this is awesome function")
                    any_function()
          return wrapper_function
def fun1():
          print("hello.....chotu bro")
def fun2():
          print("hello,,,,,,....... khaju bro")

var=decorator_function(fun2)
var()




































