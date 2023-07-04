def div(x,y):
    if y==0:
        raise Exception ("can't divide by zero")
    return x/y

try:
    result=div(10,5)
    print(result)
except Exception as e:
    print(e)

