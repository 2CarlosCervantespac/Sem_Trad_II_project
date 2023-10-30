mensajes = []

def programa(tokens):
    i = 0
    if tokens[i].type.value == 14:          #Valor definido en el lexico para if
        i += 1                              #Avanzamos i a la siguiente posicion del arreglo de Tokens
        condicion(tokens, i)
    elif tokens[i].type.value == 4:         #Valor definido en el lexico para el char
        valor = 4                            #Tipo de dato que necesita
        i += 1
        identificador(tokens, i, valor)            #Valida que sea un identificador
    elif tokens[i].type.value == 6:         #Valor definido en el lexico para el int
        valor = 6
        i += 1
        identificador(tokens, i, valor)            #Valida que sea un identificador
    elif tokens[i].type.value == 8:         #Valor definido en el lexico para el float
        valor = 8
        i += 1
        identificador(tokens, i, valor)            #Valida que sea un identificador
    else:
        mensaje = "Sintax error: Error instruccion invalida "
        mensajes.append(mensaje)
    #i = declaracion(tokens, i)
    #if len(tokens) != i+1:
    #    i = asignacion(tokens, i)


def identificador(tokens, i, valor = 0):
    try:
        if tokens[i].type.value == 50:          #Valor definido en el lexico para el identificador
            i += 1
            if llaveAbre(tokens, i):            #Si es una llave es una función
                i += 1
                if parentesisCierra(tokens, i):
                    i += 1                          #Avanzamos i a la siguiente posicion del arreglo de Tokens
                    if llaveAbre(tokens, i):
                        i += 1                      #Avanzamos i a la siguiente posicion del arreglo de Tokens
                        if llaveCierra(tokens, i):
                            mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                            mensajes.append(mensaje)
                        else:
                            mensaje = "Sintax error: Error en el '}' \n<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> }"
                            mensajes.append(mensaje) 
                    else:
                        mensaje = "Sintax error: Error en el '{' \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
                        mensajes.append(mensaje)
                else:
                    mensaje = "Sintax error: Error en el ')' \n<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
                    mensajes.append(mensaje)
            elif simboloAsignacion(tokens, i):     #Si es un = es una asignacion y declaracion
                i += 1
                tipo(tokens, i, valor)
            elif puntoComa(tokens, i):             #Si es un ; es una declaracion
                mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                mensajes.append(mensaje)
            else:
                mensaje = "Sintax error: Error en el ';' "
                mensajes.append(mensaje)
        else:
            mensaje = "Sintax error: Error en el identificador"
            mensajes.append(mensaje)
    except:
        mesnaje = "Sintax error: Error en el identificador"
        mensajes.append(mensaje)

def simboloAsignacion(tokens, i):
    try:
        if tokens[i].type.value == 40:       #Valor definido en el lexico para =
            return True
        else:
            return False
    except:
        return False
    
def tipo(tokens, i, valor):
    try:
        if valor == 4:                       #Valor definido en el lexico para el char
            i += 1
            if puntoComa(tokens, i):        #Valida que haya punto y coma
                mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                mensajes.append(mensaje)
            else: 
                mensaje = "Sintax error: Error en el ; \n <CHAR> <IDENTIFICADOR> = ' <CARACTER> ' ;"
                mensajes.append(mensaje)
        elif valor == 6:         #Valor definido en el lexico para el int
            if tokens[i].type.value == 51:            #Valor definido en el lexico para numeros enteros
                i += 1
                if puntoComa(tokens, i):        #Valida que haya punto y coma
                    mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                    mensajes.append(mensaje)
                else: 
                    mensaje = "Sintax error: Error en el ; \n <INT> <IDENTIFICADOR> = ' <ENTERO> ' ;"
                    mensajes.append(mensaje)
            else:
                mensaje = "Sintax error: Error en el tipo \n <INT> <IDENTIFICADOR> = ' <ENTERO> ' ;"
                mensajes.append(mensaje)
        elif valor == 8:         #Valor definido en el lexico para el float
            if tokens[i].type.value == 52:            #Valor definido en el lexico para numeros flotantes
                i += 1
                if puntoComa(tokens, i):        #Valida que haya punto y coma
                    mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                    mensajes.append(mensaje)
                else: 
                    mensaje = "Sintax error: Error en el ; \n <FLOAT> <IDENTIFICADOR> = ' <FLOTANTE> ' ;"
                    mensajes.append(mensaje)
            else:
                mensaje = "Sintax error: Error en el tipo \n <FLOAT> <IDENTIFICADOR> = ' <FLOTANTE> ' ;"
                mensajes.append(mensaje)
        else:
            mensaje = "Sintax error: Error en el tipo \n <TIPO> <IDENTIFICADOR> = <VALOR> ;"
            mensajes.append(mensaje)
    except:
        mensaje = "Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
        mensajes.append(mensaje)


#Proceso de condicion
def condicion(tokens, i):
    if parantesisAbre(tokens, i):
        i += 1                              #Avanzamos i a la siguiente posicion del arreglo de Tokens
        i = comparacion(tokens, i)
        if parentesisCierra(tokens, i):
            i += 1                          #Avanzamos i a la siguiente posicion del arreglo de Tokens
            if llaveAbre(tokens, i):
                i += 1                      #Avanzamos i a la siguiente posicion del arreglo de Tokens
                if llaveCierra(tokens, i):
                    mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                    mensajes.append(mensaje)
                else:
                    mensaje = "Sintax error: Error en el '}' \n<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> }"
                    mensajes.append(mensaje) 
            else:
                mensaje = "Sintax error: Error en el '{' \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
                mensajes.append(mensaje)
        else:
            mensaje = "Sintax error: Error en el ')' \n<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
            mensajes.append(mensaje)
    else:
        mensaje = "Sintax error: Error en el '('  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        

def puntoComa(tokens, i):
    try:
        if tokens[i].type.value == 49:       #Valor definido en el lexico para el ;
            return True
        else:
            return False
    except:
        return False

def llaveAbre(tokens, i):
    try:
        if tokens[i].type.value == 42:          #Valor definido en el lexico para {
            return True
        else:
            return False
    except:
        return False

def llaveCierra(tokens, i):
    try:
        if tokens[i].type.value == 43:  # Valor definido en el léxico para }
            return True
        else:
            return False
    except:
        return False

def parantesisAbre(tokens, i):
    try:
        if tokens[i].type.value == 44:          #Valor definido en el lexico para (
            return True
        else:
            return False
    except:
        return False

def parentesisCierra(tokens, i):
    try:
        if tokens[i].type.value == 45:          #Valor definido en el lexico para )
            return True
        else:
            return False
    except:
        return False

def comparacion(tokens, i):
    i = operador(tokens, i)                     #Valida el operador
    if i == -1:
        mensaje = "Sintax error: Error en el operador <COMPARACION> -> <OPERADOR> <OP_COMPARACION> <OPERADOR> "
        mensajes.append(mensaje)
    else:
        i = opComparacion(tokens, i)
        if i == -1:
            mensaje = "Sintax error: Error en el operador de comparacion <COMPARACION> -> <OPERADOR> <OP_COMPARACION> <OPERADOR> "
            mensajes.append(mensaje)
        else:
            i = operador(tokens, i)
            if i == -1:
                mensaje = "Sintax error: Error en el operador de comparacion \n<COMPARACION> -> <OPERADOR> <OP_COMPARACION> <OPERADOR> "
                mensajes.append(mensaje)
            else:
                return i

def operador(tokens, i):
    if tokens[i].type.value == 50:              #Valor definido en el lexico para el identificador
        i += 1
        return i
    elif tokens[i].type.value == 51:            #Valor definido en el lexico para numeros enteros
        i += 1
        return i
    else:
        return -1

def opComparacion(tokens, i):
    if tokens[i].type.value == 31:              #Valida operadores validos ( >, <, >=, <=, ==, !=)
        i += 1
        return i
    elif tokens[i].type.value == 32:
        i += 1
        return i
    elif tokens[i].type.value == 33:
        i += 1
        return i
    elif tokens[i].type.value == 34:
        i += 1
        return i
    elif tokens[i].type.value == 35:
        i += 1
        return i
    elif tokens[i].type.value == 36:
        i += 1
        return i
    else:
        return -1


def valorEntero(tokens, i):
    try:
        if tokens[i].type.value == 51:       #Valor definido en el lexico para numero entero
            i += 1
            puntoComa(tokens, i)                #Valida que haya ;
        else:
            mensaje = "Sintax error: Error en el <VALOR_ENTERO> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;"
            mensajes.append(mensaje)
    except:
        mensaje = "Sintax error: Error en el <VALOR_ENTERO> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;"
        mensajes.append(mensaje)

#Proceso de declaracion
def declaracion(tokens, i):        #Valida la declaracion
    i = tipo(tokens, i)
    return i