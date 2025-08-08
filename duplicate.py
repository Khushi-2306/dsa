lists=[1,1,3,4,4,4,4,4,4,8,9,10,10,11]
print("occurencens of each element")
for item in set(lists):
    print(item,"occurs",lists.count(item),"times")
unique_list=list(set(lists))
print("list after removing duplicates:",unique_list)
