class testClass:
    def __init__(self, a):
        self.a = a

    def funcA(self):
        print(self.a)

    def funcB(self):
        self.a = 123

t1 = testClass(111)
t1.funcB()
t1.funcA()