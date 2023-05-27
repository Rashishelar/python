'''list1=[10,20,30,40,50,60]
def mylist(list1):
    if not list1:
        return 0
    else:
        return list1[0]+mylist(list1[1:])

result=mylist(list1)
print("result: ",result)'''


'''
list1=[10,20,30,40,50,60]
list2=[50,40,20,1,2,3]
def mylist(list1,list2):
    if not (list1 and list2):
        return 0
    else:
        return list1[0]+list2[0]+mylist(list1[1:],list2[1:])

result=mylist(list1,list2)
print("result: ",result)'''
#@by makrand salvi,raju mane,rashi shelar,omkar sarvardekar,aryan parle,dipti shah,
list1=[10,20,30,40,50,60]
list2=[50,40]
list3=[1,2,3,4,5,4]
list4=[15,26,56,58,59,60]
list5=[15,18,19,10,20,30]
def f1(*pargs):
    list1=list(pargs)
    print(list1,range(len(list1)))
    result=0
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            result=result+pargs[i][j]
    return result

result=f1(list1,list2,list3,list4,list5)
print(result)












    

