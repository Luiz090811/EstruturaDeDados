# Definição e Importância das Estruturas de Dados

Estruturas de dados podem ser **lineares** (como listas, filas e pilhas) ou **não lineares** (como árvores e grafos). A escolha da estrutura correta impacta diretamente o desempenho de um programa.

## Exemplo de Código sem Tratamento de Estrutura de Dados
```python
# Exemplo ineficiente de busca em uma lista não ordenada
def busca_ineficiente(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False

# Exemplo eficiente de busca em uma lista ordenada
def busca_eficiente(lista, valor):
    return valor in lista