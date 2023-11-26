lineas = []

def reiniciarLineas():
    lineas.clear()

def declaraciones(var, valor):
    num = len(lineas)
    cadena = str(num) + ': ' + var + ' = ' + valor
    lineas.append(cadena)

def saltoWhile(var, var2, opCom):
    num = len(lineas)
    cadena = str(num) + ': if false ' + var + ' ' + opCom + ' ' + var2 + ' goto '
    lineas.append(cadena)
    return num
    
def asignacionArit(var, var1, var2, opArit):
    num = len(lineas)
    if var == var1 or var == var2:
        cadena = str(num) + ': t1 = ' + var1 + ' ' + opArit + ' ' + var2
        lineas.append(cadena)
        num += 1
        cadena = str(num) + ': ' + var + ' = ' + 't1'
        lineas.append(cadena)
    else:
        cadena = str(num) + ': ' + var + ' = ' + var1 + ' ' + opArit + ' ' + var2
        lineas.append(cadena)

def cerrarBucle(filas):
    num = len(lineas)
    id = filas[0]               #Linea donde se creo el if
    cadena = str(num) + ': goto ' + str(id)
    lineas.append(cadena)
    lineas[id] += str(num +1)
    
def cerrarIf(filas):
    num = len(lineas)
    id = filas[0]               #Linea donde se creo el if
    lineas[id] += str(num)

def fin():
    num = len(lineas)
    cadena = str(num) + ': '
    lineas.append(cadena)

def showLineas():
    for linea in lineas:
        print(linea)
    return lineas

