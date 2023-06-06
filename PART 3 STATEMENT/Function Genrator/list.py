#_list_
def _list():
    result=0
    list1=[2,5,8,9,10]
    for i in list1:
        result=result+i
        print('result:',result,'i:',i)
        yield result


a=_list()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


#
        


