class Etiqueta:
	def __init__(self, id, numLinea):
		self.id = id
		self.numLinea = numLinea

etiquetas = []

def declaraciones(var, valor, cadena):
    cadena += var + ' = ' + valor + '\n'
    return cadena

def bucleWhile(var, var2, opCom, cadena):
    num = etiquetas.count()
    id = 'L'+num
    etiqueta = Etiqueta(id, num)
    cadena += 'if ' + var + ' ' + opCom + ' ' + var2 + ' goto ' + id
    print(var + ' ' + var2 + ' ' + opCom + ' ' + cadena)
    return cadena