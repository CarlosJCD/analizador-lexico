from analex import constants

def esDecimal(token):
    return token.isdigit()

def esHexadecimal(token):
    if len(token) <= 2:
        return False
    if token[0:2] == "0x":
        for char in token[2:]:
            if (char not in constants.LETRAS) and (char not in constants.DIGITOS):
                return False
        return True

def esVariable(token):
    if len(token) > 16 or token[0].isdigit():
        return False
    return token.isalnum()

def esString(token):
    if token[0] == r'"' and token[-1] == r'"':
        count = 0
        for char in token:
            if char == '"':
                count += 1
        if count != 2:
            return False
        else:
            return True
    return False

def esInicioString(token):
    sub = '"'
    if token[0] != '"' or sub in token[1:]:
        return False
    else:
        return True

def esFinalString(token):
    sub = '"'
    if token[-1] != sub or sub in token[:-1]:
        return False
    return True

def error(indiceLinea, token):
    print(f"Error en la linea {indiceLinea}: {token}")


