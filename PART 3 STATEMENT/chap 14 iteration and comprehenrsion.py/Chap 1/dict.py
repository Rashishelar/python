#dict

dict1={'name':'Rashi',
       'Age':18,
       'skill':['python','Java','C'],
       'Phone':(986532014,1234567890,7894561320)
       }
print('dict1',dict1,len(dict1))

i1=iter(dict1)
print(i1)
a1=i1.__next__()
print(a1,dict1[a1])
a2=i1.__next__()
print(a2,dict1[a2])
a3=i1.__next__()
print(a3,dict1[a3])
a4=i1.__next__()
print(a4,dict1[a4])
a5=i1.__next__()
print(a5,dict1[a5])
a6=i1.__next__()
print(a6,dict1[a6])



