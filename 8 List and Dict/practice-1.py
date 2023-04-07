#list

l1=[]
print('l4:',l1,len(l1))

l2=[1,2,3,4,5,6,7,8,9,10]
print('l2:',l2, len(l2))

l3=['marks','submission','assignments',['subjects','department','students'],150]
print('l3:',l3, len(l3))

l4=[
    'Rashi',
    2411,
    {'ename':'Rashi','eid':2411,'enumber':9999,'subjects':['DSA','DM','PYTHON']},
    (9999)
    ]
print('l4:',l4,len(l4))

print()

#concate

print('concate')

l5=l3+l4
print('l5:',l5,len(l5))


l6=l2+l3+l4
print('l6:',l6,len(l6))

print()

#Repetition

print('Repetition')

l7=l1*5
print('l10:',l7,len(l7))

l8=l2*10
print('l8:',l8,len(l8))

l9=l3*10
print('l9:',l9,len(l9))

l10=l4*10
print('l10:',l10,len(l10))

print()

#indexing
print('indexing')

l11=l2[-5]
print('l11:',l11)

l12=l3[3][1]
print('l12:',l12)

l13=l3[-4]
print('l13:',l13)

l14=l4[-2]['subjects'][-2]
print('l14:',l14)

print()


#slicing

print('slicing')

print('l4:',l4)

l15=l4[2:4]
print('l15',l15,len(l15))

L16=l4[-4:-1]
print('L16:',L16,len(L16))

print()

#Matrix
print('Matrix')

m1=[
    [15,22,34],
    [70,80,90],
    [1,2,3]
    ]

print('m1:',m1,len(m1))

M2= m1 [-2][-3]
print('M2:',M2)


