
# Mi Version 1.0 Ordenamiento Burbuja
print("\n Bienvenido al Ordenador de Numeros \n\n")
lista = []
cn = int(input("Cantidad de numeros enteros a ingresar: "))
 
for i in range(0,cn):
    lista.append(int(input("Ingrese numero %d : " % i )))

numero = len(lista)
i = 0
while (i < numero):
    j = i
    while (j < numero):
        if(lista[i] > lista[j]):
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
        j = j + 1
    i = i + 1
 
for elemento in lista:
    print elemento, ', ' ,
