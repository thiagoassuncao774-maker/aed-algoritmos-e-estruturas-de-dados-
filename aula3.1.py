nota1=(int(input("digite sua primeira nota:")))
nota3=(int(input("digite sua segunda nota:")))
nota2=(int(input("digite sua terceira nota:")))
soma=nota1+nota2+nota3
media=soma/3
if media >=70:
    print("parabens voce esta aprovado!")
elif media <=40:
    print("fica pra proxima amigão")
else:
    print("você deve fazer exame!")