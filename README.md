# EstruturaDeDados

# Aplicação Prática: Uso de Pilhas para Verificação de Parênteses

## Problema
Dada uma string contendo parênteses, verifique se eles estão balanceados.

## Solução
Utilizar uma pilha para armazenar os parênteses de abertura. Quando encontramos um parêntese de fechamento, verificamos se ele corresponde ao último parêntese de abertura na pilha.

## Código
```python
def verifica_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha or pilha[-1] != '(':
                return False
            pilha.pop()
    return not pilha

# Teste
print(verifica_parenteses("((()))"))  # True
print(verifica_parenteses("(()))"))   # False

```
# Referências
https://docs.python.org/pt-br/3/tutorial/datastructures.html;
Livro: "Estruturas de Dados e Algoritmos em Python" (Michael T. Goodrich);
https://www.geeksforgeeks.org/data-structures/;
https://chatgpt.com/;
