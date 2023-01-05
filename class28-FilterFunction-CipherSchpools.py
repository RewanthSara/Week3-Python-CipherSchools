# def is_even(a):
#           return a%2==0
# numbers=[1,2,3,4,5,6,7,8,9]
# evens=[]
# naan=tuple(filter(is_even,numbers))         
# print(naan)









# numbers=[32,234,345,3,432,5,34232,5,2,43]
# numb=list(filter(lambda i:i%2!=0,numbers))

# print(numb)



# new_evens=[i for i in numbers if i%2==0]
# print(new_evens)





















def is_even(a):
          return a%2==0

numbers=[3,4,5,6,7,8,9,9,8,7,6,5]
b=list(filter(lambda i:i%2==0,numbers))
print(b)

j=[i for i in numbers if i%2==0]
print(j)
