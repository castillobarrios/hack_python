"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    output = []
    for i in range(len(result)):
        output.append(result[i])
        if i < len(result) + 1:
            output.append('@')
    return output 

# se Utiliza el siglo for y con el metodo .append
# Para validar que la funcion se ejecuta correctamente se utiliza el Print.
print (fn_hack_9())