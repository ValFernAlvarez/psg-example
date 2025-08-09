'''
3. Escribe un programa en Python que convierta 1000000 de
    segundos en semanas, días, horas, minutos y segundos
'''

segundos_por_minuto=60
segundos_por_hora=3600
horas_por_dia=24
dias_por_semana=7
segundos_por_dia=segundos_por_hora * horas_por_dia
segundos_por_semana=segundos_por_dia * dias_por_semana
#---
segundos = 1000000
#---
semanas=segundos//(segundos_por_semana)
dias=segundos%(segundos_por_semana)//((segundos_por_dia))
horas=segundos%(segundos_por_semana)%(segundos_por_dia)//segundos_por_hora
minutos=(segundos%(segundos_por_semana)%(segundos_por_dia)%segundos_por_hora)//segundos_por_minuto
segundos_restantes=(segundos%(segundos_por_semana)%(segundos_por_dia)%segundos_por_hora)%segundos_por_minuto
#---
print("Semana(s):", semanas)
print("Día(s):", dias)
print("Hora(s):", horas)
print("Minuto(s):", minutos)
print("Segundo(s):", segundos_restantes)
