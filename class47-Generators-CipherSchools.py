l=[1,2,3,4]
# i=iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

for num in map(lambda a:a**2,l):
          print(num)
b=(i**2 for i in l)
print(b)



########we can use generator or list......if we use generator the memory taken is less and the fast ness for the programme will be increased...


























