'''
s1="Everybody in this country should leran programming"
print("s1: ",s1,len(s1))
i=0
while i<len(s1):
    print(s1[i])
    i=i+1

list1=[1,2,'Raju',(1,2,5)]
i=0
while i<len(list1):
    print(list1[i])
    i=i+1
print()
print()

tuple1=(1,2,5,{'name':'Raju Mane','skill':['python','java']},(1,2,5,23.23))
i=0
while i<len(tuple1):
    print(tuple1[i])
    i=i+1
'''

dict1={'name':'Raju Mane','skill':['python','java']}
a2=list(dict1.keys())
i=0
while i<len(a2):
    print(dict1[a2[i]])
    i=i+1
    

