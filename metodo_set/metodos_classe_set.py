#Juntando os conjuntos type set  com metodo union
conjunto_a = {1,2}
conjunto_b = {3,4}
unindo = conjunto_a.union(conjunto_b)
print(unindo)

#Metodo intersection
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
unindo_intersection = conjunto_a.intersection(conjunto_b)
print(unindo_intersection)#mostra apenas os numeros ou elementos que se repetem

#Metodo diference
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
a_diferente_b = conjunto_a.difference(conjunto_b)
b_diferente_a = conjunto_b.difference(conjunto_a)
print(a_diferente_b)
print(b_diferente_a)#MOSTRA OS ELEMENTOS QUE SOA DIFERENTE SEM MOSTRAR OS IGUAIS


#METODO SYMETRIC.DIFFERENCE
conjunto_a = {1,2,3,5}
conjunto_b = {2,3,4,6}

diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_simetrica)

#metodo issubset
conjunto_a = {1,2,3,4,5,6,7,8,9}
conjunto_b = {2,3,4}

pertence_a_b = conjunto_a.issubset(conjunto_b)#TODOS ELEMENTOS DE A ESTAO EM B??
pertence_b_a = conjunto_b.issubset(conjunto_a)#TODOS ELEMSNTOS DE B ESTAO EM A?

print(pertence_a_b)#False pois nem todos de A tem em B
print(pertence_b_a)#True pois todos elementos de b tem em A


#METODO ISSUPERSET
conjunto_a = {1,2,3,4,5,6,7,8,9}
conjunto_b = {2,3,4}

verificando_a = conjunto_a.issubset(conjunto_b)#TODOS CONJUNTOS DE A NAO ESTAO EM B ??
verificando_b = conjunto_b.issubset(conjunto_a)#TODOS OS CONJUNTOS DE B NAO ESTAO EM A?
print(verificando_a)
print(verificando_b)


#METODO ISDISJOINT
conjunto_a = {1,2,3,4,5,6,7,8,9}
conjunto_b = {20,21,22}
conjunto_c = {10,11,12,13,14}
print(conjunto_a.isdisjoint(conjunto_b))


#metodo add

sorteio = {1,2}

print(sorteio.add(25))
print(sorteio.add(27))


#DISCARD
numeros2 ={ 1,2,3,4,5,56,6,9,7,78}

print(numeros2)
numeros2.discard(56)
print(numeros2)

#metodo remove
numeros2 ={ 1,2,3,4,5,56,6,9,7,78}

numeros2.remove(78)
print(numeros2)





