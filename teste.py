notas = [7.5, 8.5, 6.5, 9.0]
print(notas)

soma = sum(notas)
print(soma)

divisor = len(notas)
media = (soma/divisor)
print(media)

notas.append(5.0)
print(notas)

notas.pop(2)
print(notas)

ordenador = sorted(notas)
print(ordenador)
print(list(reversed(ordenador)))

tuple1 = (1, 2, 3, 4)
print(tuple1)
list(tuple1)
print(tuple1)

t1 = (1, 2)
t2 = (3, 4)
tuple2 = (t1+t2)
print(tuple2)

oneset = (1, 3, 3, 6, 5)
print(set(oneset))

sett = (1, 3, 3, 6, 5)
sett.add(2)
sett.remove(6)
print(sett)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)

tuple3 = (22, 25, 27, 21)