l1=[123,{1,2,3,'Rashi'},[20.85]]
print(l1)
d1={
    'fname':'Rashi',
    'lname':'shelar',
    'Age': 18,
    'job':['dev','manager']
    }
print(d1)
print(d1['fname'])
print(d1['job'][1])
print(len(d1))
l2=[456,[50.58,89.59],12,{7,2,8,6},99999]
print(l2)
print(len(l2))
print(l2[0:])
print(l2[1:4])
print(l2[-4:])
print(l2[3])
l2.pop()
print(l2)

l2=[
    {'fname':'Rashi',
     'lname':'shelar',
     'job':'dev',
     'age':18
     },
    50,60.2,70
    ]
print(l2)
print(l2[0]['fname'])

