from analex import clasificar
from analex import registrar
from analex import constants
from analex import variables

def proceso_analex(token_list: list):
    for indiceLinea, line in enumerate(token_list):
        indiceToken=0
        while indiceToken<len(line):
            token = line[indiceToken]
            finalizado = False
            if token in constants.PALABRAS_RESERVADAS or token in constants.OPERADORES_ARITMETICOS:
                variables.SALIDA.append(token)
                finalizado = True
            elif clasificar.esDecimal(token) or clasificar.esHexadecimal(token): # SI ES CONSTANTE NUMERICA
                variables.SALIDA.append("[valorn]")
                registrar.num(token)
                finalizado = True
            elif clasificar.esVariable(token): # SI ES VARIABLE
                variables.SALIDA.append("[id]")
                registrar.identificador(token)
                finalizado = True
            elif clasificar.esString(token): # SI ES STRING 
                variables.SALIDA.append("[litalfnum]") 
                finalizado = True
            elif clasificar.esInicioString(token):
                stringReconstruido = token+" "
                while indiceToken+1 < len(line):
                    indiceToken+=1
                    stringReconstruido += line[indiceToken]
                    if clasificar.esString(stringReconstruido):
                        finalizado = True
                        variables.SALIDA.append("[litalfanum]")
                        registrar.string(stringReconstruido)
                        break
                    stringReconstruido+=" "

            if not finalizado:
                clasificar.imprimeError(indiceLinea, token)
                return False
            else:
                indiceToken+=1
    return True