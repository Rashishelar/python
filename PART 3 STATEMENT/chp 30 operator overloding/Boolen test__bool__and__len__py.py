class Test:
    def __bool__(self):
        return True
x=Test()
print(bool(x))
