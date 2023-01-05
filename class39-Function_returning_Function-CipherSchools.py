# def square(a):
#           return a**2

def outer_func():
          def inner_func():
                    print('inside inner func')
          return inner_func()
var=outer_func()

















def outer_func2(mesg):
          def inner_func():
                    print(f"message is {mesg}")
          return inner_func
var= outer_func2("hello love the day.bro")
var()

































