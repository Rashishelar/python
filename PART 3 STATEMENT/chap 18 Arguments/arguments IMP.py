#add tuple
def add_type(args):
    result=0
    for i in range(len(args)):
        for j in range(len(args[i])):
            result=result+args[i][j]
    return result

tuple1=(2,4,3,5,6,8)
tuple2=(10,20,30,40,50)
tuple3=(9.8,4,5,65)
def add_tuple(*pargs):
    print(pargs)
    result=add_type(pargs)
    print("additional of",type(pargs),result)

add_tuple(tuple1,tuple2,tuple3)
'''
#Add list

list1=[20,3,5,5,8]
list2=[8,9,8,9,8,9,8]
list3=[2,10,50,90,80,7]
'''

        
