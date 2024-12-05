def soma_recursiva(n):
    # Caso base: se n for 1, retorna 1
    if n == 1:
        return 1
    # Passo recursivo: soma n ao resultado da chamada recursiva com n-1
    return n + soma_recursiva(n - 1)

# Teste do método
n = 3  # Exemplo de entrada
print(f"A soma de 1 até {n} é {soma_recursiva(n)}")
