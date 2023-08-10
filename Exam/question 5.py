list1=[x for x in range(1,11)]
print('list1',list1,len(list1))
print('list1',list1[2:6])
print('list1',list1[-8:-3])

def add(num1,num2):
    result=num1+num2
    return result

f1=add(9,8)
print(f1)

dict1={
        'Name':'Rashi',
        'Age':18,
        'Mobile No':[9856230147,7896541230],
        'Skills':['Python','Django']

    }
print('dict1',dict1)
d1=dict1['Mobile No'][-1]
print(d1)


t1=(50,2,30.90,1e-8)
print('t1',t1)


for i in range(1,11):
    print(i)
