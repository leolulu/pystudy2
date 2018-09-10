class MyClass:
    '偶的类'
    myNum = 0  # 类变量

    def __init__(self, id, name):
        print('类的实例被创建了')
        self.id = id
        self.name = name
        MyClass.myNum += 1

    def showMynum(self):
        print(self.myNum)

    def whatIsSelf(self):
        print(self)


t = MyClass(1, 'leo')
t.whatIsSelf()
t.shit = 2
t2 = MyClass(2,'dudu')
print(t2.name)

print(MyClass.myNum)
print(t2.myNum)