def tabela_zn_multiplicacao(n):
    # Cria a tabela para multiplicação modular
    tabela = [[(i * j) % n for j in range(n)] for i in range(n)]
    return tabela

def imprimir_tabela_multiplicacao(tabela):
    print(f"\nTabela de Multiplicação Modular em Z_{len(tabela)}:")
    print("   " + "  ".join(map(str, range(len(tabela)))))
    print("  " + "-" * (len(tabela) * 3))
    for i, linha in enumerate(tabela):
        print(f"{i} | " + "  ".join(map(str, linha)))

# Exemplo de uso
n = 5  # Exemplo de módulo
tabela_multiplicacao = tabela_zn_multiplicacao(n)
imprimir_tabela_multiplicacao(tabela_multiplicacao)
