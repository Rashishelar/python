num=int(input("Enter the num: "))
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)


result=fact(num)
print('result',result)
