s1='Everybody in this country should learn programming'
print('s1: ',s1,len(s1))

for i in s1:
    print(i,end=" ")

list1=[1,2,25.23,(1,2,5),{'name':'Raju Mane','skill':['python','java']}]
print('list1: ',list1,len(list1))

for i in list1:
    print(i)

tuple1=(12536,12,56,'Crazy World',{'name':'Raju Mane','skill':['python','java']})
print('tuple1: ',tuple1,len(tuple1))

for i in tuple1:
    print(i)

print()
print('dict')
dict1={
    'name':'Raju Mane',
    'skill':['python','java','c'],
    'age':32,
    'phone':(7208122920,9833395327)
    }
print('dict1: ',dict1,len(dict1))

for key in dict1:
    print(key,'->',dict1[key])
print()

a1=list(dict1.items())
print(a1)

for key,value in a1:
    print(key,value)

'''
list2=[(1,2),(3,4),(5,6)]
for (i,j) in list2:
    print(i,j)
'''
