class Indexer:
    def __init__(self,list1):
        self.list1=list1

    def __gettime__(self,index):
        print('gettime',index)
        print(self.list1[index])

x=Indexer([1,5,8,9,6,8,2,1])
x[2:6]
print(x)


class Number:
    def __init__(self,data1,result=0):
        self.data=data1
        self.result=result

    def __add__(self,data2):
        self.result=self.data1+data2
        return self.result

    def __sub__(self,data2):
        self.result=self.data1-data2
        return self.result
    
