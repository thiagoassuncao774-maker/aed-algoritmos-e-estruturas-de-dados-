win=int(input("quantas vitorias seu time tem?"))
lose=int(input("quantas derrotas seu time tem?"))
tgm=(win+lose)
print("vitorias:",win)
print("derrotas:",lose)
print("total de partidas:",tgm)
porcerntvit=(win*100)/tgm
print(porcerntvit)
