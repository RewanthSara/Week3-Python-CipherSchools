from functools import wraps
def decorator_function(any_function):
          @wraps(any_function)
          def wrapper_function(*args,**kwargs):
                    """this is wrapper function"""
                    print("this is awesome function")
                    any_function(*args,**kwargs)
          return wrapper_function
# @decorator_function
# def func1(a):
#           print(f"this is function with argument {a}")
# func1(5)
@decorator_function
def add(c,d):
          """this is add function""" 
          return c+d
print(add.__doc__)



# def first_function(any_function):
#           def second_function(*args):
#                     print("this is veruy important topic")
#                     any_function(*args)
#           return second_function
# @first_function
# def func1(a):
#           print(f"this is the biggest argument ever seen {a}")
# func1(10)










































# # func1(7)
# # func1(8)