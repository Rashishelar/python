#dict

dict1={}
print('dict2:',dict1,len(dict1))

dict2={
        'name':'Rashi',
        'Age': 18,
        'phones':[8956231470,4567891234,1324567890,9874563120],
        'skils':['python','c','.net'],
      
        'Exams':{
          'NEET':['NCERT','NEET FINGERTIPS','NTA BIOLOGY'],
          'NDA':['Pathfinder','Mission NDA','SSB Interview'],
          'MPSC':['India Since Independence'],
          'MBBS':['An Insiders Guide to Clinical Medicine','Medical physiology','BIochemistry'],

         'course':{
            'Engineering':['marine','chemical', 'civil', 'electrical' ,'mechanical', 'engineering'],
            'Professional Courses':['B.Sc','B.SC cs','B.SC.IT','B.TECH']

        }
        }
         }
print('dict2:',dict2,len(dict2))
print()

print('Indexing')
dict3=dict2['Exams']['MBBS'][-2]
print('dict2:',dict3)
dict4=dict2['Exams']['course']['Professional Courses'][-1]
print('dict4:',dict4)
dict5=dict2['Exams']['course']['Engineering'][-1]
print('dict5:',dict5)
dict6=dict2['phones'][-4]
print('dict6:',dict6)
dict7=dict2['Exams']['NDA'][-1]
print('dict7:',dict7)
print()
print('slicing')
dict8=dict2['phones'][0:1]
print('dict8:',dict8)
dict9=dict2['Exams']['course']['Engineering'][-6:-3]
print('dict9:',dict9)
dict10=dict2['Exams']['MBBS'][-3:]
print('dict10',dict10)
dict11=dict2['Exams']['NDA'][0:1]
print('dict11:',dict11)
dict12=dict2['skils'][-3:-1]
print('dict12:',dict12)
print()

dict13=dict2.get('name')
print('dict13:',dict13)
dict14=dict2.get('phones')
print('dict14:',dict14)
dict15=dict2.get('skils')
print('dict15:',dict15)
dict16=dict2.get('Exams')
print('dict16:',dict16)
dict17=dict2.get('course')
print('dict17:',dict17)
print()

list1=dict2.items()
print('list1:',list1)
list2=list(dict2.items())
print('list2:',list2)
list3=list(dict2.keys())
print('list3:',list3)
list4=list(dict2.values())
print('list4:',list4)

a1=dict2.pop('Exams')
print('a1:',a1)
a2=dict2.popitem()
print('a2:',a2)
a3=dict2.setdefault('skils')
print('a3:',a3)
print()
