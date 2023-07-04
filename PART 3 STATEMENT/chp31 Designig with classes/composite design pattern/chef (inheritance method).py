class Employee:
    def __init__(self,name,etype=None,salary=0.0):
        self.name=name
        self.etype=etype
        self.salary=salary

    def giveRaise(self,percent):
        self.salary=self.salary+(self.salary*percent)

    def work(self):
        print(self.name,'does stuff')

    def __repr__(self):
        return 'employee-> name %s,etype %s,salary = %s' %(self.name,self.etype,self.salary)

class Chef(Employee):
    def __init__(self,name):
        chef_list=['Italianchef','Maharashtrianchef','bengolichef']
        if self.__class__.__name__==chef_list[0]:
            Employee.__init__(self,name,self.__class__.__name__,25000)
        elif self.__class__.__name__==chef_list[1]:
            Employee.__init__(self,name,self.__class__.__name__,30000)
        elif self.__class__.__name__==chef_list[2]:
            Employee.__init__(self,name,self.__class__.__name__,40000)
        else:
            pass

    def work(self):
        print(self.name,'makes food')

class Italianchef(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,'makes Italian')

class Maharashtrianchef(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,'makes Maharashtrian')
        
class bengolichef(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,'makes bengoli')

class server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,self.__class__.__name__,10000)

    def work(self):
        print(self.name,'interface with customer')

if __name__=='__main__':

    chef_employee_list=[]

    raju=Italianchef('Raju Mane')
    chef_employee_list.append(raju)

    omkar=Maharashtrianchef('omkar savardekar')
    chef_employee_list.append(omkar)

    rashi=bengolichef('rashi shelar')
    chef_employee_list.append(rashi)

    for obj in chef_employee_list:
        print(obj)
        obj.work()
        print()

    print()
    print()
    server_employee_list=[]

    makrand=server('Makrand salvi')
    server_employee_list.append(makrand)

    dipti=server('dipti shah')
    server_employee_list.append(dipti)

    for obj in server_employee_list:
        print(obj)
        obj.work()
        print()


        
    






