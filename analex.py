import analex
import analex.cli_parser as c_parser
import sys
import os

def main():
    
    analex.run(c_parser.filename)

if __name__=="__main__":
    main()