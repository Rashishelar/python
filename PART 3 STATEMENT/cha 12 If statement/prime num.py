'''#prime num

num=int(input("Enter the number:"))
counter=0
i=1
if num==0 or num==1:
    print("number is 0 or 1 are not a prime number")
else:
    while i<=num:
        num%i==0
        counter=counter+1
        i=i+1

if counter==2:
    print("The num is prime")
else:
    print("The num is not prime")'''


'''#reverse num

num=int(input("Enter the number: "))
rev=0
while num!=0:
    remainder=num%10
    rev=rev*10+remainder
    num=num//10

print(rev)'''


'''#palindome num

num=int(input("En ter the num: "))
rev=0
temp=num
while num!=0:
    remainder=num%10
    rev=rev*10+remainder
    num=num//10
print('Reverse of a number:', rev)

if temp==rev:
    print("palindrome number")
else:
    print("The num is not palindrome number")'''

'''#even odd

def even_odd():
    num=int(input("Enter the num: "))
    if num%2==0:
        print("The num is even")
    else:
        print("The num is odd")
        
even_odd()'''


'''#Square

a=int(input("Enter the num a:"))
b=int(input("Enter the num b:"))
c=int(input("Enter the num c:"))
d=int(input("Enter the num d:"))
total=a+b+c+d

if total==360:
    print("square")
else:
    print("Not square")'''

'''#Traingle


a=int(input("Enter the num a:"))
b=int(input("Enter the num b:"))
c=int(input("Enter the num c:"))

total=a+b+c

if total==180:
    print("Traingle")
else:
    print("Not Traingle")
    
    
    

    
    
    
