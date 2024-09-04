from lexer import lexer
from parser import parser

def main():
    with open('program.txt', 'r') as archivo:
        program = archivo.read().upper()
        tokens = lexer(program)
        response = parser(tokens)
        print(response)

if __name__ == "__main__":
    main()