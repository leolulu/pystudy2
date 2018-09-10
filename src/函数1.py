def irepeat(str):
        print(str)
        return

def fixedrepeat():
    print('不变')

def doublerepeat(func,strr):
    func(strr)

doublerepeat(irepeat,'shit')
