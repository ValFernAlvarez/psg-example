'''
3. Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online.
        a. Quiénes compraron en ambos canales.
        b. Quiénes compraron solo en la tienda física.
        c. Quiénes compraron solo online.
'''
tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]
#---
conjunto_tienda_fisica=set(tienda_fisica)
conjunto_tienda_online=set(tienda_online)
#-Para a--
ambos_canales=conjunto_tienda_fisica & conjunto_tienda_online
#-Para b--
solo_fisico=conjunto_tienda_fisica-conjunto_tienda_online
#-Para c--
solo_online=conjunto_tienda_online-conjunto_tienda_fisica
#---
print(f"Para 'a': {ambos_canales}\nPara 'b': {solo_fisico}\nPara 'c': {solo_online}")