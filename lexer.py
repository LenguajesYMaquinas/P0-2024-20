import ply.lex as lex

def lexer(program):
   tokens = (
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
      'SEMICOLON',
      'LPAREN',
      'RPAREN',
      'COMMA',
      'EQUALS',
      'LBRACKET',
      'RBRACKET',
      'VARIABLE',
      'NUMBER',
      'SIZE',
      'MYX',
      'MYY',
      'MYCHIPS',
      'MYBALLOONS',
      'BALLOONSHERE',
      'CHIPSHERE',
      'ROOMFORCHIPS',
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
      'EXEC',
      'NEW',
      'VAR',
      'MACRO',
      'IF',
      'THEN',
      'ELSE',
      'FI',
      'DO',
      'OD',
      'REP',
      'PER',
      'TIMES',
      'ISBLOCKED',
      'ISFACING',
      'ISZERO',
      'NOT',

      
   )

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

   def t_RPAREN(t):
      r'\)'
      return t 
   
   def t_COMMA(t):
      r','
      return t

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
   
   def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")

   lexer = lex.lex()
   lexer.input(program)

   return lexer