"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    nueva_Lista = ['F', '0', '0', 'Z', '1', 'M', '@', 'N']
    return nueva_Lista


# Se crea una nueva lista y se manda a Imprimir
# Tambien se puede realizar de otra manera que la dejare comentada.

#def fn_hack_10(input_string):
#    result = [char.upper() for char in input_string]
#    result = ['0' if char == 'O' else '1' if char == 'I' else '@' if char == 'A' else char for char in result]
#    return result

#input_string = "fooziman"
#output = fn_hack_10(input_string)

#print (output)
#print (fn_hack_10())