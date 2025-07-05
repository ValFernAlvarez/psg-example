'''
4. Jane y Jhon llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a un candy bar.
    Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. A continuación
    tienes los postres que han ido pidiendo en cada salida:

Jane: Lemon Pie, Brownie, Tarta de Manzana, Helado de Chocolate, Flan
Jhon: Carrot Cake, Croissant de Chocolate, Lemon Pie, Tarta de Manzana, Pudding

Si la cantidad de postres que tienen en común es mayor al 50% entonces son compatibles, de lo contrario quieren
replantear su relación.
'''
platos_jane={"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
platos_john={"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}
#---
platos_en_comun=platos_jane & platos_john
#---
verificacion=len(platos_en_comun)>(len(platos_jane | platos_john)/2)
#---
print(f"Platos en comun: {platos_en_comun}\n¿Son compatibles?: {verificacion}")