
""" 
En estre archivo vamos a trabajar 
con los diccionarios dict()
"""
cliente = {'Nombres':['juan', 'pedro', 'Alberto'],
           'Tel':[123, 456, 789, 987]} 

print(cliente)
print()
print('list(cliente.keys())')
print(list(cliente.keys()))
print('claves = list(cliente.keys())')
claves = list(cliente.keys())
print(claves[0])
print
print('list(cliente.values())')
print(list(cliente.values()))
print()
valores = list (cliente.values())
print(valores[0])
print(valores[0][1])
print()
print(f'{valores[0][0]}\t{valores[1][0]}')
print(f'{valores[0][1]}\t{valores[1][1]}')
print(f'{valores[0][2]}\t{valores[1][2]}')
print()
c = 0
f = 0
print(f'{valores[c][f]}\t {valores[c+1][f]}')
c = 0
f = 1
print(f'{valores[c][f]}\t {valores[c+1][f]}')
c = 0
f = 2
print(f'{valores[c][f]}\t {valores[c+1][f]}')
c = 0
#f = 0,1,2,3
for f in range(0,3):
    print(f'{valores[c][f]}\t {valores[c+1][f]}')
print()
print('Ejemplo')
proveedores = {'Nombre': ['Mercedes', 'Audi', 'Porsche', 'Rolls Royse', 'BMW', 'Mustang'],
               'Precios': [600, 100, 500, 300, 400, 200],
               'Modelo': ['2004','2005', '2014', '1997', '2008', '2009']}
print(proveedores)
claves = list(proveedores.keys())
valores = list(proveedores.values())
print()
print(f'{claves[0]}\t{claves[1]}\t{claves[2]}')
print()
for f in range(6):
    print(f'{valores[0][f]}\t{valores[1][f]}\t{valores[2][f]}')


