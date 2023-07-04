def mul(x,y):
    result=x*y
    print('mul:',result)
    def div():
        result=x/y
        print('div:',result)
        def add():
            result=x+y
            print('add:',result)
            def sub():
                result=x-y
                print('sub:',result)
                def floor():
                    result=x//y
                    print('floor:',result)
                    def mod():
                        result=x%y
                        print('mod:',result)
                    mod()
                floor()
            sub()
        add()
    div()
mul(-9,-96)
