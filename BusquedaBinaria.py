lista = int(input("Ingrese el tamaño del vector: "))
vector = []

for i in range(lista):
    num = int(input(f"Ingrese un numero {i + 1}: "))
    vector.append(num)

print("El vector es:", vector)

elemento = int(input("Ingrese el elemento que desea buscar: "))

inicio = 0
fin = len(vector) - 1
encontrado = False

for i in range(len(vector)):
    medio = (inicio + fin) // 2

    if vector[medio] == elemento:
        encontrado = True
        break
    elif vector[medio] > elemento:
        fin = medio - 1
    else:
        inicio = medio + 1

if encontrado:
    print(f"El elemento {elemento} está en la posición {medio}.")
else:
    print("El elemento no se encuentra en el vector.")
