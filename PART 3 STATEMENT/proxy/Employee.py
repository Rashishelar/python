class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary

    def __repr__(self):
        return'[Employee:%s,%s,%s]'%(self.name,self.position,self.salary)

class Employee_proxy:
    def __init__(self,target):
        self.target=target

    def __getattr__(self,attr):
        return getattr(self.target,attr)

    def getName(self):
        print(self.name)

    def getposition(self):
        print(self.position)

    def getsallary(self):
        if self.position=='Mgr':
            print(self.salary)
        else:
            raise permissionError("Access to salary information is restricted")

rashi=Employee('Rashi shelar','dev',25000)
print(rashi)
rashi_proxy=Employee_proxy(rashi)
rashi_proxy.getName()
rashi_proxy.getposition()
#rashi_proxy.getsalary()
print()
dipti=Employee('dipti shah ','Mgr',50000)
print(dipti)
dipti_proxy=Employee_proxy(dipti)
dipti_proxy.getName()
dipti_proxy.getposition()
print()
