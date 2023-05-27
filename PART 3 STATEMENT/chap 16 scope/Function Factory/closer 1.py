#function factory

def f1(num1):
    def f2 (num2):
        return num1*num2
    return f2

a1=f1(21)
print(a1(4))


def f1(pics1):
    def f2(pics2):
        return pics1*pics2
    return f2

R1=f1(24)
print(R1(11))

