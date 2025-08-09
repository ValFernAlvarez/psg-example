'''
2. Construir el operador XNOR en Python
'''
print ("Operador XNOR")

a = False
b = False
print("A: ",a," B: ", b, " Valor: ",(a and b) or (not a and not b))
#---

a = False
b = True
print("A: ",a," B: ", b, "  Valor: ",(a and b) or (not a and not b))
#---

a=True
b=False
print("A: ",a,"  B: ", b, " Valor: ",(a and b) or (not a and not b))
#---

a=True
b=True
print("A: ",a,"  B: ", b, "  Valor: ",(a and b) or (not a and not b))