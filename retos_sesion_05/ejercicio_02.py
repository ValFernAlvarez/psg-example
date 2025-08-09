'''
2. Escribe un programa en Python que convierta las
    siguientes temperaturas de grados Fahrenheit a
    grados Celsius:
        25 ºF
        300 ºF
        76 ºF
'''
frnht_a=25 #Temperatura A
frnht_b=300 #Temperatura B
frnht_c=76 #Temperatura C
#---
clss_a=(frnht_a-32)/(1.8) #Celsius A
clss_b=(frnht_b-32)/(1.8) #Celsius B
clss_c=(frnht_c-32)/(1.8) #Celsius C
#---
print("Fahrenheit: ", frnht_a, "ºF  --->  Celsius: ", clss_a, "°C")
print("Fahrenheit: ", frnht_b, "ºF  --->  Celsius: ", clss_b, "°C")
print("Fahrenheit: ", frnht_c, "ºF  --->  Celsius: ", clss_c, "°C")