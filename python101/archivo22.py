
""" 
Vamos a mirar algunas funciones con
diccionarios 

"""
proveedores = {'Nombre': ['Mercedes', 'Audi', 'Porsche', 'Rolls Royse', 'BMW', 'Mustang'],
               'Precios': [600, 100, 500, 300, 400, 200],
               'Modelo': ['2004','2005', '2014', '1997', '2008', '2009']}

print()
print(proveedores)
print()
print(proveedores.get('Nombre'))
print(proveedores.get('Modelo'))
print()
print(proveedores.items())
print(proveedores['Nombre'])
proveedores['Nombre'] = ['Mercedes', 'Ferrari', 'Porsche', 'Rolls Royse', 'BMW', 'Mustang']
print()
print(proveedores)
proveedores.update({'Nombre': ['Mercedes', 'Ferrari', 'Porsche', 'Rolls Royse', 'BMW', 'Mustang'],})
print()
proveedores.pop('Precios')
print(proveedores)
print()
proveedores.popitem()
print(proveedores)
print()
proveedores['Propietarios']=['Cesar', 'Yojan', 'Juan', 'yo', 'Nosotros', 'Ustedes', 'Ellos']
print()
print(proveedores)
proveedores = {'Nombre': ['Mercedes', 'Audi', 'Porsche', 'Rolls Royse', 'BMW', 'Mustang'],
               'Precios': [600, 100, 500, 300, 400, 200],
               'Modelo': ['2004','2005', '2014', '1997', '2008', '2009']}
prov2 = proveedores.copy()
prov2['Color'] = ['AZ','NG','RS','PL']
print()
print(prov2)
print()
print(proveedores)
