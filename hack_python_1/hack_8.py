"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    result = result[1:4]
    return result  


# se utiliza la sintaxis slicing
# Para validar que la funcion se ejecuta correctamente se utiliza el Print. 
print (fn_hack_8())