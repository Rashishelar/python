x=99
y=88
z=77

def test():
    global v
    v=21
    x=4
    print('x:',x)
    print('y:',y)
    print('z:',z)

test()
print('v: ',v)
print('x: ',x)
