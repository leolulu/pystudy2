lista = [i for i in range(10)]
lista.append(None)
lista.append(10)


print(
    lista
)


def func1(i):
    print(lista[i])
    if lista[i] is not None:
        func1(i+1)

func1(2)