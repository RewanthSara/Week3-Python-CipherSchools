# square={num:num**2 for num in range (1,11)}
# print(square)
























square={f"square of {num} is": num**2 for num in range(1,6)}
print(square)
for key,value in square.items():
          print(f"{key}: {value}")





name="khasim basha"
word_count={char:name.count(char) for char in name}
print(word_count)
for key,value in word_count.items():
          print(f"{key}:{value}")



name="KHASIM"
counting={naam:name.count(naam) for naam in name}
print(counting)




















