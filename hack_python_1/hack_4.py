"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result[:-1] + result[-1].upper()
    return result


# indico que me tome todos los caracteres la palabra execto la ultima. 
# luego indico que acceda a la ultima letra "N" e indico que coloque en mayuscula.
# Para validar que la funcion se ejecuta correctamente se utiliza el Print.
print (fn_hack_4())
