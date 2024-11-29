
def calc_fatorial(n):
    if n == 1 or n == 0 :
        return 1
    elif n > 0 :
        resultado = n * calc_fatorial(n-1)
        return resultado
    else:
        print("Número fora do escopo")

n = int(input("Escreva o número: "))
resultado = calc_fatorial(n)
print("O fatorial de", n,"é", resultado)
    
