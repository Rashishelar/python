#List Operation

print(80*'-')

List1=[]
List2=[9,8,7,6,5,4,3,2,4,9,5,6]
List3=['pointer','Array','files']
List4=[4,2,1,0,90.99,'dictionary','strings','tuples']
List5=[{'enumber':9999,'esalary':150000},9,8,3,(90.92,80,55)]

print(80*'-')

print('List1:',List1,len(List1))
print('List2:',List2,len(List2))
print('List3:',List3,len(List3))
print('List4:',List4,len(List4))
print('List5:',List5,len(List5))

print(80*'-')

print('Append')
List1.append(1)
print('List1:',List1,len(List1))

List2.append(500)
print('List2:',List2,len(List2))

print(80*'-')

print('count')
a1=List2.count(10)
print('List2:',List2,len(List2))
print('List2.count(9)',a1)

a2=List2.count(9)
print('List2:',List2,len(List2))
print('List2.count(9)',a2)

print(80*'-')

print('extend')
List1.extend([2,3,4,5,9,8,1,2,5,3,5,3])
print('List1:',List1,len(List1))

