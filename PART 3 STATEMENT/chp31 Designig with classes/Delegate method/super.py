class Super:
    def method(self):
        print('in super.method')

    def delegate(self):
        self.action()

x=Super()
x.method()

class Provider(Super):
    def action (self):
        print('in provider action')

y=Provider()
y.delegate()


class sub(Super):
    def method(self):
        print('starting sub.method')
        Super.method(self)
        #y=Super()
        #y.method()
        print('ending sub.method')
