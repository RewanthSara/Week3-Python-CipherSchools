numbers1=[2,4,9,8,10]
numbers2=[1,2,3,4,5,6]
# a=[i for i in numbers1 if i%2==0]
# print(a)

# num=[]
# for i in numbers1:
#           if i%2==0:
#                     num.append(True)
# print(num)
# print(all([True,, True, True, True]))

print(any([i%2==0 for i in numbers1]))

