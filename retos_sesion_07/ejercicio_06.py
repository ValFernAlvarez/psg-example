'''
6. Agregar 5 Ejemplos con otras funciones no vistas en la sesión.
'''
print('''1. str.casefold()
Convierte todas las letras a minúsculas, incluyendo los caracteres acentuados, lo que lo hace ideal para comparaciones
o para procesar texto cuando no te importa distinguir entre mayúsculas y minúsculas.''')
palabra="CAMIÓN"
print(f"{palabra}:{palabra.casefold()}")
print('''
2. str.center(width[, fillchar])
Centra una cadena (str) en un campo de ancho especificado (width). Puedes rellenar los espacios a los lados con el carácter
que elijas (fillchar), que por defecto es un espacio.''')
palabra="HOLA"
print(f"{palabra}")
print(f"{palabra.center(15, "-")}")
print('''
3. str.endswith(suffix[, start[, end]])
Devuelve True si la cadena termina con el sufijo indicado (suffix).
Opcionalmente, puedes indicar el índice de inicio (start) y fin (end) para comprobar solo una parte de la cadena.''')
frase="Hola mundo"
print(f"{frase}:{frase.endswith("la", 0, 5)}")
frase_2="Sala 2"
print(f"{frase_2}:{frase_2.endswith("la", 0, 5)}")
frase_3="Alas"
print(f"{frase_3}:{frase_3.endswith("la", 0, 5)}")
print('''
4. str.isdecimal()
Devuelve True si todos los caracteres de la cadena son dígitos decimales (0 al 9).
Si la cadena tiene letras, espacios, signos, fracciones, o cualquier otro carácter, devuelve False.''')
cadena_1="1234"
print(f"{cadena_1}:{cadena_1.isdecimal()}")
cadena_2="123,4"
print(f"{cadena_2}:{cadena_2.isdecimal()}")
print('''
5. str.ljust(width[, fillchar])
Ajusta una cadena a la izquierda en un campo de ancho especificado (width), rellenando con el carácter
que elijas (fillchar), que por defecto es un espacio.''')
palabra="hola"
print(palabra)
print(palabra.ljust(10, "-"))




