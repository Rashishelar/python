'''def fetch(obj,index):
    return obj[index]

z=[1,2,3,4]
print(fetch(z,3))
print(fetch(z,4))


def fetch(obj,index):
    return obj[index]
z=[1,4,5,]

try:
    a1=fetch(z,3)
except ZeroDivisionError as e:
    print(e)
print("Zero")'''

def div(x,y):
    return x/y

try:
    a1=div(10,8)
    print(a1)
except Exception as e:
    print(e)
