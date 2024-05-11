"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    for i in range(6):
        result.append(i)
    return result  


# Utilice un bucle "for" sobre los números del 0 al 5 (usando range(6))
# Para validar que la funcion se ejecuta correctamente se utiliza el Print.

print (fn_hack_6())