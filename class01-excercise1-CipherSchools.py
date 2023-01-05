def cube_finder(n):
          b={}
          for i in range(1,n+1):
                    b[i]=i**3
          return b
print(cube_finder(5))