list1=[1,
       30.50,
       ['python','java'],
       {'name':'Rashi',
        'phone':850762985,
       'skills':['python','c++','java','mysql','.net']},
       (85,55,20,10,
        {'2019':'MI',
         '2020':'CSK',
         '2018':['MI','CSK']})
       ]
print('list1:',list1,len(list1))
list2=list1[-2]
print('list2:',list2)
list3=list1[3]['skills'] [-3]
print('list3:',list3)
list4=list1[-1][-2]
print('list4:',list4)
list5=list1[-1][-1]['2020']
print('list5:',list5,len(list5))
list6=list1[-1][-1]['2018'][1]
print('list6:',list6,len(list6))
list8=[1,2,3,4,5,6,7,8,9,10]
print('list8:',list8,len(list8))
list9=list8[-5:-2]
print('list9:',list9)
list10=list8[-6:]
print('list10:',list10)
list11=list8[:-4]
print('list11:',list11)
list12=list8[2:]
print('list12:',list12)
list13=list8[:]
print('list13:',list13)