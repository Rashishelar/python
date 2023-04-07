s='wireless mouse indexing'
print(s)
print(len(s))
'slicing'
print(s[0:12])
print(s[2:14])
print(s[-13:-6])
print(s[-13:-1])
l=[252,'spam',36.89,42.20,2411]
print(l)
print(len(l))
print(l[0:4])
print(l[-5:])
l.append(321)
print(l)
l.append('Raju')
print(l)
l.pop()
print(l)
d1={
    'fname':'Rashi',
    'lname':'shelar',
    'age':18,
    'job':'CEO of google'
    }
print(d1)
print(d1['job'])
d2={
    'name':{'fname':'Rashi','lname':'shelar'},
    'age':18,
    'job':['dev','finance'],
    }
print(d2)

T=(1,2,3,4,5)
print(T)
T=T + (6,7)
print(T)
T[1]
print(T[1])
print(T[-3])
print(T[0:])
print(T[1:6])
print(T[-7:-3])
print(T[-5:])
