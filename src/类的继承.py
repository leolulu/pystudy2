class baseClass:
    def set1(self,num):
        self.num = num

class childClass(baseClass):
    def set1(self,num,name):
        self.num = num
        self.name = name

t = childClass()
t.set1(14,'ago')
print(
    t.num,
    t.name
)

# print(
#     issubclass(childClass,baseClass)
# )

# print(
#     isinstance(childClass,baseClass)
# )