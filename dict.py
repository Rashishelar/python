dict1={
        'name':'Rashi shelar',
        'age':18,
        'phones':(8521467245,8956237845,7894561232),
        'skills':['python','.net','mysql'],
        'yrs':{
        '2023': 'F.Y.BSC',
        '2024': 'S.Y.BSC',
        '2025': ['Degree','MSC']
        }
    }
print('dict1:',dict1,len(dict1))
dict2=dict1['skills'][-2]
print('dict2:',dict2)
dict3=dict1['yrs']['2025'][-1]
print('dict3:',dict3,len(dict3))
dict4=dict1['phones'][-1]
print('dict4:',dict4)
