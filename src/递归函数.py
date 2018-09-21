lista = [ i for i in range(10)]
lista.append(None)

print(
    lista
)

def func1(i):
    if lista[i] is None:
        return 'end'
    return str(lista[i]) + func1(i+1)

print(
    func1(5)
)