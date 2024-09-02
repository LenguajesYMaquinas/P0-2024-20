"""
<PROGRAM>: (<EXECBLOCK> | <DEFINITION>)*

<EXECBLOCK>: <EXEC> <BLOCK>

<BLOCK>: <LBRACKET> <INSTRUCTION>+ <RBRACKET>

<INSTRUCTION>: (<COMMAND> | <CONTROLSTRUCTURE>) <SEMICOLON>

<DEFINITION>: <VARIABLEDEFINITION> | <MACRODEFINITION>

<VARIABLEDEFINITION>: <NEW> <VAR> <VARIABLE> <EQUALS> <VALUE>

<MACRODEFINITION>: <NEW> <MACRO> <VARIABLE> <LPAREN> (<VARIABLE>* | (<VARIABLE> <COMMA>)+ <VARIABLE>) <RPAREN> <BLOCK>

<COMMAND>: 
    <MOVEFORWARD> |
    <TURNRIGHT> |
    <DROPCHIP> |
    <PLACEBALLON> |
    <POPBALLON> |
    <JUMPFORWARD> |
    <GOTO> |
    <ASSIGNMENT> |
    <MACROINVOCATION> |
    <TURNTOMY> |
    <TURNTOTHE> |
    <WALK> |
    <JUMP> |
    <DROP> |
    <PICK> |
    <GRAB> |
    <LETGO> |
    <POP> |
    <MOVES> |
    <NOP> |
    <SAFEEXE>
    
<CONTROLSTRUCTURE>: <IF> | <DO> | <REP>

<CONDITION>: <ISBLOCKED> | <ISFACING> | <ZERO> <NOT>
    
<ASSIGNMENT>: <VARIABLE> <EQUALS> <VALUE>

<MACROINVOCATION>: <VARIABLE> <LPAREN> (<VARIABLE>* | (<VARIABLE> <COMMA>)+ <VARIABLE>) <RPAREN>

<VALUE>: 
    <VARIABLE> |
    <NUMBER> |
    <SIZE> |
    <MYX> |
    <MYY> |
    <MYCHIPS> |
    <MYBALLOONS> |
    <BALLOONSHERE> |
    <CHIPSHERE> |
    <ROOMFORCHIPS>
"""
def parser(tokens):
    adjacency_matrix_order = {
        0: 'MOVEFORWARD',
        1: 'TURNRIGHT',
        2: 'DROPCHIP',
        3: 'PLACEBALLON',
        4: 'POPBALLON',
        5: 'JUMPFORWARD',
        6: 'GOTO',
        7: 'TURNTOMY',
        8: 'TURNTOTHE',
        9: 'WALK',
        10: 'JUMP',
        11: 'DROP',
        12: 'PICK',
        13: 'GRAB',
        14: 'LETGO',
        15: 'POP',
        16: 'MOVES',
        17: 'NOP',
        18: 'SAFEEXE',
        19: 'SEMICOLON',
        20: 'LPAREN',
        21: 'RPAREN',
        22: 'COMMA',
        23: 'EQUALS',
        24: 'LBRACKET',
        25: 'RBRACKET',
        26: 'VARIABLE',
        27: 'NUMBER',
        28: 'SIZE',
        29: 'MYX',
        30: 'MYY',
        31: 'MYCHIPS',
        32: 'MYBALLOONS',
        33: 'BALLOONSHERE',
        34: 'CHIPSHERE',
        35: 'ROOMFORCHIPS',
        36: 'LEFT',
        37: 'RIGHT',
        38: 'BACK',
        39: 'NORTH',
        40: 'SOUTH',
        41: 'EAST',
        42: 'WEST',
        43: 'FORWARD',
        44: 'BACKWARDS',
        45: 'FRONT',
        46: 'EXEC',
        47: 'NEW',
        48: 'VAR',
        49: 'MACRO',
        50: 'IF',
        51: 'THEN',
        52: 'ELSE',
        53: 'FI',
        54: 'DO',
        55: 'OD',
        56: 'REP',
        57: 'PER',
        58: 'TIMES',
        59: 'ISBLOCKED',
        60: 'ISFACING',
        61: 'ISZERO',
        62: 'NOT',
        63: 'INITIAL'
    }
    adjacency_matrix_order_inverted = {
        adjacency_matrix_order[i]: i for i in range(len(adjacency_matrix_order))
    }
    adjacency_matrix = [[False for _ in range(len(adjacency_matrix_order))] for _ in range(len(adjacency_matrix_order))]
    

    graph_file = open('graph.txt', 'r')
    line = graph_file.readline()
    while line:
        if line != '...\n':
            line = line.replace('\n', '').split('->')
            index_initial_node = adjacency_matrix_order_inverted[line[0]]
            index_final_node = adjacency_matrix_order_inverted[line[1]]
            adjacency_matrix[index_initial_node][index_final_node] = True
            adjacency_matrix[index_final_node][index_initial_node] = True
        line = graph_file.readline()
        
    current_state = 'INITIAL'
    current_state_index = adjacency_matrix_order_inverted[current_state]
    for token_object in tokens:
        token = token_object.type
        token_index = adjacency_matrix_order_inverted[token]
        if adjacency_matrix[current_state_index][token_index]:
            current_state = token
            current_state_index = adjacency_matrix_order_inverted[current_state]
        else:
            print(token_object, current_state, token)
            return False
        
    return True