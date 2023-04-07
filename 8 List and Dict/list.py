l1=[]
print('l1:',l1,len(l1))
l2=[1,2,3,4,5,6,7,8,9,10]
print('l2:',l2,len(l2))
l3=['Rashi',18,24.11,['rsoftware','mysql','idle']]
print('l3:',l3,len(l3))
l4=[
    'Rashi',
    'Rajesh',
    'shelar',
    2104,
    {'name':'Rashi','age':'18','skill':['python','calculs','statistics']},
    (31.08,21.04,99)
    ]
print('l4:',l4, len(l4))
print()

print('concate')
_5=l1+l2
print('_5:', _5 ,len(_5))
_6=l2+l3+l4
print('_6:',_6,len(_6))
print()

print('Repetition')
l7=l2*3
print(l7)
print('l2:',l2[-8])
print()
print('indexing')
l8=l3[3]
print('l8:',l8,len(l8))
l9=l3[3][1]
print('l9:',l9)
l10=l3[-1][-3]
print('l10:',l10)
l11=l4[-2]['skill'][-1]
print('l11:',l11)
print()

print('slicing')
print('l4:',l4)
l12=l4[1:4]
print('l12:',l12)
l13=l4[2:5]
print('ll3:',l13)
_m1=[
    [21,4,31],
    [99,98,97],
    [17,7,2]
    ]
print('_m1:',_m1,len(_m1))
m2=_m1[-2][-2]
print('m2:',m2)
print()

print('In place change')
print('l4',l4)
l4[-5]='computer'
print('l4:',l4)
print('l4:',l4[-2]['name'])
l4[-2]['name']='raju'
print(l4)
l4[-2]['skill'][0]='java'
print(l4)
l4[-2]['skill'][-1]='dbms'
print(l4)
l14=l2*3
print('l14:',l14)
l15=l14[7:10]
print('l15:',l15)
print(l2)
print('l2:',l2[1])
print('l2:',l2[-2])
print('l2:',l2[-3])
print('l2:',l2[-9])
print('l2:',l2[1:7])

