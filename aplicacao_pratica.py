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