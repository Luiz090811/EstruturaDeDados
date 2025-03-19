# Exemplo de código sem tratamento de estrutura de dados
def busca_ineficiente(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False

# Exemplo de código com tratamento de estrutura de dados
def busca_eficiente(lista, valor):
    return valor in lista

# Teste
lista = [1, 2, 3, 4, 5]
print(busca_ineficiente(lista, 3))  # True
print(busca_eficiente(lista, 6))    # False