list1=[78,9,6,20,45,63,77,99,8956,230]
print('list1:',list1,len(list1))

for i in list1:
    print(i)

list2=[x-10 for x in list1]
print(list2)
print(list1)
