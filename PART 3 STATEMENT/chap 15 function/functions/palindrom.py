def pal(num):
    temp=num
    rev=0
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=num//10

    print(rev)
    if temp==rev:
        print("The number is palindrome")
    else:
        print("The number is ot a palindrome")
                   
num=int(input("Enter the number: "))
pal(num)
