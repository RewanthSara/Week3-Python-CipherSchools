import time

# a=[i**2 for i in range(1000000)]
# print(a)
t1=time.time()

b=(i**2 for i in range(10000000000000000))
t2=time.time()
print(t2-t1)