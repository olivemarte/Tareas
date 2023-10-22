"""d1= {
    "Nombre": "Sara",
    "Edad": 27,
    "Documento": 1003882 
}
d1['Nombre']="Laura"

print(len(d1))
Documento=d1.get('Edad')
print(Documento)
print(d1.items())
clave=d1.keys()
print(clave)
valores=d1.values() 
print(valores)
valor=d1.pop('Edad')
print(valor)
print(d1)
eliminado=d1.popitem()
print(eliminado)
print(d1) 

d2= {
    'Nombre':'Sara',
    'Edad':21,
    'Asignatura': 'Ingieneria en sistema computacionales',
    'Matricula':1187896
}
d1.update(d2)
print(d1) 

frutas={'Naranja', 'Banana', 'Pera'} 
frutas.add('Manzanas')
print(frutas)
frutas.remove('Pera')
print(frutas)

frutas.discard('Sandia')
print(frutas)

numero={1,2,3}
print(2 in numero)
print(4 in numero)"""

a={1,2,3}
b={3,4,5}
c={2,3,4}
"""c=a.union(b)"""
d=a.intersection(c)
print(d)


