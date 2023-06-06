def catch1(d1,d2):
    result1=d1//d2
    print('catch1:',result1)
    def catch2(e1,e2):
        result2=e1**e2
        print('catch2:',result2)
    return catch2

