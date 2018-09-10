class myClass2:
    '这是一个学猪叫的类'
    def __init__(self):
        pass
    
    def jiao(self):
        print('猪叫')

print(myClass2.__dict__)
print(myClass2.__name__)
print(myClass2.__doc__)