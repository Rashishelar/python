
def even_odd():
    i=1
    while i<=10:
        num=int(input("Enter the number: "))
        if num%2==0:
            print("the number is even: ",num)
        else:
            print("the number is odd: ",num)
        i=i+1

even_odd()
