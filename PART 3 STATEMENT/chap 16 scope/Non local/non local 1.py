#Non local

w=88
z=20
def f1():
    y=4
    def f2():
        nonlocal y
        y=21
        z=74
        def f3():
            nonlocal z
            z=4
            print('z:',z)
            print('y:',y)
            def f4():
                global w
                w=24
                print('w:',w)
            f4()
            
        f3()
    f2()
f1()
