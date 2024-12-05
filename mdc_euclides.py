def mdc(a, b):
    while b != 0:
        a, b = b, a % b  # Atualiza 'a' e 'b' usando o resto da divisão
    return a

# Teste do algoritmo
num1 = 56  # Exemplo de entrada
num2 = 98
print(f"O MDC de {num1} e {num2} é {mdc(num1, num2)}")
