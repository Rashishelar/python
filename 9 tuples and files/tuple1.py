#tuple

tuple1=()
print('tuple1:',tuple1,len(tuple1))

tuple2=(89.22,10,2,63.78)
print('tuple2:',tuple2,len(tuple2))

tuple3=(
        (66,1,2,89),
        'Rashi','Shelar',
        {
          'AGE':18,
          'PHONE':['9820250432','8928629700'],
          'SKILL':['PYTHON','.NET'],
          
        'Population':{
          'India':'17.70 %',
          'China':'18.47 %',
          'United States':'4.25 %',
          'Indonesia':'3.51%',
         }
         }
)
print('tuple3:',tuple3,len(tuple3))
tuple4=tuple3[3]['Population']['China']
print('tuple4:',tuple4)
tuple5=tuple3[-1]['SKILL'][-1]
print('tuple5:',tuple5)
tuple6=tuple3[-1]['Population']['Indonesia']
print('tuple6:',tuple6)
tuple7=tuple3[-1]['SKILL'][-1]
print('tuple7:',tuple7)
tuple8=tuple1+tuple3
print('tuple8:',tuple8,len(tuple8))
tuple9=tuple2*8
print('tuple9:',tuple9,len(tuple9))
tuple10=tuple2[-3:-1]
print('tuple10:',tuple10,len(tuple10))
tuple11=tuple9.count(2)
print('tuple11:',tuple11)
tuple12=tuple9.index(2)
print('tuple12:',tuple12)



    
