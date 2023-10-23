def programa(tokens):
    declaracion(tokens)

def declaracion(tokens):        #Valida la declaracion
    i = 0
    tipo(tokens, i)

def tipo(tokens, i):
    try:
        if tokens[i].type.value == 4:           #Valor definido en el lexico para el char
            i += 1
            identificador(tokens, i)            #Valida que sea un identificador
        elif tokens[i].type.value == 6:         #Valor definido en el lexico para el int
            i += 1
            identificador(tokens, i)            #Valida que sea un identificador
        elif tokens[i].type.value == 8:         #Valor definido en el lexico para el float
            i += 1
            identificador(tokens, i)            #Valida que sea un identificador
        else:
            print("Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")
    except:
        print("Sintax error: Error en el tipo \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")

def identificador(tokens, i):
    try:
        if tokens[i].type.value == 50:          #Valor definido en el lexico para el identificador
            i += 1
            puntoComa(tokens, i)                #Valida que haya ;
    except:
        print("Sintax error: Error en el identificador \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")

def puntoComa(tokens, i):
    try:
        if tokens[i].type.value == 49:       #Valor definido en el lexico para el identificador
            print("Syntax analysis completed with no errors \n Process finished with exit code 0")
    except:
        print("Sintax error: Error en el ';' \n <DECLARACION> -> <TIPO> <IDENTIFICADOR> ;")
    
