'''
2. Tienes una app para gestionar tareas de 4 usuarios, para acceder los 
    usuarios deben iniciar sesión con un nombre de usuario y una contraseña
    introducidos por teclado.

a)Define los siguientes usuarios y contraseñas utilizando la estructura de
datos mas adecuada.

b)Verifica si el usuario inició sesión para acceder a la app y muestra el
mensaje Acceso Aprobado, caso contrario muestra el mensaje de error
Acceso Denegado.
'''
#---Para (a)---
usuarios={
    "admin": "admin123",
 "user1": "user123",
 "user2": "user123",
 "user3": "user123"}
#---
user_input=input("Ingrese usuario: ")
user_contrasena=input("Ingrese contraseña: ")
#---Para (b)---
if user_input in usuarios and usuarios[user_input]==user_contrasena:
    print("Acceso Aprobado.")
else:
    print("Acceso Denegado.")