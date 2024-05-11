"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    i = 5
    while i >= 0:
        result.append(i)
        i -= 1
    return result

   
   
 #  encontre dos forma de realizar esta tarea el metodo reverse que lo dejo comentado. con el bucle while el cual se esta ejecutando.  
    #for i in range(6):
        #    result.append(i)
        #list.reverse(result)
# Se Utiliza el metodo remplazo para realizar este ejercicio.
# Para validar que la funcion se ejecuta correctamente se utiliza el Print.
print (fn_hack_7())