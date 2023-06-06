num=int(input("Enter the num: "))
def f1(name,value):
    for i in range(value):
        print(name.__next__())

list1=(x*y for x in range(1,11) for y in range(1,6))
f1(list1,50)
print()

list2=(x+y for x in range(1,5) for y in range(5,9))
f1(list2,16)
print()

list3=(x for x in range(num))
f1(list3,num)


    
