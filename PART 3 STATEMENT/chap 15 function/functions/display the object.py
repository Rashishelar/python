#display the object

def display(obj):
    if isinstance(obj,str):
        for i in obj:
            print(i,end="")
    elif isinstance (obj,tuple):
        for i in obj:
            print(i)
    elif isinstance (obj,dict):
        for i in obj:
            print(i,obj[i])
    else:
        print(type(obj))
        for i in obj:
            print(i)


list1=list(range(15))
list2=[20,80.9,45,(66666,4444,1421),'Everybody',{'name':'Rashi','age':18,'skill':['java','python'],}]
tuple1=(89,22,421,2411)
s1='Everybody'
dict1={
        'name':'Rashi',
        'Age':18,
        'phone':[9865320147,7896541230,8791230456]
        }
display(list1)
print()
display(list2)
print()
display(tuple1)
print()
display(s1)
print()
print()
display(dict1)
print()












       
