from collections import deque
fila = deque()
fila.append(1)  # Inserção
fila.append(2)
fila.popleft()  # Remoção
print(fila)     # deque([2])