#from lexico import token_types, get_tokens

class Variable:
	def __init__(self, identificador, tipo, valor):
		self.identificador = identificador
		self.tipo = tipo
		self.valor = valor

	def setValor(self, valor):
		self.valor = valor
	
	def setId(self, identificador):
		self.identificador = identificador
