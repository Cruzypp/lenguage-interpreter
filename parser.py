import ply.yacc as yacc
from lexer import tokens, lexer

# Precedencia de operadores
precedence = (
    ('left', 'EQ', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Variable para detectar errores
p_error_detected = False

def p_program(p):
    '''program : declarations statements
               | declarations
               | statements
               | empty'''
    if not p_error_detected:
        print("sí")

# Declaraciones
def p_declarations(p):
    '''declarations : declaration declarations
                    | declaration'''
    pass

def p_declaration(p):
    '''declaration : type COLON id_list SEMICOLON
                   | type COLON id_list'''
    pass

def p_type(p):
    '''type : INT
            | FLOAT'''
    pass

def p_id_list(p):
    '''id_list : ID COMMA id_list
               | ID'''
    pass

# Lista de sentencias principal
def p_statements(p):
    '''statements : statement statements
                  | statement'''
    pass

def p_statement(p):
    '''statement : assignment SEMICOLON
                 | assignment
                 | read_stmt SEMICOLON
                 | read_stmt
                 | print_stmt SEMICOLON
                 | print_stmt
                 | while_stmt SEMICOLON
                 | while_stmt
                 | ifelse_stmt SEMICOLON
                 | ifelse_stmt'''
    pass

# Sentencias básicas
def p_assignment(p):
    '''assignment : ID ASSIGN expression'''
    pass

def p_read_stmt(p):
    '''read_stmt : READ ID'''
    pass

def p_print_stmt(p):
    '''print_stmt : PRINT expression'''
    pass

# Sentencias de control
def p_while_stmt(p):
    '''while_stmt : WHILE LPAREN logical_expr RPAREN block'''
    pass

def p_ifelse_stmt(p):
    '''ifelse_stmt : IFELSE LPAREN logical_expr RPAREN block block'''
    pass

# Bloques
def p_block(p):
    '''block : LBRACKET block_statements RBRACKET
             | LBRACKET RBRACKET'''
    pass

def p_block_statements(p):
    '''block_statements : block_statement SEMICOLON block_statements
                        | block_statement SEMICOLON
                        | block_statement block_statements
                        | block_statement'''
    pass

def p_block_statement(p):
    '''block_statement : assignment
                       | read_stmt
                       | print_stmt
                       | while_stmt
                       | ifelse_stmt'''
    pass

# Expresiones lógicas
def p_logical_expr(p):
    '''logical_expr : expression LT expression
                    | expression LE expression
                    | expression GT expression
                    | expression GE expression
                    | expression EQ expression
                    | expression'''
    pass

# Expresiones aritméticas
def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    pass

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    pass

def p_factor(p):
    '''factor : LPAREN expression RPAREN
              | ID
              | NUMINT
              | NUMFLOAT'''
    pass

# Producción vacía
def p_empty(p):
    'empty :'
    pass

<<<<<<< HEAD
def p_error(p):
    global p_error_detected
    p_error_detected = True
    if p:
        print(f"Error de sintaxis en:'{p.value}' Tipo: {p.type} (línea {p.lineno})")
        # Mostrar contexto
        print(f"Posición: {p.lexpos}")
    else:
        print("Error de sintaxis")


parser = yacc.yacc(debug=False)
=======
class TokenIterator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.lineno = 1
>>>>>>> 884ab77c4d307d3d670e3cd234c4218fd1d89a0c

def parse(data):
    lexer.input(data)
    result = parser.parse(data, lexer=lexer)
    return not p_error_detected

# Función para leer archivos y analizarlos
def parse_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        print(f"\n{'-'*30}")
        print(f"ANALIZANDO {filename}")
        print(f"{'-'*30}")
        success = parse(data)
        if success:
            print("\nAnálisis exitoso")
        else:
            print("\nError en el análisis")
        return success
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {filename}")
        return False

<<<<<<< HEAD
if __name__ == '__main__':
    parse_file('ejemplo1.txt')
    parse_file('ejemplo2.txt')
    parse_file('error1.txt')
=======
def p_empty(p):
    'empty : '
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
        print(f"Line: {getattr(p, 'lineno', '?')}")
    else:
        print("Syntax error at EOF")
    quit()

# Construye el parser
parser = yacc.yacc()

class TokenFromFile:
    def __init__(self, filename):
        self.tokens = []
        self.index = 0
        self._read_tokens(filename)

    def _read_tokens(self, filename):
        lex_token_re = re.compile(r"LexToken\((\w+),(.+?),(\d+),(\d+)\)")
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                m = lex_token_re.match(line.strip())
                if m:
                    type_, value, lineno, lexpos = m.groups()
                    # Limpia el valor si es string o número
                    value = value.strip()
                    if value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    elif value.replace('.', '', 1).isdigit():
                        # Convierte a int o float si es posible
                        if '.' in value:
                            value = float(value)
                        else:
                            value = int(value)
                    # Crea un objeto tipo token
                    tok = type('Tok', (), {})()
                    tok.type = type_
                    tok.value = value
                    tok.lineno = int(lineno)
                    tok.lexpos = int(lexpos)
                    self.tokens.append(tok)

    def token(self):
        if self.index < len(self.tokens):
            tok = self.tokens[self.index]
            self.index += 1
            return tok
        else:
            return None

if __name__ == "__main__":
    # Error handling si el usuario no proporciona el archivo 
    if len(sys.argv) <= 1:
        print("Por favor proporciona el archivo de tokens a analizar")
        quit()

    token_stream = TokenFromFile(sys.argv[1])
    result = parser.parse(lexer=token_stream)

>>>>>>> 884ab77c4d307d3d670e3cd234c4218fd1d89a0c
