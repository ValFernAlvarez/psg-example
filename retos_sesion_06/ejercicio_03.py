'''
3. Imprime una tabla de verdad para la siguiente sentencia:
    "Un sistema de seguridad controla el acceso a una habitación, la puerta sólo se abre si se introduce
    una tarjeta válida o la huella dactilar, pero no ambas al mismo tiempo. Si se introduce la tarjeta y
    la huella dactilar, la puerta no se abre. ¿Qué operador lógico se puede utilizar?"
'''
tarjeta=True
huella=True
print ("Operador XOR")
print("Para ambos (V) (V): ",(tarjeta or huella) and not (tarjeta and huella))
tarjeta=True
huella=False
print("Para tarjeta (V) (F): ",(tarjeta or huella) and not (tarjeta and huella))
tarjeta=False
huella=True
print("Para huella (F) (V): ",(tarjeta or huella) and not (tarjeta and huella))
tarjeta=True
huella=True
print("Para ninguno (F) (F): ",(tarjeta or huella) and not (tarjeta and huella))
