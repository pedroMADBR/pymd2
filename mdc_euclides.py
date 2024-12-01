
def mdc(num1, num2):
    if (num1 > num2):
        resto = 1
        while resto != 0 :
            resto = num1 % num2
            num1 = num2
            num2 = resto
            if resto == 0:
                mdc = num1
        if resto == 0:
                mdc = num2
    else:
        resto = 1
        while resto != 0 :
            resto = num2 % num1
            num2 = num1
            num1 = resto
            if resto == 0:
                mdc = num2
        if resto == 0:
                mdc = num1
    print(mdc)

num1 = int(input("insira numero 1: "))
num2 = int(input("insira numero 2: "))

mdc(num1,num2)

