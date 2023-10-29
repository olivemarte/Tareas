
palabras=("Como estas", "Hola", "Bienvenido", "Mañana", "Buenos dias")
cantidad=0
for c in palabras:
 cantidad= cantidad + c.count('a')
print("La cantidad que aparece la letra (a) es:", cantidad)