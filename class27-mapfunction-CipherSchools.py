# number=[1,2,3,4,5,6,7,8,9]
# def square(a):
#           return a**2
# squares=list(map(square,number))
# print(squares)



# def square(a):
#           return [i**2 for i in number]
# a=list(map(lambda i:i**2 ,number))
# print(a)



# squares_new=[i**2 for i in number]
# print(squares_new)


# names=["abc","abcd","abcde"]
# name=[len(i) for i in names]
# namess=[i for i in names]

# print(map(namess,name))


def square(a):
          return a**2
numbers=[2,3,3,2,3,4,4,3,2]
b=list(map(square,numbers))
print(b)


numbers=[7,5,4,6,4,5,3]
a=list(map(lambda i:i**2,numbers))
print(a)



b=[i**2 for i in numbers]
print(b)



names=["abc","abcd","abcde"]
k=[len(i) for i in names]
length=map(len,names)
for i in length:
          print(i)