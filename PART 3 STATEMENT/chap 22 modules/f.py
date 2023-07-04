def add(p,q):
    result=p+q
    print('add:',result)
    def sub():
        result=p-q
        print('sub:',result)
        def mul():
            result=p*q
            print('mul:',result)
            def div():
                result=p/q
                print('div:',result)
                def mod():
                    result=p%q
                    print('mod:',result)
                    def R1():
                        result=p<q
                        print('R1:',result)
                        def R2():
                            result=p>q
                            print('R2:',result)
                            def R3():
                                result=p<=q
                                print('R3:',result)
                                def R4():
                                    result=p>=q
                                    print('R4:',result)
                                    def R5():
                                        result=p==q
                                        print('R5:',result)
                                        def R6():
                                            result=p!=q
                                            print('R6:',result)
                                            def L1():
                                                result=p+q and p*q
                                                print('L1:',result)
                                                def L2():
                                                    result=p/q or p-q
                                                    print('L2:',result)
                                                    def L3():
                                                        result=p%q and p+q
                                                        print('L3:',result)
                                                        def L4():
                                                            result=p<q or p>=q
                                                            print('L4:',result)
                                                            def L5():
                                                                result=p<=q and p>=q
                                                                print('L5:',result)
                                                                def L6():
                                                                    result=p==q or p!=q
                                                                    print('L6:',result)
                                                                    def L7():
                                                                        result=not p/q and p<=q
                                                                        print('L7:',result)
                                                                        def L8():
                                                                            result=not p//q or p*q
                                                                            print('L8:',result)
                                                                        L8()
                                                                    L7()
                                                                L6()
                                                            L5()
                                                        L4()
                                                    L3()
                                                L2()
                                            L1()
                                        R6()
                                    R5()
                                R4()
                            R3()
                        R2()
                    R1()
                mod()
            div()
        mul()
    sub()
add(10,20)
                                                                    
                                                                
