import re
from enum import Enum

class TokenType(Enum):
	PalabraReservadaTrue = 0
	PalabraReservadaFalse = 1
	PalabraReservadaReturn = 2
	PalabraReservadaVoid = 3
	PalabraReservadaChar = 4
	PalabraReservadaShort = 5
	PalabraReservadaInt = 6
	PalabraReservadaLong = 7
	PalabraReservadaFloat = 8
	PalabraReservadaDo = 9
	PalabraReservadaWhile = 10
	PalabraReservadaFor = 11
	PalabraReservadaBreak = 12
	PalabraReservadaSwitch = 13
	PalabraReservadaIf = 14
	OperacionSuma = 15
	OperacionResta = 16
	OperacionIncremento = 17
	OperacionDecremento = 18
	OperacionMasIgual = 19
	OperacionMenosIgual = 20
	OperacionMultiplicacion = 21
	OperacionDivision = 22
	OperacionMultiplicacionIgual = 23
	OperacionDivisionIgual = 24
	OperacionModulo = 25
	OperacionModuloIgual = 26
	ANDBits = 27
	ANDLogico = 28
	ORBits = 29
	ORLogico = 30
	MayorQue = 31
	MenorQue = 32
	MayorIgualQue = 33
	MenorIgualQue = 34
	IgualA = 35
	DiferenteDe = 36
	Negacion = 37
	CorrimientoHaciaLaDerecha = 38
	CorrimientoHaciaLaIzquierda = 39
	Asignacion = 40
	Dolar = 41
	LlaveAbre = 42
	LlaveCierra = 43
	ParentesisAbre = 44
	ParentesisCierra = 45
	CorcheteAbre = 46
	CorcheteCierra = 47
	Coma = 48
	PuntoComa = 49
	Identificador = 50
	Numero = 51
	NumeroFlotante = 52
	Cadena = 53
	Desconocido = 54
	PalabraReservadaPrint = 55
	PalabraReservadaElse = 56

class Token:
	def __init__(self, type: TokenType, lexema: str, line: int):
		self.type = type
		self.lexema = lexema
		self.line = line

	def __str__(self):
		return f'Token: {token_types[self.type.value][1]:<32s}Lexema: {self.lexema:<24s}Linea: {self.line}'
	
token_types = [
	('true', 'Palabra reservada true'),
	('false', 'Palabra reservada false'),
	('return', 'Palabra reservada return'),
	('void', 'Palabra reservada void'),
	('char', 'Palabra reservada char'),
	('short', 'Palabra reservada short'),
	('int', 'Palabra reservada int'),
	('long', 'Palabra reservada long'),
	('float', 'Palabra reservada float'),
	('do', 'Palabra reservada do'),
	('while', 'Palabra reservada while'),
	('for', 'Palabra reservada for'),
	('break', 'Palabra reservada break'),
	('switch', 'Palabra reservada switch'),
	('if', 'Palabra reservada if'),
	('+', 'Operacion suma'),
	('-', 'Operacion resta'),
	('++', 'Operacion incremento'),
	('--', 'Operacion decremento'),
	('+=', 'Operacion mas igual'),
	('-=', 'Operacion menos igual'),
	('*', 'Operacion multiplicacion'),
	('/', 'Operacion division'),
	('*=', 'Operacion multiplicacion igual'),
	('/=', 'Operacion division igual'),
	('%', 'Operacion modulo'),
	('%=', 'Operacion modulo igual'),
	('&', 'AND a nivel de bits'),
	('&&', 'AND logico'),
	('|', 'OR a nivel de bits'),
	('||', 'OR logico'),
	('>', 'Mayor que'),
	('<', 'Menor que'),
	('>=', 'Mayor o igual que'),
	('<=', 'Menor o igual que'),
	('==', 'Igual a'),
	('!=', 'Diferente de'),
	('!', 'Negacion'),
	('>>', 'Corrimiento hacia la derecha'),
	('<<', 'Corrimiento hacia la izquierda'),
	('=', 'Asignacion'),
	('$', 'Simbolo dolar'),
	('{', 'Llave abre'),
	('}', 'Llave cierra'),
	('(', 'Parentesis abre'),
	(')', 'Parentesis cierra'),
	('[', 'Corchete abre'),
	(']', 'Corchete cierra'),
	(',', 'Coma'),
	(';', 'Punto y coma'),
	('', 'Identificador'),
	('', 'Numero'),
	('', 'Numero flotante'),
	('', 'Cadena'),
	('', 'Desconocido'),
	('print', 'Palabra reservada print'),
 	('else', 'Palabra reservada else'),
]

# Determinar si un caracter es operador
def is_operator(c):
	operators_symbols = "+-*/%!=&|<>"
	return c in operators_symbols

# Determinar si un caracter es separador
def is_separator(c):
	separators_symbols = "{}()[],;"
	return c in separators_symbols

# Validar un numero
def valid_number(string):
	try:
		number = float(string)
		if number.is_integer():
			return 1
		else:
			return 2
		
	except ValueError:
		return 0

# Validar un identificador
def valid_id(nombre):
	pattern = r"[a-zA-Z_][a-zA-Z0-9_]*"
	return re.match(pattern, nombre) is not None

# dividir el codigo en lexemas y su correspondiente linea de codigo
def split_code(code: str):

	# Vector de tuplas de la forma (lexema, numLinea)
	vector = []
	vector_aux = []

	# Cadena auxiliar
	string_aux = ''

	# Enumerar lineas
	lineas_codigo = code.split('\n')
	for linea_numero, linea_string in enumerate(lineas_codigo, start=1):
		vector_aux.append((linea_string, linea_numero))
	
	vector = vector_aux
	vector_aux = []

	# Separar strings
	linea = 0
	while linea < len(vector):
		string_aux = str()

		index = 0
		while index < len(vector[linea][0]):
			c = vector[linea][0][index]

			if c != '\"':
				string_aux += c
				index += 1
			else:
				if string_aux:
					vector_aux.append((string_aux, vector[linea][1]))
				string_aux = str()

				index = index + 1
				while linea < len(vector):
					if (index < len(vector[linea][0])):
						c = vector[linea][0][index]
						if (c != '\"'):
							string_aux += c
							index += 1
						else:
							vector_aux.append(('\"' + string_aux + '\"', vector[linea][1]))
							string_aux = str()
							index += 1
							break
					else:
						string_aux += '\n'
						linea += 1
						index = 0
		
		if string_aux:
			vector_aux.append((string_aux, vector[linea][1]))
			linea += 1

	vector = vector_aux
	vector_aux = []

	# Separar espacios en blanco
	for l in vector:
		# Ignorar strings
		if l[0][0] == '\"':
			vector_aux.append(l)
			continue
		
		temp = l[0].split()
		vector_aux.extend([(j, l[1]) for j in temp])

	vector = vector_aux
	vector_aux = []

	# Dividir separadores
	for l in vector:
		# Ignorar strings
		if l[0][0] == '\"':
			vector_aux.append(l)
			continue

		string_aux = str()
		for c in l[0]:
			if is_separator(c):
				if string_aux:
					vector_aux.append((string_aux, l[1]))
					string_aux = str()
				vector_aux.append((c, l[1]))
			else:
				string_aux += c
		if string_aux:
			vector_aux.append((string_aux, l[1]))

	vector = vector_aux
	vector_aux = []

	# Separar operadores
	for l in vector:
		# Ignorar strings
		if l[0][0] == '"':
			vector_aux.append(l)
			continue

		string_aux = str()
		it = 0

		while it < len(l[0]):
			c = l[0][it]

			if is_operator(c):
				if string_aux:
					vector_aux.append((string_aux, l[1]))
					string_aux = str()

				operator = c

				# Concatenar a operator todos los caracteres operadores
				temp_string = c
				it += 1
				while it < len(l[0]) and is_operator(l[0][it]):
					temp_string += l[0][it]
					it += 1

				vector_aux.append((temp_string, l[1]))
			else:
				string_aux += c
				it += 1

		if string_aux:
			vector_aux.append((string_aux, l[1]))

	vector = vector_aux
	vector_aux = []

	return vector

def get_tokens(code: str):

	words = split_code(code)

	tokens = []

	for w in words:
		found = False
		index = 0

		for i in token_types:
			if (i[0] == w[0]):
				found = True
				break
			index += 1

		if (found):
			tokens.append(Token(TokenType(index), w[0], w[1]))
		elif (w[0][0] == '\"'):
			tokens.append(Token(TokenType.Cadena, w[0], w[1]))
		elif (valid_id(w[0])):
			tokens.append(Token(TokenType.Identificador, w[0], w[1]))
		elif (valid_number(w[0]) != 0):
			tipo = valid_number(w[0])
			if (tipo == 1):
				tokens.append(Token(TokenType.Numero, w[0], w[1]))
			else:
				tokens.append(Token(TokenType.NumeroFlotante, w[0], w[1]))
		else:
			tokens.append(Token(TokenType.Desconocido, w[0], w[1]))

	return tokens