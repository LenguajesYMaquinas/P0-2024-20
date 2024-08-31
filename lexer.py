import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'COMMAND',
)

# Definir la expresión regular para el token COMMAND
def t_COMMAND(t):
    r'(M;|R;|C;|B;|c;|b;|P;|J\([a-zA-Z_][a-zA-Z_0-9]*\);|G\([a-zA-Z_][a-zA-Z_0-9]*,[a-zA-Z_][a-zA-Z_0-9]*\);)'
    
    # Remover el punto y coma del valor del token antes de procesarlo
    t.value = t.value[:-1]

    # Identificar la instrucción específica
    if t.value == 'M':
        t.value = 'MOVE_FORWARD'
    elif t.value == 'R':
        t.value = 'TURN_RIGHT'
    elif t.value == 'C':
        t.value = 'DROP_CHIP'
    elif t.value == 'B':
        t.value = 'PLACE_BALLOON'
    elif t.value == 'P':
        t.value = 'POP_BALLOON'
    elif t.value.startswith('J('):
        arg = t.value[2:-1]  # Extrae el argumento dentro de J()
        t.value = f'JUMP {arg}'
    elif t.value.startswith('G('):
        args = t.value[2:-1].split(',')
        t.value = f'GOTO ({args[0]}, {args[1]})'  # Extrae y asigna los valores de x e y
    
    return t

# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = ' \t\n'

# Manejar errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Probar el lexer
data = 'M; R; C; B; \n \t \n P; J(variable); G(numero_1,numero_2);'

# Pasa la entrada al lexer
lexer.input(data)

# Itera sobre los tokens generados
for tok in lexer:
    print(tok)  # Imprimir solo el valor del token
