#DIVERSAS FORMAS DE SE FAZER UMA LISTA 

frutas = ["Maçã", "Banana", "Morango"]#Lista vc acessa os indices a partir do 0.
print(frutas[0])#Maçã
print(frutas[-3])#Indice negativo nao se inicia a partir do 0


frutas = []


letras = list("Python")


numeros = list(range(10))


carro = ["Ferrari", "458 Italia", 2024, 2000, "DLA1212", True]



#Acessando Os elemenstos das listas por linha ou por coluna
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [5, 6, "c"],
]

print(matriz[0])#acessando indice 0 completo -->[1, "a", 2]
print(matriz[0][0])#acessando linha 0 e o indice 0 da lista --> 1
print(matriz[0][-1])#acessando lista 0 e o ultimo elemento da lista --> 2
print(matriz[-1][-1])#acessando ultima lista e ultimo elemento da lista --> c





#FATIAMANETO DE LISTAS
lista = list("Python")

print(lista[2:])# acessando do do indice 2 para frente --> ['t', 'h', 'o', 'n']
print(lista[:2])# acessando so os dois primeiros indices --> ['P', 'y']
print(lista[1:3])# ['P', 'y']
print(lista[0:3:2])# acessando do indice 0 ate o 3 pulando um indice pois o 2 representa o stap ou o passo 
print(lista[::])#acessando lista argumento por argumento --> ['P', 'y', 't', 'h', 'o', 'n']
print(lista[::-1])# acessando os itens da lista de traz para frente --> ['n', 'o', 'h', 't', 'y', 'P']


#ITERAÇAO DE LISTAS


carros = ["Ferrari", "Porsche", "Maserati"]

for carro in carros:
    print(carro) #ITERANDO SOBRE UMA LISTA ULTILIZANDO FOR E METDO DE ACESSO A ELEMENTOS E FATIAMENTO
    print(carro[1])




#FUNCAO ENUMERATE

carros = ["Ferrari", "Porsche", "Maserati"]

for i, carro in enumerate(carros):#AQUI ESTOU ENUMERANDO OS ELEMENTOS DA LISTA FICA MAIS FACIL CASO EU PRECISE PERCORRELA
    print(f"{i}:{carro}")


#COMPRENSAO DE LISTAS

# numeros = [1, 2, 3, 4, 5, 6]

# pares =[]

# for numero in numeros:
#     if numero % 2 ==0:
#         pares.append(numero)
#         print(pares)


# numeros = [1, 2, 3, 4, 5, 6]
# pares = [numero for numero in numeros if numero%2 ==0 ]
# print(pares)

numeros = [1, 2, 3, 4, 5, 6]
quadrado = []

for numero in numeros:
    quadrado.append(numero **2)

    print(quadrado)