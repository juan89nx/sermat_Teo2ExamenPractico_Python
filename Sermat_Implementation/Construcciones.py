idFuncion = ""
listaAtributos = []
listaFuncionesExistentes = ["suma", "producto", "Tuple"]



def construirEnBaseAFuncion(funcionId, listaAtributosParaFuncion):
    if(listaFuncionesExistentes.__contains__(funcionId)):
        #print "FuncionID existente"
        #Magia para crear funcion - globals
        retornoDeFuncion = globals()[funcionId](listaAtributosParaFuncion)
        #print "La Funcion Retorna: "+str(retornoDeFuncion)
        return retornoDeFuncion
    else:
        return "FuncionID no existe"


def suma(listaValores):
    valorFinal = 0
    for valor in listaValores:
        valorFinal += valor
    return valorFinal

def producto(listaValores):
    if ( (len(listaValores)) == 1):
        valorFinal = listaValores[0]
    if( (len(listaValores) ) >1):
        valorFinal = listaValores[0]
        for i in range(1, len(listaValores)):
            valorFinal = valorFinal * listaValores[i]
    return valorFinal

def Tuple(listaValores):
    return tuple(listaValores)

#Construcciones.construirEnBaseAFuncion("suma", [1,2,3])

