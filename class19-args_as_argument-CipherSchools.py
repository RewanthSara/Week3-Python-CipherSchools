def multiply_names(*args):
          multiply=1
          print(*args)
          for i in args:
                    multiply*=i
          return multiply
nums=[32,43,34,24]
print(multiply_names(*nums))