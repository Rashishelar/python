list1=[80,90,70,60,42,45,10,90,92,21,24]
print('list1:',list1,len(list1))

for i in list1:
    print(i)

list2=[x+10 for x in list1]
print(list2)
print(list1)
