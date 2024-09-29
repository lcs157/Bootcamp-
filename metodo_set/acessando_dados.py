numeros = {1,2,3,4,5,6,7,8,8}
numeros_list = list(numeros)
print(numeros_list[-2])

carros = {"Hyunday", "Elantra", "Hyunday", "Elantra"}

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):#saber qual indice quero acessar usando metodo enumerate com for 
    print(f"{indice}, {carro}")