import ply.lex as lex

# Lista de nombres de tokens
tokens = (
   
    # Commnads
    'MOVEFORWARD',
    'TURNRIGHT',
    'DROPCHIP',
    'PLACEBALLON',
    'POPBALLON',
    'JUMPFORWARD',
    'GOTO',
    'TURNTOMY',
    'TURNTOTHE',
    'WALK',
    'JUMP',
    'DROP',
    'PICK',
    'GRAB',
    'LETGO',
    'POP',
    'MOVES',
    'NOP',
    'SAFEEXE',
    
    # Symbols
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'EQUALS',
    'LBRACKET',
    'RBRACKET',
    
    # Variables and numbers
    'VARIABLE',
    'NUMBER',
    
    # Values
    'SIZE',
    'MYX',
    'MYY',
    'MYCHIPS',
    'MYBALLOONS',
    'BALLOONSHERE',
    'CHIPSHERE',
    'ROOMFORCHIPS',
    
    # Directions
    'LEFT',
    'RIGHT',
    'BACK',
    'NORTH',
    'SOUTH',
    'EAST',
    'WEST',
    'FORWARD',
    'BACKWARDS',
    'FRONT',
    
    # Definitions
    'EXEC',
    'NEW',
    'VAR',
    'MACRO',
    
    # Control structures
    'IF',
    'THEN',
    'ELSE',
    'FI',
    'DO',
    'OD',
    'REP',
    'PER',
    'TIMES',
    
    # Conditions
    'ISBLOCKED',
    'ISFACING',
    'ISZERO',
    'NOT',

    
)

# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = ' \t\n'

def t_MOVEFORWARD(t):
   r'\bM\b'
   return t

def t_TURNRIGHT(t):
   r'\bR\b'
   return t

def t_DROPCHIP(t):
   r'\bC\b'
   return t

def t_PLACEBALLON(t):
   r'\bB\b'
   return t

def t_POPBALLON(t):
   r'\bP\b'
   return t

def t_JUMPFORWARD(t):
   r'\bJ\b'
   return t

def t_GOTO(t):
   r'\bG\b'
   return t

def t_TURNTOMY(t):
   r'TURNTOMY'
   return t

def t_TURNTOTHE(t):
   r'TURNTOTHE'
   return t

def t_WALK(t):
   r'WALK'
   return t

def t_JUMP(t):
   r'JUMP'
   return t

def t_DROP(t):
   r'DROP'
   return t

def t_PICK(t):
   r'PICK'
   return t

def t_GRAB(t):
   r'GRAB'
   return t

def t_LETGO(t):
   r'LETGO'
   return t

def t_POP(t):
   r'POP'
   return t

def t_MOVES(t):
   r'MOVES'
   return t

def t_NOP(t):
   r'NOP'
   return t

def t_SAFEEXE(t):
   r'SAFEEXE'
   return t

def t_SEMICOLON(t):
    r';'
    return t

def t_LPAREN(t):
    r'\('
    return t

# Definir la expresión regular para RPAREN (paréntesis derecho)
def t_RPAREN(t):
    r'\)'
    return t 
 
# Definir la expresión regular para COMMA (coma)
def t_COMMA(t):
    r','
    return t

# Definir la expresión regular para EQUALS (=)
def t_EQUALS(t):
    r'='
    return t
 
def t_LBRACKET(t):
    r'{'
    return t
 
def t_RBRACKET(t):
    r'}'
    return t
 
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SIZE(t):
   r'SIZE'
   return t

def t_MYX(t):
   r'MYX'
   return t

def t_MYY(t):
   r'MYY'
   return t

def t_MYCHIPS(t):
   r'MYCHIPS'
   return t

def t_MYBALLOONS(t):
   r'MYBALLOONS'
   return t

def t_BALLOONSHERE(t):
   r'BALLOONSHERE'
   return t

def t_CHIPSHERE(t):
   r'CHIPSHERE'
   return t

def t_ROOMFORCHIPS(t):
   r'ROOMFORCHIPS'
   return t

def t_LEFT(t):
   r'LEFT'
   return t

def t_RIGHT(t):
   r'RIGHT'
   return t

def t_BACK(t):
   r'\bBACK\b'
   return t

def t_NORTH(t):
   r'NORTH'
   return t

def t_SOUTH(t):
   r'SOUTH'
   return t

def t_EAST(t):
   r'EAST'
   return t

def t_WEST(t):
   r'WEST'
   return t

def t_FORWARD(t):
   r'FORWARD'
   return t

def t_BACKWARDS(t):
   r'BACKWARDS'
   return t

def t_FRONT(t):
   r'FRONT'
   return t

def t_EXEC(t):
   r'EXEC'
   return t

def t_NEW(t):
   r'NEW'
   return t

def t_VAR(t):
   r'VAR'
   return t

def t_MACRO(t):
   r'MACRO'
   return t

def t_IF(t):
   r'IF'
   return t

def t_THEN(t):
   r'THEN'
   return t

def t_ELSE(t):
   r'ELSE'
   return t

def t_FI(t):
   r'FI'
   return t

def t_DO(t):
   r'DO'
   return t

def t_OD(t):
   r'OD'
   return t

def t_REP(t):
   r'REP'
   return t

def t_PER(t):
   r'PER'
   return t

def t_TIMES(t):
   r'TIMES'
   return t

def t_ISBLOCKED(t):
   r'ISBLOCKED\?'
   return t

def t_ISFACING(t):
   r'ISFACING\?'
   return t

def t_ISZERO(t):
   r'ZERO\?'
   return t

def t_NOT(t):
   r'NOT'
   return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Manejar errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)


# Construir el lexer
lexer = lex.lex()

# Probar el lexer
data = '''

   NEW VAR x = 23
   NEW VAR y = x
   
   NEW MACRO caminar(parametro_1, parametro_2){
      y = 3
   }
   
   EXEC{
      M;
      R;
      C;
      B;
      P;
      J(12);
      G(x, y);
      
      caminar(x, y);
      
      turnToMy(left);
      turnToMy(right);
      turnToMy(back);
      turnToThe(north);
      turnToThe(south);
      turnToThe(east);
      turnToThe(west);
      walk(88);
      jump(88);
      drop(88);
      pick(88);
      grab(88);
      letGo(88);
      pop(88);
      moves(forward, right, left, backwards);
      nop;
      safeExe(walk(88));
      safeExe(jump(88));
      safeExe(drop(88));
      safeExe(pick(88));
      safeExe(grab(88));
      safeExe(letGo(88));
      safeExe(pop(88));
      
      pop(size);
      pop(myX);
      pop(myY);
      pop(myChips);
      pop(myBalloons);
      pop(balloonsHere);
      pop(chipsHere);
      pop(roomForChips);
      
      if (zero?(3)) then{
         pop(88);
      } else{
         pop(89);
      } fi;
      
      do (zero?(3)){
         pop(88);
      } od;
      
      do (isFacing?(north)){
         pop(88);
      } od;
      do (isFacing?(south)){
         pop(88);
      } od;
      do (isFacing?(east)){
         pop(88);
      } od;
      do (isFacing?(west)){
         pop(88);
      } od;
      
      do (isBlocked?(left)){
         pop(88);
      } od;
      do (isBlocked?(right)){
         pop(88);
      } od;
      do (isBlocked?(front)){
         pop(88);
      } od;
      do (isBlocked?(back)){
         pop(88);
      } od;
      
      do (not(isBlocked?(back))){
         pop(88);
      } od;
      
      rep 3 times{
         pop(88);
      } per;
      
'''

# Pasa la entrada al lexer
lexer.input(data.upper())

# Itera sobre los tokens generados
for tok in lexer:
    print(tok.type)  # Imprimir tipo y valor del token
