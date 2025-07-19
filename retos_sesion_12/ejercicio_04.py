'''
4. Una tienda ofrece descuentos a sus clientes, si el cliente tiene una
    edad mayor a 60 años y tiene una compra mayor a 1000, se le aplica un
    descuento del 20%, si el cliente tiene una edad entre 18 y 60 años y
    tiene una compra mayor a 500 se le aplica un descuento del 10%, si no
    cumple ninguna condición se le aplica un descuento del 2%
'''
edad=int(input("Ingrese edad: "))
compra=float(input("Ingrese el total de compra:"))
#---
if edad>60 and compra>1000:
    descuento=compra*0.2
elif 18<=edad<=60 and compra>500:
    descuento=compra*0.10
else:
    descuento=compra*0.02
#---
total_con_descuento=compra-descuento
#---
print(f"Total con descuento: {total_con_descuento} $.")