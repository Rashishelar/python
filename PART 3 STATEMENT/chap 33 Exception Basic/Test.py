def fetch(obj,index):
    return obj[index]

s1='Everybody'
list1=[98,85,7,5,936,222]
tuple1=(1,2,3,4,6,6)

def f1(obj, index):
    try:
        result=fetch (obj,index)
        print(result)
    except Exception as e:
        print(e)

f1(s1,10)
f1(list1,15)
f1(tuple1,9)
