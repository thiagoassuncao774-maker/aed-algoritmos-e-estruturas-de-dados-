n = int(input("digite um numero:"))
i= 0
resultado=0
for i in range (1, n +1):
    if i%2 ==0:
        resultado = resultado + 1
    print(resultado)