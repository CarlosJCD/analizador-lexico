import argparse
parser = argparse.ArgumentParser(description=
"""
Analizador lexico para el lenguaje "mio"
================================================
Uso:
analex -f ejemplo.mio
================================================

Genera los archivos .lex y .sim
""")
parser.add_argument("filename",metavar="filename",type=str)
args = parser.parse_args()
filename = args.filename
