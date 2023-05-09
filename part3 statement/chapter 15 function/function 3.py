def rev(num):
    rev=0
    while num !=0:
        r=num%10
        rev=rev*10+r
        num=num//10
        print(rev)

rev(1568)
rev(18)
rev(1986)
rev(2356)
rev(89748)

'''
def fib(n1,n2):
    print(n1)
    print(n2)
    res=0
    while res<=100:
        res=n1+n2
        print(res)
        n1=n2
        n2=res
fib(0,1)

