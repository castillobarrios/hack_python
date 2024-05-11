"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    result = "fooziman"
    result = result.capitalize()
    return result

# Para validar que la funcion se ejecuta correctamente se utiliza el Print.
print (fn_hack_3())