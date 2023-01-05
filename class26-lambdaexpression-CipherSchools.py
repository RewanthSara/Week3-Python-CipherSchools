# /
# print(is_even2(4))
# print(is_even2(5))






# def last(a):
#           return a[-1]
rever=lambda a : a[-1]
print(rever("khasimbasha"))




khas= lambda a,b : a+b
print(khas(3,4))











def limit(s):
          if len(s)>5:
                    return True
          return False







print(limit("hjbdcxhgevbh"))
andi=lambda a:len(a)>5
print(andi("kadj"))




 


# names=["abc","abcdef","khasimbasha"]
# def positiom(l,target):




a=["abc","sadxs","csdcs"]
# pos=0
# for name in a:
#           print(f"{pos}:{name}")
#           pos+=1




# for name,pos in enumerate(a):
#           print(f"{pos}:{name}")


def find_pos(l,target):
          for pos,name in enumerate(l):
                    if name==target:
                              return pos
          return -1
a=["abc","sadxs","csdcs"]
print(find_pos(a,"sadxs"))









