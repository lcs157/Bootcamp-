frutas = ["Morango", "Banana", "Morango"] 
print(set(frutas))
numeros = [1,2,3,4,5,6,6,8,9,9]
print(type(numeros))

for numero in frutas:#QUANDO PASSAMOS UMA LISTA DE INTEIROS PARA O FOR ELE TRANSFORMA A LISTA EM INT 
    #ENTAO O SETT NAO FUNCIONA COM O METDDO FOR
    print(set(numero))
    print(type(numero))
fruta = ("abacaxi")
print(set(fruta))#quando se usa sett com str por mais que as palavras escritas 
#tenham letras diferentes elas nao sao demonstradas apos o uso do sett

linguagens = {"python","java","c#sharp","python"}#ultilizar chaves faz com que a variavel vire um set
print(type(linguagens))