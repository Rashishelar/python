'''list1=[1,5,6,7,8,9,1,2,5,10,12,15,16]
print('list1: ',list1,len(list1))

for i in list1:
    print(i)

list2=[x+10 for x in list1]
print(list2)
print(list1)
'''

list1=list(range(10))
print(list1)
print()
print()
list2=[x for x in list1 if x%2==1]
print(list2)
