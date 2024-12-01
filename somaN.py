

def somaN(num):
    aux = 0
    for n in range(num+1):
        soma = n + aux
        aux = soma
    print(soma)

nums = int(input("insira ultimo n: "))
somaN(nums)