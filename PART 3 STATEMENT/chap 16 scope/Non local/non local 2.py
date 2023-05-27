#Non local

a=19
b=20
c=21
def f1():
    p=4
    def f2():
        nonlocal p
        p=10
        print('p:',p)
        def f3():
            global a
            a=11
            print('a:',a)
            def f4():
                global b
                b=12
                print('b:',b)
                def f5():
                    global c
                    c=13
                    print('c:',c)
                f5()
            f4()
        f3()
    f2()
f1()
