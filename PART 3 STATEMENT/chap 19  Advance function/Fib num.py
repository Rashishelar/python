num=int(input("Enter the num:"))
def fib(num):
    if num<=1:
        return num
    else:
        return fib(num-1)+fib(num-2)

result=fib(num)
print("result:",result)
