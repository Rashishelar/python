a1=ord('r')
print('a1:',a1)

a2=ord('a')
print('a2:',a2)

a3=ord('s')
print('a3:',a3)

a4=ord('h')
print('a4:',a4)

a5=ord('i')
print('a5:',a5)

l1='Python is everything for everyone'
list1=[]
for i in l1:
    list1.append(ord(i))
print('list1:',list1)

print('-'*80)

l2='Sachmuchaam'
list2=[]
for i in l2:
    list2.append(ord(i))
print('list2:',list2)

print('-'*80)

list3=[i for i in range(21)]
print('list3:',list3)

print('-'*80)

list4=[pow(i,3)for i in range(1,21)]
print('list4:',list4)

print('-'*80)

list5=[i/2 for i in range(1,16)if i%3==1]
print('list5:',list5)

print('-'*80)

list6=[i//3 for i in range(1,16)if i%12==1]
print('list6:',list6)

print('-'*80)

#nested

list7=[i*j for i in range(1,11)for j in range(1,6)]
print('list7:',list7)
print('-'*80)

LIST8=[i+j for i in range(1,3)for j in range(12,15)]
print('-'*80)

print('LIST8:',LIST8)

list9=[i-j for i in range(-8,-10,-1)for j in range(10,15)]
print('list9:',list9)

print('-'*80)

list10=[a/b for a in range(5,8)for b in range(10,21)]
print('list10:',list10)

print('-'*80)

list11=[p//q for p in range(9,6,-1)for q in range(4,5)]
print('list11:',list11)

print('-'*80)

list12=[(c,r) for c in range(4)if c%2==0 for r in range(4) if r%2==1]
print('list12:',list12)

print('-'*80)

list13=[(c,d)for c in range(25) if c//5==0 for d in range(10) if d//2==1]
print('list13:',list13)
