num=int(input("Enter the number: "))
counter=0
i=1
if num==0 or num==1:
    print("number o or 1 is Not prime number")
else:
    while i<=num:
        if num %i==0:
            counter=counter+1
        i=i+1

if counter==2:
    print("prime number")
else:
    print("Not a prime number")
        
        
