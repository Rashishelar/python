# prime number or not
num=int(input("enter the number: "))
counter=0
i=1
if num==0 or num==1:
    print("number 0 or 1 is not prime")
else:
    while i<=num:
        if num %i==0:
            counter=counter+1
        i=i+1



if counter==2:
    print("prime number")
else:
    print("not prime number")

