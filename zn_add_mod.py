def tabela_zn_adicao(n):
    # Cria a tabela para adição modular
    tabela = [[(i + j) % n for j in range(n)] for i in range(n)]
    return tabela

def imprimir_tabela_adicao(tabela):
    print(f"\nTabela de Adição Modular em Z_{len(tabela)}:")
    print("   " + "  ".join(map(str, range(len(tabela)))))
    print("  " + "-" * (len(tabela) * 3))
    for i, linha in enumerate(tabela):
        print(f"{i} | " + "  ".join(map(str, linha)))

# Exemplo de uso
n = 5  # Exemplo de módulo
tabela_adicao = tabela_zn_adicao(n)
imprimir_tabela_adicao(tabela_adicao)
