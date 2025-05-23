'''
3. Escribe un programa en Python que convierta 1000000 de
    segundos en semanas, días, horas, minutos y segundos
'''
segundos=1000000
semanas=segundos//((3600*24)*7)
dias=segundos%((3600*24)*7)//((3600*24))
horas=segundos%((3600*24)*7)%((3600*24))//3600
minutos=(segundos%((3600*24)*7)%((3600*24))%3600)//60
segundos=(segundos%((3600*24)*7)%((3600*24))%3600)%60
#---
print(f"Semana(s): {semanas}  Día(s): {dias}  Hora(s): {horas}  Minuto(s): {minutos}  Segundo(s): {segundos}.")