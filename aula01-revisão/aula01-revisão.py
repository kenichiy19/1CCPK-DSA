def busca_binaria(lista, procurado):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == procurado:
            return meio

        elif lista[meio] < procurado:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1

numeros = [3, 7, 10, 15, 21, 28, 32, 40, 47, 51, 63]

posicao = busca_binaria(numeros, 40)

print(posicao)