def programa(tokens):
    i = 0

    condicion(tokens, i)
    #i = declaracion(tokens, i)
    #if len(tokens) != i+1:
    #    i = asignacion(tokens, i)

#Proceso funcion
def funcion(tokens, i):
    i = declaracion(tokens, i, 2)

def instruccion(tokens, i, instruccion = 0):
    if instruccion == 0:
        i = declaracion(tokens, i)            #Condicion
        return i
    elif instruccion == 1:                  
        i = condicion(tokens, i)      

#Proceso de condicion
def condicion(tokens, i):
    palabraIf(tokens, i)

def palabraIf(tokens, i):
    try:
        if tokens[i].type.value == 14:       #Valor definido en el lexico para if
            i += 1
            parantesisAbre(tokens, i)
        else:
            print("Sintax error: Error en el 'if' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")
    except:
        print("Sintax error: Error en el 'if' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")

def parantesisAbre(tokens, i, instruccion = 0):
    try:
        if instruccion == 0:                        #Comparacion
            if tokens[i].type.value == 44:          #Valor definido en el lexico para (
                i += 1
                i = comparacion(tokens, i)              #Revisar la comparacion
                parentesisCierra(tokens, i)
            else:
                print("Sintax error: Error en el '(' \n"
                    "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")
        if instruccion == 1:
            parentesisCierra(tokens, i)
        elif instruccion == 1:                      #Funcion
            i += 1
            parentesisCierra(tokens, i)
            
    except:
        print("Sintax error: Error en el '(' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")

def comparacion(tokens, i):
    i = operador(tokens, i)                     #Valida el operador
    if i == -1:
        print("Sintax error: Error en el operador \n"
                  "<COMPARACION> -> <OPERADOR> <OP_COMPARACION> <OPERADOR> ")
    else:
        i = opComparacion(tokens, i)
        if i == -1:
            print("Sintax error: Error en el operador de comparacion \n"
                    "<COMPARACION> -> <OPERADOR> <OP_COMPARACION> <OPERADOR> ")
        else:
            i = operador(tokens, i)
            if i == -1:
                print("Sintax error: Error en el operador de comparacion \n"
                        "<COMPARACION> -> <OPERADOR> <OP_COMPARACION> <OPERADOR> ")
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


def parentesisCierra(tokens, i):
    try:
        if tokens[i].type.value == 45:          #Valor definido en el lexico para )
            i += 1
            llaveAbre(tokens, i)              #Revisar la comparacion
        else:
            print("Sintax error: Error en el ')' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")
    except:
        print("Sintax error: Error en el ')' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")
        
def llaveAbre(tokens, i):
    try:
        if tokens[i].type.value == 42:          #Valor definido en el lexico para {
            i += 1
            i = instruccion(tokens, i)
            llaveCierra(tokens, i)
        else:
            print("Sintax error: Error en el '{' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")
    except:
        print("Sintax error: Error en el '{' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")

def llaveCierra(tokens, i):
    try:
        if tokens[i].type.value == 43:          #Valor definido en el lexico para }
            i += 1
            print("Syntax analysis completed with no errors \n Process finished with exit code 0")
            return i
        else:
            print("Sintax error: Error en el '}' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")
    except:
        print("Sintax error: Error en el '}' \n"
                  "<CONDICION> -> if ( <COMPARACION> ) { <ORDENES> } ")

#Proceso de asignacion
def asignacion(tokens, i):
    i += 1
    i = identificador(tokens, i, 1)

def simboloAsignacion(tokens, i):
    try:
        if tokens[i].type.value == 40:       #Valor definido en el lexico para =
            i += 1
            valorEntero(tokens, i)
        else:
            print("Sintax error: Error en el '=' \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;")
    except:
        print("Sintax error: Error en el '=' \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;")

def valorEntero(tokens, i):
    try:
        if tokens[i].type.value == 51:       #Valor definido en el lexico para numero entero
            i += 1
            puntoComa(tokens, i)                #Valida que haya ;
        else:
            print("Sintax error: Error en el <VALOR_ENTERO> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;")
    except:
        print("Sintax error: Error en el <VALOR_ENTERO> \n <ASIGNACION> -> <IDENTIFICADOR> = <VALOR_ENTERO> ;")

#Proceso de declaracion
def declaracion(tokens, i):        #Valida la declaracion
    i = tipo(tokens, i)
    return i

def tipo(tokens, i):
    try:
        if tokens[i].type.value == 4:           #Valor definido en el lexico para el char
            i += 1
            i = identificador(tokens, i)            #Valida que sea un identificador
            return i
        elif tokens[i].type.value == 6:         #Valor definido en el lexico para el int
            i += 1
            i = identificador(tokens, i)            #Valida que sea un identificador
            return i
        elif tokens[i].type.value == 8:         #Valor definido en el lexico para el float
            i += 1
            i = identificador(tokens, i)            #Valida que sea un identificador
            return i
        else:
            print("Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")
    except:
        print("Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")

def identificador(tokens, i, instruccion = 0):
    try:
        if tokens[i].type.value == 50:          #Valor definido en el lexico para el identificador
                if instruccion == 0:                        #Declaracion
                    i += 1
                    i = puntoComa(tokens, i)                #Valida que haya ;
                    return i
                elif instruccion == 1:                      #Asiganacion
                    i += 1
                    i = simboloAsignacion(tokens, i)
                elif instruccion == 2:                      #Funcion
                    i += 1
                    i = parantesisAbre(tokens, i, 1)
                    return i
                else:
                    print("Sintax error: Error en el identificador \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")
        else:
            print("Sintax error: Error en el identificador \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")
    except:
        print("Sintax error: Error en el identificador \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")

def puntoComa(tokens, i):
    try:
        if tokens[i].type.value == 49:       #Valor definido en el lexico para el ;
            i += 1
            return i
        else:
            print("Sintax error: Error en el ';' ")
    except:
        print("Sintax error: Error en el ';' ")