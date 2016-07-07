#Created by: Juan Perciante
# July 2016

#When a new function is defined, it must be added in the following list
listaFuncionesExistentes = ["suma", "producto", "Tuple"]


def construirEnBaseAFuncion(funcionId, listaAtributosParaFuncion):
    if(listaFuncionesExistentes.__contains__(funcionId)):
        #Magic to call functions - globals
        retornoDeFuncion = globals()[funcionId](listaAtributosParaFuncion)
        return retornoDeFuncion
    else:
        return "FunctionID doesn't exist"


def suma(listaValores):
    if(len(listaValores) >=1):
        valorFinal = 0
        for valor in listaValores:
            valorFinal += valor
        return valorFinal

def producto(listaValores):
    if ( (len(listaValores)) == 1):
        valorFinal = listaValores[0]
        return valorFinal
    if( (len(listaValores) ) >1):
        valorFinal = listaValores[0]
        for i in range(1, len(listaValores)):
            valorFinal = valorFinal * listaValores[i]
        return valorFinal

def Tuple(listaValores):
    return tuple(listaValores)


