from lexico import *

class Variable:
	def __init__(self, identificador, tipo, valor):
		self.identificador = identificador
		self.tipo = tipo
		self.valor = valor

	def setValor(self, valor):
		self.valor = valor
	
	def setId(self, identificador):
		self.identificador = identificador

def buscarVar(token, vars):
	for var in vars:
		if token.lexema == var.identificador:
			return var
	return None

def buscarValor(var):
	if var.valor is not '':
		return var
	return None