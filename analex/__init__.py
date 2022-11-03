from analex import parse
from analex import proceso
from analex import output

def run(filename: str):
    list_ = parse.tokenization(filename)
    if list_: 
        if proceso.proceso_analex(list_):
            output.generar_LEX(filename)
            output.generar_Factorial_Sim()