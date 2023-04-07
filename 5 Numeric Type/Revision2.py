'''
p=print
p('Arithmetic operator')
a1=20
a2=10.5
a3=5.2
a4=10.5
p('a1=20 a2=10.5 a3=5.2 a4=10.5')
a5=a1+a2-a4
p(a5)
a6=a1/a4-a2*a3/a4
p(a6)
a7=a2/a4-a1+a3*a3
p(a7)
a8=a1/a1-a1+a1*a1
p(a8)
a9=a1+a2-a3*a4/a1
p(a9)
a10=-a4/a3*a2-a1
p(a10)
a11=a1/a2*a3!=a4 or a1/a1+a2==a3
print(a11)
a12=a1/a2<a3 and a1*a2/a3!=a2 or -a2>=a2*a1/a1-a2+a3
print(a12)
a13=-a3/a2*a3-a3!=a2 or a3==a1/a3*a3<=a3 or a3-a2-a3>=a3!=a3
print(a13)
a14=-a3*a3-a3==a3 and a2<=-a2-a2-a2
print(a14)
a15=10<11>2>3
p(a15)
a16=-a3/a2>=a3!=a3 and -a3+a3*a2==a2 and -a3==a2*a2>=a1
p(a16)
'''

'''
a1=20
a2=10.5
a3=5.2
a4=10.5
print('a1=20 a2=10.5 a3=5.2 a4=10.5')
a17=a1>a2<a3>a4
print('a1>a2<a3>a4',a17)
a18=a3>a2<a1>a4
print('a3>a2<a1>a4',a18)
a19=a2<a2>a3>a4
print('a2<a2>a3>a4',a19)
a20=a4<a3>a1>a2
print('a4<a3>a1>a2',a20)
a21=a1<a4<a2<a1>a4>a2>a1>a3
print('a1<a4<a2<a1>a4>a2>a1>a3',a21)
'''

'''
print('Division operator')
a1=20
a2=10
print('a1=20 a2=10')
a3=a1/a2
print('True division',a3)
a4=a1/a2
print('floor',a4)
a5=a1//a2
print('exponential',a5)
a6=a1<<a2
print('left shift',a6)
a7=a1>>a2
print('right shift',a7)
print()


print('sets')
print('Union operator')
s1={10,20,30,40,50}
print(s1)
s2={30,40,50,60}
print(s2)
s3=s1|s2
print('union',s3)
s4=s1.union(s2)
print(s4)

print('Intersection operator')
s5=s1&s2
print('Intersection',s5)
s6=s1.intersection(s2)
print(s6)

print('Set difference operator')
s7=s1-s2
print('set difference operator',s7)
s8=s2-s1
print('set difference operator',s8)

print('set symmetric operator')
s9=(s1-s2)|(s2-s1)
print('set symmetric operator',s9)
s10=(s2-s1)|(s1-s2)
print('set symmetric operator',s10)
'''

print('membership test')
a={1,2,3,4,5}
b={3,4,5,6,7}
c={3,4,5,8,9,10}
a.difference(b)
x1=a.difference(b)
print('diference',x1)
x2=a.difference(b,c)
print('differnce',x2)
a.union (b)
x3=a.union(b,c)
print('union',x3)
x4=a.intersection (b,c)
print('intersection',x4)
a.add(15)
x5=a.add(15)
print(x5)
a.pop
x6=a.pop
print(x6)
a.update
x6=a.update

