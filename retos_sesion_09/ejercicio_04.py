'''
4. 
Parte 1: 
Una dulcería tiene 2 listas una con los productos y otra con los precios:
    Agregar 2 productos nuevos al final de las listas
    Eliminar el producto con el nombre "Bon Bon Bum" de las listas
    ¿Cuánto cuesta el producto "Oreo" y "Chizitos"?
    ¿Cuál es el producto más caro y el más barato?

Parte 2:
Una dulcería tiene 2 listas una con los productos y otra con los precios.
    ¿Cuántos productos tienes en total?
    ¿Cuanto cuestan todos los productos?
    Ordena los productos y precios del más barato al más caro.
    Eliminar todos los productos de las listas.
'''
print("\nPARTE 1: ")
productos=["Oreo", "Chizitos", "Delimon", "Skittles","Bon Bon Bum", ]
precios=[3.50, 3.00, 1.00, 11.50, 4.00]
#---
productos.append("Grosso")
productos.append("Ritz")
precios.append(0.50)
precios.append(4.00)
print("4.1.: ")
print(f"Productos: {productos}\nPrecios: {precios}")
#---
precios.pop(productos.index("Bon Bon Bum"))
productos.pop(productos.index("Bon Bon Bum"))
print("\n4.2.: ")
print(f"Productos: {productos}\nPrecios: {precios}")
#---
precio_oreo=precios[productos.index("Oreo")]
precio_chizitos=precios[productos.index("Chizitos")]
print("\n4.3.: ")
print(f"Precio de Oreo: {precio_oreo}\nPrecio de Chizitos: {precio_chizitos}")
#---
producto_mas_caro=productos[precios.index(max(precios))]
producto_mas_barato=productos[precios.index(min(precios))]
print("\n4.4.: ")
print(f"Producto más caro: {producto_mas_caro}\nProducto más barato: {producto_mas_barato}")
#---
#---
print("\n\nPARTE 2: ")
print(f"Productos: {productos}\nPrecios: {precios}")
#---
total_productos=len(productos)
print("\n4.5.: ")
print(f"Total de productos: {total_productos}")
#---
suma_total_productos=sum(precios)
print("\n4.6.: ")
print(f"Total de precios: {suma_total_productos}")
#---
precios_ordenados=sorted(precios)
productos_ordenados=[]
productos_ordenados.append(productos[precios.index(precios_ordenados[0])])
productos_ordenados.append(productos[precios.index(precios_ordenados[1])])
productos_ordenados.append(productos[precios.index(precios_ordenados[2])])
productos_ordenados.append(productos[precios.index(precios_ordenados[3])])
productos_ordenados.append(productos[precios.index(precios_ordenados[4])])
productos_ordenados.append(productos[precios.index(precios_ordenados[5])])
print("\n4.7.: ")
print(f"Productos ordenados: {productos_ordenados}\nPrecios ordenados: {precios_ordenados}")
#---
productos.clear()
precios.clear()
print("\n4.8.: ")
print(f"Productos: {productos}\nPrecios: {precios}")