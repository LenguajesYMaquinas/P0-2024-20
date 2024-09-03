from lexer import lexer
from parser import parser

def main():
    with open('program.txt', 'r') as archivo:
        program = archivo.read().upper()
        tokens = lexer(program)
        #for token in tokens:
         #   print(token.type, token.value)
        response = parser(tokens)
        print(response)

if __name__ == "__main__":
    main()