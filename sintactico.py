from semantico import *
import cod3direcciones as cod3Dir

vars = []
mensajes = []

def finPrograma(tokens, i):
    if i+1 > len(tokens):
        return True
    return False

def programa(tokens):
    i = 0
    vars.clear()
    mensajes.clear()
    cod3Dir.reiniciarLineas()
    i = funcion(tokens, i)
    if i != None:
        codigo = cod3Dir.showLineas()
        return codigo

#Crear una funcion
def funcion(tokens, i):    
    if tokens[i].type.value != 3:         #Valor definido en el lexico para el void
        mensaje = "Sintax error: Error en el 'tipo' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    i += 1
    if not id(tokens, i):           #Valida que sea un identificador
        mensaje = "Sintax error: Error en el 'identificador' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    i += 1
    if not parantesisAbre(tokens, i):
        mensaje = "Sintax error: Error en el '(' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    i += 1
    if not parentesisCierra(tokens, i):
        mensaje = "Sintax error: Error en el ')' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    i += 1
    if not llaveAbre(tokens, i):
        mensaje = "Sintax error: Error en el '{' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    i += 1          #Avanzamos i a la siguiente posicion del arreglo de Tokens
    i = declaraciones(tokens, i)    #Declaraciones
    if i is None:
        return None
    i = instrucciones(tokens, i)
    if i is None:
        return None
    if not llaveCierra(tokens, i):
        mensaje = "Sintax error: Error en el '}' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    i += 1
    cod3Dir.fin()
    if finPrograma(tokens, i):
        mensaje = "Syntax analysis completed with no errors \nProcess finished with exit code 0"
        mensajes.append(mensaje)
        return i
    else:
        mensaje = "Sintax error: Error en el '}' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    
#------------------------ Proceso de declaracion -----------------------------
def declaraciones(tokens, i):
    while sig_declaracion(tokens, i):  #Ciclo que revisa las declaraciones
        i = declaracion(tokens, i)
        if i is None:           # i = None si hubo un error en la declaracion
            return None
        if puntoComa(tokens, i):
            i += 1
        elif simboloAsignacion(tokens, i):  # Validar si es declaracion-asigancion
            i += 1
            var = vars.pop()
            if validVar(tokens, i, var):
                i += 1
                if puntoComa(tokens, i):
                    cod3Dir.declaraciones(var.identificador, var.valor)
                    i += 1
                else:
                    mensaje = "Sintax error: Error en el ';' \n<TIPO_INT> <IDENTIFICADOR> = <VALOR_ENTERO> ;"
                    mensajes.append(mensaje)
                    return None
            else:
                return None
        else:
            mensaje = "Sintax error: Error en el ';' \n<DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
            mensajes.append(mensaje)
            return None
    return i

def sig_declaracion(tokens, i):
    if tokens[i].type.value == 6 or tokens[i].type.value == 8:  #Revisa si el token actual es una declaracion
        return True
    return False 

def declaracion(tokens, i):        #Valida la declaracion
    i = tipo(tokens, i)
    if i is None:
        mensaje = "Sintax error: Error en el 'tipo' \n<DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
        mensajes.append(mensaje)
        return None
    if id(tokens, i):
        var = vars.pop()
        var.setId(tokens[i].lexema)
        vars.append(var)
        i += 1
        return i
    mensaje = "Sintax error: Error en el 'identificador' \n<DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
    mensajes.append(mensaje)
    return None

def tipo(tokens, i):
    if(tokens[i].type.value == 6):      #Valor definido en el lexico para el int
        var = Variable( '', 6, '')     #Se crea Nueva variable de tipo int
        vars.append(var)
        i += 1
        return i
    elif(tokens[i].type.value == 8):    #Valor definido en el lexico para el float
        var = Variable( '', 8, '')     #Se crea Nueva variable de tipo float
        vars.append(var)
        i += 1
        return i
    else:
        mensaje = "Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;"
        mensajes.append(mensaje)
        return None

def id(tokens, i):
    try:
        if tokens[i].type.value == 50:       #Valor definido en el lexico para Identificador
            return True
        else:
            return False
    except:
        return False
    
def validVar(tokens, i, var):
    if(var.tipo == 6):      #Valor definido en el lexico para el int
        if valorEntero(tokens, i):
            var.setValor(tokens[i].lexema)
            vars.append(var)
            return True
        return False
    elif(var.tipo == 8):    #Valor definido en el lexico para el float
        if valorReal(tokens, i):
            var.setValor(tokens[i].lexema)
            vars.append(var)
            return True
        return False
    else:
        mensaje = "Sintax error: Error en el 'valor' \nValor Invalido"
        mensajes.append(mensaje)
        return False
    
#------------------ Proceso de instrucciones -----------------------
def instrucciones(tokens, i):
    while sig_instruccion(tokens, i):  #Ciclo que revisa las declaraciones
            i = instruccion(tokens, i)
            if i is None:           # i = None si hubo un error en la declaracion
                break
            i += 1
    return i

def sig_instruccion(tokens, i):
    if tokens[i].type.value == 14 or tokens[i].type.value == 55 or tokens[i].type.value == 10 or tokens[i].type.value == 50:  #Revisa si el token actual es una instruccion
        return True
    return False

def instruccion(tokens, i):
    if tokens[i].type.value == 14:          #Valor definido en el lexico para if
        i += 1                              #Avanzamos i a la siguiente posicion del arreglo de Tokens
        i = condicion(tokens, i)
    elif tokens[i].type.value == 10:          #Valor definido en el lexico para while
        i += 1                              #Avanzamos i a la siguiente posicion del arreglo de Tokens
        i = bucle(tokens, i)
    elif tokens[i].type.value == 55:         #Valor definido en el lexico para el print
        i += 1
        i = instruccionPrint(tokens, i)            #Valida que sea un print
    elif tokens[i].type.value == 50:              #Valor definido en el lexico para el identificador
        i = asignacion(tokens, i)                   #Proceso de asignacion
    else:
        mensaje = "Sintax error: Error instruccion invalida "
        mensajes.append(mensaje) 
    return i

#------------------ Proceso de asinacion -----------------------
def asignacion(tokens, i):
    var = buscarVar(tokens[i], vars)
    if var is None:
        mensaje = "Semantic error: Error en la variable, variable no declarada"
        mensajes.append(mensaje)
        return None
    i += 1
    if not simboloAsignacion(tokens, i):
        mensaje = "Sintax error: Error en el '=' \n<ASIGNAR> -> <IDENTIFICADOR> = <EXP_ARIT> ;"
        mensajes.append(mensaje)
        return None
    i += 1
    i = exprAritmetica(tokens, i, var)
    if i is None:
        return None
    if not puntoComa(tokens, i):
        mensaje = "Sintax error: Error en el ';' \n<ASIGNAR> -> <IDENTIFICADOR> = <EXP_ARIT> ;"
        mensajes.append(mensaje)
        return None
    return i

def exprAritmetica(tokens, i, var):
    i = operador(tokens, i)                     #Valida el operador
    if i is None:
        return None
    var1 = tokens[i-1].lexema
    i = opArit(tokens, i)
    if i is None:
        return None
    opeArit = tokens[i-1].lexema
    i = operador(tokens, i)
    if i is None:
        return None
    var2 = tokens[i-1].lexema
    cod3Dir.asignacionArit(var.identificador, var1, var2, opeArit)
    return i

def opArit(tokens, i):
    if tokens[i].type.value == 15:              #Valida operadores validos ( +, -, *, /)
        i += 1
        return i
    elif tokens[i].type.value == 16:
        i += 1
        return i
    elif tokens[i].type.value == 21:
        i += 1
        return i
    elif tokens[i].type.value == 22:
        i += 1
        return i
    else:
        mensaje = "Sintax error: Error en el 'operador aritmetico' <EXP_ARIT> -> <OPERADOR> <OP_ARITMETICO> <OPERADOR> "
        mensajes.append(mensaje)
        return None
# -------- Instruccion print ----------
def instruccionPrint(tokens, i):
    try:
        if not parantesisAbre(tokens, i):
            mensaje = "Sintax error: Error en la instruccion '(' \n<PRINT> -> print ( <CADENA> ) ;"
            mensajes.append(mensaje)
            return None
        i += 1
        if not cadena(tokens, i):
            mensaje = "Sintax error: Error en la cadena \n<PRINT> -> print ( <CADENA> ) ;"
            mensajes.append(mensaje)
            return None
        i += 1
        if not parentesisCierra(tokens, i):
            mensaje = "Sintax error: Error en la instruccion ')' \n<PRINT> -> print ( <CADENA> ) ;"
            mensajes.append(mensaje)
            return None
        i += 1
        if not puntoComa(tokens, i):
            mensaje = "Sintax error: Error en la instruccion ';' \n<PRINT> -> print ( <CADENA> ) ;"
            mensajes.append(mensaje)
            return None
        if finPrograma(tokens, i):
            mensaje = "Sintax error: Error en el '}' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
            mensajes.append(mensaje)
            return None
        else:
            return i
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

#--------------- Proceso de bucle -------------------
def bucle(tokens, i):
    lineas = []        
    if not parantesisAbre(tokens, i):
        mensaje = "Sintax error: Error en el '('  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    i += 1                              #Avanzamos i a la siguiente posicion del arreglo de Tokens
    i = comparacion(tokens, i, lineas)          #Reviso la comparacion
    print(lineas)
    if i is None:
        return None
    if not parentesisCierra(tokens, i):
        mensaje = "Sintax error: Error en el ')'  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    i += 1
    if not llaveAbre(tokens, i):
        mensaje = "Sintax error: Error en el '{'  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    i += 1
    i = instrucciones(tokens, i)
    if i is None:
        return None
    if not llaveCierra(tokens, i):
        mensaje = "Sintax error: Error en el '{'  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    cod3Dir.cerrarBucle(lineas)
    if finPrograma(tokens, i):
        mensaje = "Sintax error: Error en el '}' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    else:
        return i
#--------------- Proceso de condicion -------------------
def condicion(tokens, i):
    lineas = []
    if not parantesisAbre(tokens, i):
        mensaje = "Sintax error: Error en el '('  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    i += 1                              #Avanzamos i a la siguiente posicion del arreglo de Tokens
    i = comparacion(tokens, i, lineas)          #Reviso la comparacion
    if i is None:
        return None
    if not parentesisCierra(tokens, i):
        mensaje = "Sintax error: Error en el ')'  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    i += 1
    if not llaveAbre(tokens, i):
        mensaje = "Sintax error: Error en el '{'  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    i += 1
    i = instrucciones(tokens, i)
    if i is None:
        return None
    if not llaveCierra(tokens, i):
        mensaje = "Sintax error: Error en el '{'  \n <CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    cod3Dir.cerrarIf(lineas)#Cierre de 3 direcciones
    if palabraElse(tokens, i+1):
        i += 2
        i = condicionElse(tokens, i)
    if i is None:
        return None
    if finPrograma(tokens, i):
        mensaje = "Sintax error: Error en el '}' \n<FUNCION> -> <TIPO> <IDENTIFICADOR> ( ) { <ORDENES> <INSTRUCCIONES> }"
        mensajes.append(mensaje)
        return None
    else:
        return i

#---------------- Proceso de else -----------------
def condicionElse(tokens, i):
    if not llaveAbre(tokens, i):
        mensaje = "Sintax error: Error en el '{'  \n <ELSE> -> else { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    i += 1
    i = instrucciones(tokens, i)
    if i is None:
        return None
    if not llaveCierra(tokens, i):
        mensaje = "Sintax error: Error en el '}'  \n <ELSE> -> else { <ORDENES> } "
        mensajes.append(mensaje)
        return None
    return i
#---------------- Proceso de comparacion -----------------
def comparacion(tokens, i, lineas):
    i = operador(tokens, i)                     #Valida el operador
    if i is None:
        return None
    var = tokens[i-1].lexema
    i = opComparacion(tokens, i)
    if i is None:
        return None
    opCom = tokens[i-1].lexema
    i = operador(tokens, i)
    if i is None:
        return None
    var1 = tokens[i-1].lexema
    num = cod3Dir.saltoWhile(var, var1, opCom)
    lineas.append(num)
    return i

def operador(tokens, i):
    if tokens[i].type.value == 50:              #Valor definido en el lexico para el identificador
        var = buscarVar(tokens[i], vars)
        if var is None:
            mensaje = "Semantic error: Error en la variable, variable no declarada"
            mensajes.append(mensaje)
            return None
        var = buscarValor(var)
        if var is None:
            mensaje = "Semantic error: Error en la variable, valor de la variable no definida"
            mensajes.append(mensaje)
            return None
        i += 1
        return i
    elif tokens[i].type.value == 51:            #Valor definido en el lexico para numeros enteros
        i += 1
        return i
    else:
        mensaje = "Sintax error: Error en el 'operador' <COMPARACION> -> <OPERADOR> <OP_COMPARACION> <OPERADOR> "
        mensajes.append(mensaje)
        return None

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
        mensaje = "Sintax error: Error en el 'operador de comparacion' <COMPARACION> -> <OPERADOR> <OP_COMPARACION> <OPERADOR> "
        mensajes.append(mensaje)
        return None

def palabraElse(tokens, i):
    try:
        if tokens[i].type.value == 56:       #Valor definido en el lexico para el ;
            return True
        else:
            return False
    except:
        return False

#---------------------- Tokens comunes ----------------------------
def puntoComa(tokens, i):
    try:
        if tokens[i].type.value == 49:       #Valor definido en el lexico para el ;
            return True
        else:
            return False
    except:
        return False

def simboloAsignacion(tokens, i):
    try:
        if tokens[i].type.value == 40:       #Valor definido en el lexico para =
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
            return True
        else:
            mensaje = "Sintax error: Error en el <VALOR_ENTERO> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;"
            mensajes.append(mensaje)
            return False
    except:
        mensaje = "Sintax error: Error en el <VALOR_ENTERO> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;"
        mensajes.append(mensaje)
        return False

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