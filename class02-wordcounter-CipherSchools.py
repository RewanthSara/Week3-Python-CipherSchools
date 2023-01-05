def word_counter(n):
          d={}
          for i in n:
                    d[i]=n.count(i)
          return d
print(word_counter("khasimbasha"))