#Nested for

for i in range(1,21):
    for j in range(1,11):
        for k in range(2,31):
            for l in range (1,11):
                result1=i*j
                result2=k*l
                result3=result1*result2
                print(result3)
                print(k,'x',l,'=',result3)
                print(i,'x',j,'=',result1)
            print('\n')
