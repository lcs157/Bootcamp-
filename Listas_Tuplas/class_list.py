#ADICIONANDO ELEMENTOS A LISTA COM METODO APPEND

lista = []

lista.append(1)
lista.append("Python")
lista.append([1,2,3,4,5])

print(lista)

#LISTAS SAO MUTAVEIS CRIANDO UMA NOVA LISTA COM METODO COPY

nova_lista = lista.copy()
print(nova_lista,"Lista do copy")
print(id(lista), id(nova_lista))

nova_lista[0] = 2
print(nova_lista)


#METODO COUNT SERVE PARA MOSTRAR QUANTAS VEZES UM OBJETO APARECE NA LISTA
cores = ["Vermelho", "Azul", "Verde", "Azul"]

print(cores.count("Vermelho"))
print(cores.count("Azul"))
print(cores.count("Verde"))

#METODO EXTEND SERVE PARA JUNTAR AS LISTAS 

lingaugens = ["Python", "C#", "Java"]
print(lingaugens)

lingaugens.extend(["Kotlin", "Ruby"])

print(lingaugens)

#METODO INDEX ENCONTRA EM QUAL POSIÇAO DA LISTA O ELEMENTO ESTA
#CASO TENHA ELEMENTOS REPETIDOS O INDEX FOCA APENAS NO PRIMEIRO QUE APARECE NA LISTA

print(lingaugens.index("Kotlin"))
print(lingaugens.index("Python"))

#METODO POP EXCLUI O ULTIMO ITEN ADICIONADO A LISTA 
#SEMPRE BOM ULTILIZAR JUNTO A O METODO INDEX POIS ASSIM 
#FACILITA A NAO EXLCUIR UM ITEN ERRADO DA LISTA

# print(lingaugens.pop())
# print(lingaugens.pop())
# print(lingaugens.pop())
# print(lingaugens.pop(0))

# print(lingaugens)

#METODO REMOVE VOCE CONSEGUE REMOVER ITENS DA LISTA 
#A PARTIR DOS NOMES DELES
lingaugens.remove("Kotlin")
print(lingaugens)


#REVERSE SERVE PARA INVERTER A LISTA DE TRAS PARA FRENTE
#AONDE O PRIMEIRO ELEMENTO PASSA A SER O ULTIMO E O ULTIMO O PRIMEIRO

lingaugens.reverse()
print(lingaugens)


#METODO SORT SERVE PARA ORGANIZAR AS LISTAS SEJA EM ORDEN
#ALFABETICA OU NUMERICA ou ULTILIZANDO BOOL PARA REVERTER 


lingaugens.sort()
print(lingaugens)

lingaugens.sort(reverse=True)
print(lingaugens)


lingaugens.sort(key=lambda x: len(x)) #COMBINANDO CONSIGO COLOCAR A LISTA EM ORDEN CRESCENTE
print(lingaugens)


lingaugens.sort(key=lambda x: len(x), reverse=True) #ADICIONANDO O REVERSE JUNTO A O KEY COLOCO EM ORDEN DECRESCENTE
print(lingaugens)



tamanho_lista = len(lingaugens)
print(tamanho_lista)

print(type(lingaugens))