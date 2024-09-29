#BOA PRATICA E SEMPRE COLOCAR UMA VIRGULA NO FINAL DE QUAISQUER
#DECLARACAO DE TUPLA


frutas = ("Laranja", "Maçã", "Morango",)
print(frutas[0])
print(frutas[-1])

letras = tuple("Python")

numeros =tuple([1,2,3,4,5,6])

pais = ("Canada",)

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (5, 6, "c"),
)

print(matriz[0])#acessando indice 0 completo -->[1, "a", 2]
print(matriz[0][0])#acessando linha 0 e o indice 0 da lista --> 1
print(matriz[0][-1])#acessando lista 0 e o ultimo elemento da lista --> 2
print(matriz[-1][-1])#acessando ultima lista e ultimo elemento da lista --> c


#FATIAMENTO DE TUPLAS
tupla = ("P","y","h","o","n",)

print(tupla[2:])# acessando do do indice 2 para frente --> ['t', 'h', 'o', 'n']
print(tupla[:2])# acessando so os dois primeiros indices --> ['P', 'y']
print(tupla[1:3])# ['P', 'y']
print(tupla[0:3:2])# acessando do indice 0 ate o 3 pulando um indice pois o 2 representa o stap ou o passo 
print(tupla[::])#acessando lista argumento por argumento --> ['P', 'y', 't', 'h', 'o', 'n']
print(tupla[::-1])# acessando os itens da lista de traz para frente --> ['n', 'o', 'h', 't', 'y', 'P']

#PERCORRENDO A TUPLA COM FOR 
carros = ("Hyunday", "BMW", "Mercedes",)

for carro in carros:
    print(carro)


#METODO COUNT

carros = ("Hyunday", "BMW", "Mercedes",)

print(carros.count("Hynday"))

#METODO INDEX

carros = ("Hyunday", "BMW", "Mercedes",)
print(carros.index("BMW"))

#METODO LEN
print(len(carros))



carros = ("gol") 
print(isinstance(carros, tuple))