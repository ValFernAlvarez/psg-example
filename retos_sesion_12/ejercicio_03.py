'''
3. Jhon colecciona autos a escala 1:64.
    Jess tambien colecciona autos a escala 1:64

a) ¿Que autos tienen en común ambos coleccionistas?
b)¿Cuáles son los autos en común?
'''
jhon={'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
jess={'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}
#---
autos_en_comun=jhon & jess
#---
print(f"\nAutos en común: {autos_en_comun}\nTotal: {len(autos_en_comun)}")