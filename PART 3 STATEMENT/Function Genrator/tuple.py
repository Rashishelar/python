#Tuple

def _tuple1():
    result=0
    t1=(10,20,30,40,50)
    for i in t1:
        result=result+i
        print('result:',result,'i:',i)
        yield result

b=_tuple1()
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

