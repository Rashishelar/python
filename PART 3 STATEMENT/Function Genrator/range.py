#Range

def _r1():
    result=0
    for i in range(10):
        result=result+i
        print('result:',result,'i:',i)
        yield result

r=_r1()
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())












