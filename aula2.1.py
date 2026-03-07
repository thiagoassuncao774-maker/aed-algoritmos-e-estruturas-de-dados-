numero1=float(input("digite um numero para a operação aritmetica:"))
numero2=float(input("digite um numero para a operação aritmetica:"))
sinal=str(input("digite o sinal desejado:"))
print("para adicionar digite + \n para subtrair digite - \n para multiplicar digite * \n para dividir digite / \n")
if sinal==("+"):
    adição=numero1+numero2
    print("adição:",adição)
if sinal==("-"):
    subtração=numero1-numero2
    print("subtração:",subtração)
if sinal==("*"):
    multiplicação=numero1*numero2
    print("multiplicação:",multiplicação)
if sinal==("/"):
    divisão=numero1/numero2
    print
if numero2!=0:
    print("0")
    print("divisão:",divisão)
resto=numero1%numero2
print("resto:",resto)
exponenciacao=numero1**numero2
print("exponenciação:",exponenciacao)
divisaointeira=numero1//numero2
print("divisão inteira:",divisaointeira)