
def fibo(num):
    a = 1
    b = 0

    for n in range(num):
        aux = a + b
        b = a
        a = aux

        print(b)
    

num = int(input("Insira quantos numeros da serie deseja: "))

fibo(num)