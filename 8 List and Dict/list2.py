list1=[]
print('list1:',list1,len(list1))
list2=[10,9,8,7,6,5,4,3,2,1,10,9,56,3,5,3,5,3,5,3,10,9,0,7,0,536,55,78,7,8,9,1,0,4,2,5]
print('list2:',list2,len(list2))
list3=['NDA','MPSC','NEET','CET']
print('list3:',list3,len(list3))
list4=[
        'Rashi',
        'Shelar',
        2104,
        99999,50.55,
        {
         'Name':'Rashi',
         'Age':18,
         'Skill':['python','rsoftware','sql','java'],
         'phone':[8956231471,8974561230,7894561230,1234567899,92214537890],
        
            
         }]
print('list4:',list4,len(list4))
print()

print('concate')
list5=list1+list2+list3
print('list5:',list5,len('list5'))
list6=list3+list4
print('list6:',list6,len('list6'))
list16=list3+list2
print('list16:',list16)
print()

print('Repetation')
list6=list4*10
print('list6:',list6,len(list6))
list7=list3*5
print('list7:',list7,len(list7))
list15=list2*15
print('list15:',list15)
print() 

print('indeing')
list8=list4[-1]['Skill'][-4]
print('list8',list8)
list9=list3[2]
print('liat9:',list9)
list10=list3[-4]
print('list10:',list10)
list11=list3[-1]
print('list11:',list11)
print()

print('slicing')
list12=list2[-5:]
print('list12:',list12)
list13=list4[-1]['phone'][-3:-1]
print('list13:',list13)
list14=list4[-1]['phone'][-5:-2]
print('list14:',list14)
list20=list4[-1]['Skill'][-1]
print('list20:',list20)
print()

print('In place change')
list4[-1]['Skill'][-1]=['dbms']
print('list4',list4)
list4[-1]['Skill'][-2]=['.net']
print('list5:',list5)
list4[-1]['Name']='Rakshu'
list1.append('Rashi')
print('list1',list1)
print('list2',list2)
list22=list2.count(10)
print('list22:',list22)
list23=list2.count(5)
print('list23:',list23)
list24=list2.count(3)
print('list24:',list24)
list25=list2.count(9)
print('list25:',list25)
list2.extend((1,2,3))
print('list2:',list2)
list4.extend([999595])
print('list4:',list4)
list3.extend(['GAT'])
print('list3:',list3)
list3.extend(['UPSC'])
print('list3:',list3)
print()

print('Indexing')
list26=list2.index(9)
print('list26:',list26)
print(list3)
list27=list3.index('UPSC')
print('list27:',list27)
list28=list3.pop(-2)
print('list28:',list28,list3)
list2.remove(10)
print('list2:',list2)
list3.reverse()
print(list3)
list2.sort()
print('list2:',list2)
list2.sort(reverse=True)
print('list2',list2)

