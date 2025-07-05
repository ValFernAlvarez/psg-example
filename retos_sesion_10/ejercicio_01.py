'''
1. Elimina los elementos de oficina repetidos de la cadena.
'''
cadena_original="📎📐📏✏️🖊️🖋️📎📌📏📇🗂️📁📌🗃️✏️📂🖇️"
conjunto_de_cadena=set(cadena_original)
print(f"Cadena original: {cadena_original}\nCadena nueva sin elementos repetidos: {"".join(conjunto_de_cadena)}")