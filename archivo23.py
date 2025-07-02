""" 
En este archivo vamos a hacer 
ejercicios 
"""

#Contador de palabras  
entrada = input('Ingrese la grase: ').lower()
palabras = entrada.split(' ')
conjunto = list(set(palabras))
print()
"""    
print(conjunto[0])
print(palabras.count(conjunto[0]))
print(conjunto[1])
print(palabras.count(conjunto[1]))
print(conjunto[2])
print(palabras.count(conjunto[2]))"""

for i in range(len(conjunto)):
    print(conjunto[i])
    print(palabras.count(conjunto[i]))
print()
salida = {}
for i in range(len(conjunto)):
    salida[conjunto[i]] = palabras.count(conjunto[i])
    
print(salida)

#Y debe arrojar esta salida 
#salida = {'Manzana': 2, 'Banana': 1, 'Melon':1 }
