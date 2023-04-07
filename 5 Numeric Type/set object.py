print('set object')
s1={11,12,13,14,15,16}
print(s1)
s2={15,16,17,18,19}
print(s2)
s3=s1.union(s2)
print('union',s3)
s4= s1 & s2
print('intersection',s4)
s5=s1.intersection(s2)
print(s5)
s6=s1-s2
print('set difference',s6)
s7=s2-s1
print('set difference',s7)
s8=(s1-s2)|(s2-s1)
print('set symmetric',s8)
print()

print('set object')
s1={10,20,30,40,50}
print(s1)
s2={30,40,50,60,70,80}
print(s2)
s3=s1.union(s2)
print(s3)
s4= s1 & s2
print('intersection',s4)
s5=s1.intersection(s2)
print(s5)
s6=s1-s2
print('set difference',s6)
s7=s1
