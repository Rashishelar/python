'''for i in range(1,91):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)
    print()
'''


#mirror

for i in range(10):
    for j in range(10-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print(j,end=' ')
    print()

num=int(input("Enter the num:"))
for i in range(num):
    for j in range(num-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print(j,end=' ')
    print()
