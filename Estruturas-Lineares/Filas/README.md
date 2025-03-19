# Filas

Filas seguem o princípio FIFO (First In, First Out). O primeiro elemento a ser inserido é o primeiro a ser removido.

## Exemplo em Python
```python
from collections import deque
fila = deque()
fila.append(1)  # Inserção
fila.append(2)
fila.popleft()  # Remoção
print(fila)     # deque([2])