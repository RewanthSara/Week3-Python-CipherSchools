def to_power(num,*args):
          if args:
                    return [i**num for i in args]
          else:
                    return "You dint pass any args"
nums=[1,2,3]
print(to_power(3,*nums))
print(to_power(1,2))



def to_power(nums,*args):
          if args:
                    return [i**nums for i in args]
          else:
                    return "hey you dint pass anything"
nums=[7,6,5]
print(to_power(2,*nums))




































































