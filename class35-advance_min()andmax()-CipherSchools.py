names=["khasim","basha","chotu"]
# print(max(names))


# names=["khasimbasha","swarna nelatur","chotu"]
# print(max(names,key=lambda item:len(item)))

students={
          "harshit": {"score":92,"age": 90},
          "basha":{"score":95,"age": 68},
          "khasim":{"score":99, "age":75}
}

print(max(students,key=lambda item:students[item]["score"]))




