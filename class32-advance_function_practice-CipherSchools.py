# # def average_finder(l1,l2):
# #           average=[]
# #           for pair in zip(l1,l2):
# #                    average.append(sum(pair)/len(pair))
# #           return average
# # print(average_finder([1,2,3],[4,5,6]))






# def average(*args):
#           # average=[]
#           # for pair in zip(*args):
#           #           average.append(sum(pair)/len(pair))
#           # return average
# average = lambda*args:[sum(pair)/len(pair) for pair in zip(*args)]
# print(average([1,2,3],[4,5,6],[7,8,9]))








def average_function(*args):
          average=[]
          for pair in zip(*args):
                    average.append(sum(pair)/len(pair))
          return average
print(average_function([1,2,3],[4,5,6],[7,8,9]))