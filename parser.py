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
        line = graph_file.readline()
        
    adjacency_matrix_copy = adjacency_matrix.copy()
    
    # States transitions
    current_state = 'INITIAL'
    current_state_index = adjacency_matrix_order_inverted[current_state]
    final_states = ["INITIAL", "RBRACKET", "NUMBER", "VARIABLE", "SIZE", "MYX", "MYY", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "ROOMFORCHIPS"]
    
    # Verifications
    brackets_stack = 0
    parenthesis_stack = 0
    
    variables = []
    macro_parameters_quantity = {}
    
    macro_pending_parameters = False
    macro_recieving_parameters = False
    variables_in_macro = []
    macro_pending_block =  False
    macro_in_block = False
    
    current_macro_in_definition_name = None
    
    macro_calling_pending_parameters = False
    macro_calling_parameters_received = 0
    macro_calling_name = None
    
    in_variable_definition = False
    pending_equals_in_variable_definition = pending_assign_value = value_assigned = False
    
    in_macro_definition = pending_lparen_in_macro_definition = False
    pending_rparen_in_macro_definition = False
    pending_variable_in_macro_definition = False
    pending_comma_from_variable_in_macro_definition = False
    pending_lbracket_in_macro_definition = False
    
    in_jumpforward = in_jumpforward_pending_rparen = in_jumpforward_pending_value = False
    
    goto_parameters_received = 0
    in_goto_pending_values = in_goto =  False
    
    in_assignment_pending_value = in_assignment_pending_equals = in_assignment = False
    
    in_turntomy_pending_rparen = in_turntomy_pending_argument = in_turntomy = False
    in_turntothe_pending_rparen = in_turntothe_pending_argument = in_turntothe = False
    
    in_moves_pending_rparen = in_moves_pending_arguments = in_moves = False
    
    in_safeexe_pending_command_name = in_safeexe = False
    
    in_isblocked_pending_rparen = in_isblocked_pending_argument = in_isblocked = False
    
    in_isfacing_pending_rparen = in_isfacing_pending_argument = in_isfacing = False

    in_not = in_not_pending_condition = False
    
    if_stack = then_stack = do_stack = rep_stack = 0
    
    in_if_pending_then = in_if_pending_rparen = in_if_pending_condition = in_if = False
    
    in_do_pending_od = in_do_pending_block = in_do_pending_rparen = in_do_pending_condition = in_do = False
    
    for token_object in tokens:
        token = token_object.type
        token_value = token_object.value
        print(if_stack)
        print("{}: {}".format(token, token_object.value))
        
        # Closing brackets verification
        if token == "LBRACKET":
            brackets_stack += 1
        elif token == "RBRACKET":
            brackets_stack -= 1
            
        # Closing parenthesis verification
        if token == "LPAREN":
            parenthesis_stack += 1
        elif token == "RPAREN":
            parenthesis_stack -= 1
            
        # Closing if verification
        if token == "IF":
            if_stack += 1
        elif token == "FI":
            if_stack -= 1
            
        # Closing then verification
        if token == "THEN":
            then_stack += 1
        elif token == "ELSE":
            then_stack -= 1
            
        #Closing do verification
        if token == "DO":
            do_stack += 1
        elif token == "OD":
            do_stack -= 1
            
        # Closing rep verification
        if token == "REP":
            rep_stack += 1
        elif token == "TIMES":
            rep_stack += 1
        elif token == "PER":
            rep_stack -= 2
            
        # Not duplicated variables definition verification
        if current_state == "VAR" and token == "VARIABLE":
            if token_value not in variables:
                variables.append(token_value)
            else:
                print('a')
                return False
        
        # Use of variables already declareds verification
        if current_state == "EQUALS" and token == "VARIABLE" and token_value not in variables and not macro_in_block:
            print('b')
            return False
        
        # Not duplicated macros definition verification
        if current_state == "MACRO" and token == "VARIABLE":
            if token_value not in macro_parameters_quantity:
                macro_parameters_quantity[token_value] = 0
                current_macro_in_definition_name = token_value
            else:
                print('c')
                return False
        
        # Use in MACROs of parameters and variables already declared verification
        if token == "MACRO":
            macro_pending_block = True
            macro_pending_parameters = True
        if token == "LPAREN" and macro_pending_parameters:
            macro_recieving_parameters = True
        if token == "VARIABLE" and macro_recieving_parameters:
            variables_in_macro.append(token_value)
            macro_parameters_quantity[current_macro_in_definition_name] += 1
        if token == "RPAREN" and macro_recieving_parameters:
            macro_recieving_parameters = False
            macro_pending_parameters = False
        if token == "LBRACKET" and macro_pending_block:
            macro_in_block = True
        if token == "RBRACKET" and macro_in_block:
            macro_in_block = False
            macro_pending_block = False
            variables_in_macro = []
            print(macro_parameters_quantity)
            current_macro_in_definition_name = None
        if token == "VARIABLE" and macro_in_block:
            if token_value not in variables_in_macro and token_value not in variables and token_value not in macro_parameters_quantity:
                print('d')
                print(current_state, token_value)
                return False
            
        # Allowing using macros in blocks
        if current_state in ['LBRACKET', 'SEMICOLON'] and token == 'VARIABLE':
            if token_value not in variables_in_macro and token_value not in variables and token_value not in macro_parameters_quantity:
                print('e')
                return False 
            elif token_value in macro_parameters_quantity:
                macro_calling_pending_parameters = True
                macro_calling_name = token_value
        if current_state in ['LPAREN', 'COMMA'] and token == "VARIABLE" and macro_calling_pending_parameters:
            macro_calling_parameters_received += 1
        if current_state == 'VARIABLE' and token == 'RPAREN' and macro_calling_pending_parameters:
            if macro_calling_parameters_received!= macro_parameters_quantity[macro_calling_name]:
                print('f')
                return False
            macro_calling_pending_parameters = False
            macro_calling_parameters_received = 0
            macro_calling_name = None
            
        # EXECs and definitions only in level 0
        if current_state in ['EXEC'] and brackets_stack > 1:
            print(current_state, token_value)
            print('z')
            return False
        # EXECs and definitions only in level 0
        if current_state in ['NEW'] and brackets_stack > 0:
            print(current_state, token_value)
            print('i')
            return False
        
        # Semicolons only in levels not equals to level 0
        if token == 'SEMICOLON' and brackets_stack == 0:
            print(current_state, token_value)
            print('j')
            return False
        
        # Limitations of succesors of VARIABLE token when declaring a variable
        if current_state == 'VAR' and token == 'VARIABLE':
            #print("in_variable_definition")
            in_variable_definition = pending_equals_in_variable_definition = True
        elif in_variable_definition and pending_equals_in_variable_definition:
            if token == 'EQUALS':
                pending_assign_value = True
                pending_equals_in_variable_definition = False
            else:
                print('w')
                return False
        elif current_state == "EQUALS" and in_variable_definition and pending_assign_value:
            if token in ["NUMBER", "VARIABLE", "SIZE", "MYX", "MYY", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "ROOMFORCHIPS"]:
                pending_equals_in_variable_definition = False
                pending_assign_value = False
                value_assigned = True
            else:
                print('x')
                return False
        elif in_variable_definition and value_assigned and current_state in ["NUMBER", "VARIABLE", "SIZE", "MYX", "MYY", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "ROOMFORCHIPS"]:
            if token not in ['NEW', 'EXEC']:
                #print(current_state, token_value)
                print('..')
                return False
            else:
                #print("out of in_variable_definition")
                value_assigned = False
                in_variable_definition = False
        
        # Validation of macro definition sequence
        if current_state == 'MACRO' and token == 'VARIABLE':
            in_macro_definition = pending_lparen_in_macro_definition = True
        elif pending_lbracket_in_macro_definition:
            if token == 'LBRACKET':
                pending_lbracket_in_macro_definition = False
                in_macro_definition = pending_lparen_in_macro_definition = False
                pending_rparen_in_macro_definition = False
                pending_variable_in_macro_definition = False
                pending_comma_from_variable_in_macro_definition = False
            else:
                print('h')
                return False
        elif in_macro_definition and pending_lparen_in_macro_definition:
            if token == 'LPAREN':
                pending_lparen_in_macro_definition = False
                pending_rparen_in_macro_definition = True
                pending_variable_in_macro_definition = True
            else:
                print('xl')
                return False
        elif in_macro_definition and (pending_rparen_in_macro_definition or pending_variable_in_macro_definition):
            if pending_variable_in_macro_definition and token == 'VARIABLE':
                pending_comma_from_variable_in_macro_definition = True
            elif pending_comma_from_variable_in_macro_definition and token == 'COMMA':
                pending_comma_from_variable_in_macro_definition = False
                pending_variable_in_macro_definition = True
            elif token == 'RPAREN':
                pending_rparen_in_macro_definition = False
                pending_variable_in_macro_definition = False
                pending_lbracket_in_macro_definition = True
            else:
                print('k')
                return False
            
        
        # 'JUMPFORWARD', 'WALK', 'JUMP', 'DROP', 'PICK', 'GRAB', 'LETGO', 'POP', ISZERO sequence  and argument verification
        if current_state in ['JUMPFORWARD', 'WALK', 'JUMP', 'DROP', 'PICK', 'GRAB', 'LETGO', 'POP', 'ISZERO']:
            in_jumpforward = True
            in_jumpforward_pending_value = True
        elif in_jumpforward and current_state == 'LPAREN' and in_jumpforward_pending_value:
            if token in ["NUMBER", "VARIABLE", "SIZE", "MYX", "MYY", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "ROOMFORCHIPS"]:
                in_jumpforward_pending_value = False
                in_jumpforward_pending_rparen = True
            else:
                print('l')
                return False
            if token == 'VARIABLE' and (token_value not in variables and token_value not in variables_in_macro):
                print('r')
                return False
        elif in_jumpforward and in_jumpforward_pending_rparen and current_state in ["NUMBER", "VARIABLE", "SIZE", "MYX", "MYY", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "ROOMFORCHIPS"]:
            if token == "RPAREN":
                in_jumpforward = False
                in_jumpforward_pending_rparen = False
            else:
                print('m')
                return False
            
        # Goto sequence and correct arguments verification
        if current_state == 'GOTO':
            in_goto = True
            in_goto_pending_values = True
        elif in_goto and in_goto_pending_values and current_state in ['LPAREN', 'COMMA'] and token in ["NUMBER", "VARIABLE", "SIZE", "MYX", "MYY", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "ROOMFORCHIPS"]:
            goto_parameters_received += 1
            if token == 'VARIABLE' and token_value not in variables and not macro_in_block:
                print('dfdf')
                return False
        elif in_goto and in_goto_pending_values and current_state in ["NUMBER", "VARIABLE", "SIZE", "MYX", "MYY", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "ROOMFORCHIPS"]:
            if token == "RPAREN":
                in_goto = False
                in_goto_pending_values = False
                if goto_parameters_received != 2:
                    print('n')
                    return False
                goto_parameters_received = 0
            if token not in ["COMMA", "RPAREN"]:
                return False
            
        # Assignment sequence and correct value verification
        if current_state in ["LBRACKET", "SEMICOLON"] and token == 'VARIABLE':
            if token_value not in variables and token_value not in variables_in_macro and token_value not in macro_parameters_quantity:
                print(token_value)
                print('o')
                return False
            elif token_value in variables or token_value in variables_in_macro:
                in_assignment = True
                in_assignment_pending_equals = True
        elif in_assignment and in_assignment_pending_equals:
            if token == 'EQUALS':
                in_assignment_pending_equals = False
                in_assignment_pending_value = True
            else:
                print('p')
                return False
        elif in_assignment and in_assignment_pending_value:
            if token in ["NUMBER", "VARIABLE", "SIZE", "MYX", "MYY", "MYCHIPS", "MYBALLOONS", "BALLOONSHERE", "CHIPSHERE", "ROOMFORCHIPS"]:
                in_assignment_pending_value = False
            else:
                print('q')
                return False
            if token == 'VARIABLE' and (token_value not in variables and token_value not in variables_in_macro):
                print('r')
                return False
            
        # TURNTOMY sequence and correct argument verification
        if current_state == 'TURNTOMY':
            in_turntomy = True
            in_turntomy_pending_argument = True
        elif in_turntomy and in_turntomy_pending_argument and current_state == 'LPAREN':
            if token in ['LEFT', 'RIGHT', 'BACK']:
                in_turntomy_pending_argument = False
                in_turntomy_pending_rparen = True
            else:
                print('s')
                return False
        elif in_turntomy and in_turntomy_pending_rparen:
            if token == 'RPAREN':
                in_turntomy = False
                in_turntomy_pending_rparen = False
            else:
                print('t')
                return False
            
        # TURNTOTHE sequence and correct argument verification
        if current_state == 'TURNTOTHE':
            in_turntothe = True
            in_turntothe_pending_argument = True
        elif in_turntothe and in_turntothe_pending_argument and current_state == 'LPAREN':
            if token in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
                in_turntothe_pending_argument = False
                in_turntothe_pending_rparen = True
            else:
                print('s')
                return False
        elif in_turntothe and in_turntothe_pending_rparen:
            if token == 'RPAREN':
                in_turntothe = False
                in_turntothe_pending_rparen = False
            else:
                print('t')
                return False
            
        # MOVES sequence and correct arguments verification
        if current_state == 'MOVES' and token == 'LPAREN':
            in_moves = True
            in_moves_pending_arguments = True
        elif in_moves and in_moves_pending_arguments and current_state in ['LPAREN', 'COMMA']:
            if token in ['FORWARD', 'RIGHT', 'LEFT', 'BACKWARDS']:
                in_moves_pending_rparen = True
            else:
                print('u')
                return False
        elif in_moves and in_moves_pending_rparen:
            if token == 'RPAREN':
                in_moves = False
                in_moves_pending_arguments = False
                in_moves_pending_rparen = False
            elif token == 'COMMA':
                in_moves_pending_arguments = True
            else:
                print('v')
                return False
        
        
            
        # SAFEEXE sequence and correct arguments verification
        if current_state == 'SAFEEXE' and token == 'LPAREN':
            in_safeexe = True
            in_safeexe_pending_command_name = True
        elif in_safeexe and in_safeexe_pending_command_name and current_state == 'LPAREN':
            if token in ['WALK', 'JUMP', 'DROP', 'PICK', 'GRAB', 'LETGO', 'POP']:
                in_safeexe_pending_command_name = False
                in_safeexe = False
            else:
                print('w')
                return False
            
        # isblocked sequence and correct arguments verification
        if current_state == 'ISBLOCKED' and token == 'LPAREN':
            in_isblocked = True
            in_isblocked_pending_argument = True
        elif in_isblocked and in_isblocked_pending_argument and current_state == 'LPAREN':
            if token in ['LEFT', 'RIGHT', 'FRONT', 'BACK']:
                in_isblocked_pending_argument = False
                in_isblocked_pending_rparen = True
            else:
                print('w')
                return False
        elif in_isblocked and in_isblocked_pending_rparen and current_state in ['LEFT', 'RIGHT', 'FRONT', 'BACK']:
            if token == 'RPAREN':
                in_isblocked = in_isblocked_pending_rparen = False
            else:
                print('w')
                return False
            
        # isfacing sequence and correct arguments verification
        if current_state == 'ISFACING' and token == 'LPAREN':
            in_isfacing = True
            in_isfacing_pending_argument = True
        elif in_isfacing and in_isfacing_pending_argument and current_state == 'LPAREN':
            if token in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
                in_isfacing_pending_argument = False
                in_isfacing_pending_rparen = True
            else:
                print('w')
                return False
        elif in_isfacing and in_isfacing_pending_rparen and current_state in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
            if token == 'RPAREN':
                in_isfacing = in_isfacing_pending_rparen = False
            else:
                print('w')
                return False
            
        # not sequence and correct arguments verification
        if current_state == 'NOT' and token == 'LPAREN':
            in_not = True
            in_not_pending_condition = True
        elif in_not and in_not_pending_condition and current_state == 'LPAREN':
            if token in ['ISBLOCKED', 'ISFACING', 'ISZERO', 'NOT']:
                in_not = False
                in_not_pending_condition = False
            else:
                print('w')
                return False
            
        # if sequence and correct arguments verification
        if current_state == 'IF' and token == 'LPAREN':
            in_if = True
            in_if_pending_condition = True
        elif in_if and in_if_pending_condition and current_state == 'LPAREN':
            if token in ['ISBLOCKED', 'ISFACING', 'ISZERO', 'NOT']:
                in_if_pending_condition = False
                in_if_pending_rparen = True
            else:
                print('w')
                return False
        elif in_if and in_if_pending_rparen and current_state == 'RPAREN':
            if token == 'RPAREN':
                in_if_pending_rparen = False
                in_if_pending_then = True
            else:
                print('w')
                return False
        elif in_if and in_if_pending_then and current_state == 'RPAREN':
            if token == 'THEN':
                in_if_pending_then = False
                rbracket_index = adjacency_matrix_order_inverted['RBRACKET']
                else_index = adjacency_matrix_order_inverted['ELSE']
                adjacency_matrix[rbracket_index] = [False] * len(adjacency_matrix)
                adjacency_matrix[rbracket_index][else_index] = True
            elif token == 'RPAREN':
                pass
            else:
                print('w')
                return False
        elif in_if and current_state == 'ELSE':
            rbracket_index = adjacency_matrix_order_inverted['RBRACKET']
            fi_index = adjacency_matrix_order_inverted['FI']
            adjacency_matrix[rbracket_index] = [False] * len(adjacency_matrix)
            adjacency_matrix[rbracket_index][fi_index] = True
        elif in_if and current_state == 'FI':
            adjacency_matrix = adjacency_matrix_copy.copy()
            in_if = False
            
        # do sequence and correct arguments verification
        if current_state == 'DO' and token == 'LPAREN':
            in_do = True
            in_do_pending_condition = True
        elif in_do and in_do_pending_condition and current_state == 'LPAREN':
            if token in ['ISBLOCKED', 'ISFACING', 'ISZERO', 'NOT']:
                in_do_pending_condition = False
                in_do_pending_rparen = True
            else:
                print('w')
                return False
        elif in_do and in_do_pending_rparen and current_state == 'RPAREN':
            if token == 'RPAREN':
                in_do_pending_rparen = False
                in_do_pending_block = True
            else:
                print('w')
                return False
        elif in_do and in_do_pending_block and current_state == 'RPAREN':
            if token == 'LBRACKET':
                in_do_pending_block = False
                in_do_pending_od = True
            elif token == 'RPAREN':
                pass
            else:
                print('w')
                return False
        elif in_do and in_do_pending_od and current_state == 'RBRACKET':
            if token == 'OD':
                in_do_pending_od = False
                in_do = False
            else:
                print('w')
                return False
        
        
        # States transition
        token_index = adjacency_matrix_order_inverted[token]
        if adjacency_matrix[current_state_index][token_index]:
            current_state = token
            current_state_index = adjacency_matrix_order_inverted[current_state]
        else:
            print(current_state, token_value)
            print('g')          
            return False
    
    if current_state not in final_states or brackets_stack != 0 or parenthesis_stack != 0 or if_stack != 0 or then_stack != 0 or do_stack != 0 or rep_stack != 0:
        print('u')
        print(current_state)
        print(brackets_stack)
        print(parenthesis_stack)
        print(if_stack)
        print(then_stack)
        print(do_stack)
        print(rep_stack)
        return False

    return True