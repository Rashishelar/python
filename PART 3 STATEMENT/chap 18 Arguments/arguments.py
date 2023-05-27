#By positional 

b=40
def f1(a):
    a=66
    print(a)

f1(b)
print(b)
print('-'*50)

l1=['python',2.5,10,80]
x=20


def f2(a,b):
    b[-1]=99
    b[1]='java'
    print(b)
    print(a)

f2(x,l1[:])
print(l1)
print(x)
