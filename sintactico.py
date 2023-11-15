import semantico

variables = []
mensajes = []

def finPrograma(tokens, i):
    if i+1 >= len(tokens):
        return True
    return False

def programa(tokens):
    i = 0
    funcion(tokens, i)
    print(i)

#Crear una funcion
def funcion(tokens, i):        
    if tokens[i].type.value == 3:         #Valor definido en el lexico para el void
        i += 1
        if id(tokens, i):           #Valida que sea un identificador
            i += 1
            if parantesisAbre(tokens, i):            #Si es una llave es una función
                i += 1
                if parentesisCierra(tokens, i):
                    i += 1                          #Avanzamos i a la siguiente posicion del arreglo de Tokens
                    if llaveAbre(tokens, i):
                        i += 1                      #Avanzamos i a la siguiente posicion del arreglo de Tokens
                        i = declaraciones(tokens, i)    #Declaraciones
                        i = instrucciones(tokens, i)    #Instrucciones
                        i += 1
                        if llaveCierra(tokens, i):
                            if finPrograma(tokens, i):
                                mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                                mensajes.append(mensaje)
                                return i
                            else:
                                return i
                        else:
                            mensaje = "Sintax error: Error en el '}' \n<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> }"
                            mensajes.append(mensaje) 
                    else:
                        mensaje = "Sintax error: Error en el '{' \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
                        mensajes.append(mensaje)
                else:
                    mensaje = "Sintax error: Error en el ')' \n<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
                    mensajes.append(mensaje)
    elif tokens[i].type.value == 6:         #Valor definido en el lexico para el int
        i += 1
        if id(tokens, i):           #Valida que sea un identificador
            i += 1
            if parantesisAbre(tokens, i):            #Si es una llave es una función
                i += 1
                if parentesisCierra(tokens, i):
                    i += 1                          #Avanzamos i a la siguiente posicion del arreglo de Tokens
                    if llaveAbre(tokens, i):
                        i += 1                      #Avanzamos i a la siguiente posicion del arreglo de Tokens
                        #i = instruccion(tokens, i)
                        #i += 1
                        if validReturn(tokens, i):
                            i += 1
                            if id(tokens, i):           #Valida que sea un identificador
                                i += 1
                            else:
                                mensaje = "Sintax error: Error en el 'return' \n <FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> } "
                                mensajes.append(mensaje)
                        else:
                           mensaje = "Sintax error: Error en el 'return' \n <FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> } "
                           mensajes.append(mensaje) 
                    else:
                        mensaje = "Sintax error: Error en el '{' \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
                        mensajes.append(mensaje)
                else:
                    mensaje = "Sintax error: Error en el ')' \n<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
                    mensajes.append(mensaje)
    return i

def declaraciones(tokens, i):
    while(tokens[i].type.value == 6 or tokens[i].type.value == 8):  #Ciclo que revisa las declaraciones
            i = declaracion(tokens, i)
            if i == None:           # i = None si hubo un error en la declaracion
                break
    return i

def tipo(tokens, i):
    try:
        if(tokens[i].type.value == 6):      #Valor definido en el lexico para el int
            i += 1
            if id(tokens, i):
                vars = semantico.Variable(tokens[i].lexema, tokens[i-1].lexema, '')
                variables.append(vars)
                i += 1
                if puntoComa(tokens, i):
                    i += 1
                    return i
                elif simboloAsignacion(tokens, i):
                    i += 1
                    if valorEntero(tokens, i):
                            i += 1
                            if puntoComa(tokens, i):
                                i += 1
                                return i
                            else:
                                mensaje = "Sintax error: Error en el ';' \n <FLOAT> <IDENTIFICADOR> = <VALOR_REAL>;"
                                mensajes.append(mensaje)
                                return None
                    else:
                        mensaje = "Sintax error: Error en el tipo \n <FLOAT> <IDENTIFICADOR> ;"
                        mensajes.append(mensaje)
                        return None
                else:
                    mensaje = "Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
                    mensajes.append(mensaje)
                    return None
            else:
                mensaje = "Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
                mensajes.append(mensaje)
                return None
        elif(tokens[i].type.value == 8):    #Valor definido en el lexico para el float      
                i += 1
                if id(tokens, i):
                    i += 1
                    if puntoComa(tokens, i):
                        i += 1
                        return i
                    elif simboloAsignacion(tokens, i):
                        i += 1
                        if valorReal(tokens, i):
                                i += 1
                                if puntoComa(tokens, i):
                                    i += 1
                                    return i
                                else:
                                    mensaje = "Sintax error: Error en el ';' \n <FLOAT> <IDENTIFICADOR> = <VALOR_REAL>;"
                                    mensajes.append(mensaje)
                                    return None
                        else:
                            mensaje = "Sintax error: Error en el valor \n <FLOAT> <IDENTIFICADOR> = <VALOR_REAL>;"
                            mensajes.append(mensaje)
                            return None
                    else:
                        mensaje = "Sintax error: Error en el tipo \n <FLOAT> <IDENTIFICADOR> ;"
                        mensajes.append(mensaje)
                        return None
                else:
                    mensaje = "Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
                    mensajes.append(mensaje)
                    return None
        else:
            mensaje = "Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
            mensajes.append(mensaje)
            return None
    except:
        mensaje = "Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
        mensajes.append(mensaje)



def id(tokens, i):
    try:
        if tokens[i].type.value == 50:       #Valor definido en el lexico para =
            return True
        else:
            return False
    except:
        return False
    
def validReturn(tokens, i):
    try:
        if tokens[i].type.value == 2:       #Valor definido en el lexico para el return
            return True
        else:
            return False
    except:
        return False
    
#Proceso de declaracion
def declaracion(tokens, i):        #Valida la declaracion
    i = tipo(tokens, i)
    return i

def instrucciones(tokens, i):
    while(tokens[i].type.value == 14 or tokens[i].type.value == 55):  #Ciclo que revisa las declaraciones
            i = instruccion(tokens, i)
            if i == None:           # i = None si hubo un error en la declaracion
                break
    return i

def instruccion(tokens, i):
    if tokens[i].type.value == 14:          #Valor definido en el lexico para if
        i += 1                              #Avanzamos i a la siguiente posicion del arreglo de Tokens
        i = condicion(tokens, i)
    elif tokens[i].type.value == 55:         #Valor definido en el lexico para el print
        i = palabraPrint(tokens, i)            #Valida que sea un identificador
    else:
        mensaje = "Sintax error: Error instruccion invalida "
        mensajes.append(mensaje) 
    print(i)
    return i

# -------- Instruccion print --------
def palabraPrint(tokens, i):
    try:
        if tokens[i].type.value == 55:          #Valor definido en el lexico para el identificador
            i += 1
            if parantesisAbre(tokens, i):            #Si es una llave es una función
                i += 1
                if cadena(tokens, i):
                    i+= 1
                    if parentesisCierra(tokens, i):
                        i += 1
                        if puntoComa(tokens, i):
                            if finPrograma(tokens, i):
                                mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                                mensajes.append(mensaje)
                                return i
                            else:
                                return i
                        else:
                            mensaje = "Sintax error: Error en la instruccion print \n<PRINT> -> print ( <CADENA> ) ;"
                            mensajes.append(mensaje)
                    else:
                        mensaje = "Sintax error: Error en la cadena \n<PRINT> -> print ( <CADENA> ) ;"
                        mensajes.append(mensaje)
                else:
                    mensaje = "Sintax error: Error en el ')' \n<PRINT> -> print ( <CADENA> ) ;"
                    mensajes.append(mensaje)
            else:
                mensaje = "Sintax error: Error en el '(' \n<PRINT> -> print ( <CADENA> ) ;"
                mensajes.append(mensaje)
    except:
        mensaje = "Sintax error: Error en la instruccion print \n<PRINT> -> print ( <CADENA> ) ;"
        mensajes.append(mensaje)

def cadena(tokens, i):
    try:
        if tokens[i].type.value == 53:          #Valor definido en el lexico para la cadena
            return True
        else:
            return False
    except:
        return False

def identificador(tokens, i, valor = 0):
    try:
        if tokens[i].type.value == 50:          #Valor definido en el lexico para el identificador
            i += 1
            if parantesisAbre(tokens, i):            #Si es una llave es una función
                i += 1
                if parentesisCierra(tokens, i):
                    i += 1                          #Avanzamos i a la siguiente posicion del arreglo de Tokens
                    if llaveAbre(tokens, i):
                        i += 1                      #Avanzamos i a la siguiente posicion del arreglo de Tokens
                        i = instruccion(tokens, i)
                        i += 1
                        if llaveCierra(tokens, i):
                            if finPrograma(tokens, i):
                                mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                                mensajes.append(mensaje)
                                return i
                            else:
                                return i
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
                i = tipo(tokens, i, valor)
                return i
            elif puntoComa(tokens, i):             #Si es un ; es una declaracion
                if finPrograma(tokens, i):
                    mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                    mensajes.append(mensaje)
                    return i
                else:
                    return i
            else:
                mensaje = "Sintax error: Error en el ';' "
                mensajes.append(mensaje)
        else:
            mensaje = "Sintax error: Error en el identificador"
            mensajes.append(mensaje)
    except:
        mensaje = "Sintax error: Error en el identificador"
        mensajes.append(mensaje)

def simboloAsignacion(tokens, i):
    try:
        if tokens[i].type.value == 40:       #Valor definido en el lexico para =
            return True
        else:
            return False
    except:
        return False
    
#--------------- Proceso de condicion -------------------
def condicion(tokens, i):
    if parantesisAbre(tokens, i):
        i += 1                              #Avanzamos i a la siguiente posicion del arreglo de Tokens
        i = comparacion(tokens, i)
        if parentesisCierra(tokens, i):
            i += 1                          #Avanzamos i a la siguiente posicion del arreglo de Tokens
            if llaveAbre(tokens, i):
                i += 1                      #Avanzamos i a la siguiente posicion del arreglo de Tokens
                i = instruccion(tokens, i)
                i += 1
                if llaveCierra(tokens, i):
                    if finPrograma(tokens, i):
                        mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
                        mensajes.append(mensaje)
                        return i
                    else:
                        return i
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
    
#---------------------- Tokens comunes ----------------------------
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

def valorEntero(tokens, i):
    try:
        if tokens[i].type.value == 51:       #Valor definido en el lexico para numero entero
            i += 1
            return i
        else:
            mensaje = "Sintax error: Error en el <VALOR_ENTERO> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;"
            mensajes.append(mensaje)
    except:
        mensaje = "Sintax error: Error en el <VALOR_ENTERO> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;"
        mensajes.append(mensaje)

def valorReal(tokens, i):
    try:
        if tokens[i].type.value == 52:       #Valor definido en el lexico para numero entero
            i += 1
            return i
        else:
            mensaje = "Sintax error: Error en el <VALOR_REAL> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_REAL> ;"
            mensajes.append(mensaje)
    except:
        mensaje = "Sintax error: Error en el <VALOR_REAL> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_REAL> ;"
        mensajes.append(mensaje)