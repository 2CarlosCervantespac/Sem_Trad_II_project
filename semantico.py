from lexico import token_types, get_tokens

class Variable:
	def __init__(self, id, tipo, valor):
		self.id = id
		self.tipo = tipo
		self.valor = valor

	def setValor(self, valor):
		self.valor = valor