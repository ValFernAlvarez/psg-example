'''
5. Tienes una app para gestionar contactos, cada contacto tiene un nombre
    y un número de teléfono, si el contacto tiene un número de teléfono
    válido (11 dígitos incluyendo el código de país) y un nombre valido
    se guarda en la lista de contactos y muestra el mensaje 'contacto guardado',
    caso contrario se muestra el mensaje de error 'Datos incorrectos'.
-El nombre y el numero de teléfono se ingresan por teclado
-Verifica si el el numero de teléfono es válido
-Verifica si el nombre válido usando truthiness
'''
nombre=input("Ingrese nombre: ")
num_telefono=input("Ingrese el numero de teléfono: +")
#---
if nombre and (num_telefono).isdigit() and len(num_telefono)==11:
    print("-------------\nContacto Guardado.")
else:
    print("-------------\nDatos Incorrectos.")