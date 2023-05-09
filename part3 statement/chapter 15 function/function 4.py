def display(obj):
    if isinstance(obj,str):
        print(type(obj))
        for i in obj:
            print(i,end=' ')
    elif isinstance(obj,tuple):
        print(type(obj))
        for i in obj:
            print(i)
    elif isinstance(obj,dict):
        print(type(obj))
        for i in obj:
            print(i,'->',obj[i])
    else:
        print(type(obj))
        for i in obj:
            print(i)
        


list1=list(range(10))
list2=[1,2,2.23,(125898,5623),{'name':'Raju','age':32}]
tuple1=(15,78,98,65)
s1='everybody'
dict1={
    'name':'Raju Mane',
    'age':32,
    'skill':['c','java','python']
    }

display(list1)
print()
display(list2)
print()
display(tuple1)
print()
display(s1)
print()
display(dict1)
