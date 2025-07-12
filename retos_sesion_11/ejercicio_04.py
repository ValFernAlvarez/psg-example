'''
4. Gestión de hábitats en peligro: Crea un diccionario que asocie
especies animales en peligro de extinción con información sobre
sus hábitats amenazados, lo que permite priorizar la protección
de áreas críticas para la supervivencia de estas especies
    a. Añade al diccionario 2 habitats más usando update() con
        2 especies cada uno
    b.Existe en el diccionario el habitat 'amazonas'?
    c. Añade al amazonas la especie 'anaconda'
'''
habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}},
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}}}
#---Para 'a'---
habitats.update({
    "sabana africana": {
        "especies": {"elefante", "jirafa"}},
    "oceano pacifico": {
        "especies": {"delfín rosado", "tortuga laúd"}}})
print(f"\nPARA 'A':\nDiccionario de Habitats +2 Habitats:\n{habitats}")
#---Para 'b'---
existe_amazonas="amazonas" in habitats
print(f"\nPARA 'B':\n¿Existe 'amazonas'?: {existe_amazonas}")
#---Para 'c'---
habitats["amazonas"]["especies"].update({"anaconda"})
print(f"\nPARA 'C':\nDiccionario de Habitats +2 'anaconda':\n{habitats}")
