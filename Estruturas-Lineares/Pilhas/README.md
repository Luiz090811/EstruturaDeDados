# Pilhas

Pilhas seguem o princípio LIFO (Last In, First Out). O último elemento a ser inserido é o primeiro a ser removido.

## Exemplo em Python
```python
pilha = []
pilha.append(1)  # Inserção
pilha.append(2)
pilha.pop()      # Remoção
print(pilha)     # [1]