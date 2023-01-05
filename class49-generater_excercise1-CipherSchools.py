def even_numbers(a):
          for i in range(1,a+1):
                    if i%2==0:
                              yield(i)
for num in even_numbers(20):
          print(num)
for num in even_numbers(6):
          print(num)
for num in even_numbers(6):
          print(num)