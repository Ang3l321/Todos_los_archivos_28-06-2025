""" 
En este archivo vamos a hacer
ejercicios. Ejercicio 2
"""
#Ingreso de productos 
import os
def crear_producto():
    producto = input('Ingrese el producto: ')
    if producto in inventario:
        precio = input('Ingrese el precio de ese producto: ')
        A = input(f'El producto {producto} se actualizara. "S" para continuar')
        if A == 'S':
            inventario.update({producto: precio})
        else:
            print('Entendido la actualización no se realizara')
        os.system('pause')
    else:
        precio = input('Ingrese el precio de ese producto: ')   
        inventario[producto] = precio
    return inventario


def leer_producto(diccionario):
    prod = input('Ingrese producto que quiere conocer: ')
    if prod in diccionario:
        print(f'El precio es: {diccionario[prod]}')
    else:
        print('El procunto no se encuentra en el inventario.')
    os.system('pause')
    
def borrar_produto():
    producto = input('Cual es el producto que desea borrar?')
    inventario.pop(producto)
    
inventario = {}
while True:
    os.system('cls')
    seleccion = input('\tMENU DE OPCIONES:\n''1) Para crear o actualizar producto\n''2) Para saber precio de producto\n''3) Para borrar producto \n''4)Salir ')
    if seleccion == '1':
        inventario = crear_producto()
        print(inventario)
    elif seleccion == '2':
        leer_producto(inventario)
    elif seleccion == '3':
        borrar_produto()
    else:
        print('Salimos.(～￣▽￣)～\n ')
        break
        
print(inventario)