from analex import variables
import re
def generar_LEX(filename) -> None:
    new_filename = re.sub(".mio","",filename)

    with open(f"./{new_filename}.lex","w") as fp:
        for line in variables.SALIDA:
            fp.write(line+"\n")
        fp.close()

def generar_Factorial_Sim() -> None:
    with open("./factorial.sim","w") as fp:
        fp.write("IDS\n") # Escribe la matriz de identificadores
        for row in variables.IDS:
            fp.write(f"{row[0]} {row[1]}\n")
        
        fp.write("\nTXT\n") # Escribe la matriz de literales de texto
        for row in variables.TXT:
            fp.write(f"{row[0]} {row[1]}\n")
        
        
        fp.write("\nVAL\n") # Escribe la matriz de valores numericos
        for row in variables.VAL:
            fp.write(f"{row[0]} {row[1]}\n")  

        fp.close()