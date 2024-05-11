"""
text: "fooziman" output => "FOOZIMAN"
"""

def fn_hack_1():
    result = "fooziman"
    result = result.upper()
    return result

# Para validar que la funcion se ejecuta correctamente se utiliza el Print.
print(fn_hack_1()) 
