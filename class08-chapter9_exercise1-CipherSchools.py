def reverse(l):
          return [name[::-1] for name in l]
print(reverse(["abc","tuv","xyz"]))

def reverse(l):
          list=[]
          for name in l:
                    list.append(name[::-1])
          return list
print(reverse(["abc","tuv","xyz"]))