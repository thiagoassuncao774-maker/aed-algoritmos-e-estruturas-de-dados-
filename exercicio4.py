lista = [1, 2, 2, 3, 3, 3, 4]
i = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while i != len(lista):
    if lista [i]== 1:
        cont1+1

    if lista [i]== 2:
        cont2+=1

    if lista [i]== 3:
        cont3+=1

    if lista [i]== 4:
        cont4+=1
    i+= 1
dict = {1: cont1, 2:cont2, 3:cont3, 4:cont4}
print(dict)