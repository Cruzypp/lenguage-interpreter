
# Cruz Yael Pérez González y Elisheba Hannai Trejo Leyva

import sys
import ply.yacc as yacc
import re

# tokens que también usa el lexer
tokens = [
    'EQ', 'ASSIG', 'GT', 'LT', 'GTEQ', 'LTEQ', 'MAS', 'MENOS', 'POR', 'DIV',
    'PYC', 'COMA', 'DOSP',
    'ID', 'NUMINT', 'NUMFLOAT',
    'PARIZ', 'PARDER', 'CORIZQ', 'CORDER',
    'IFELSE', 'WHILE', 'PRINT', 'READ', 'INT', 'FLOAT'
]

# Definición de la gramatica
def p_program(p):
    '''program : opt_decls opt_stmts'''
    print("Sí")

def p_opt_decls(p):
    '''opt_decls : decl_lst
                 | empty'''
    pass

def p_decl_lst(p):
    '''decl_lst : decl PYC decl_lst
                | decl'''
    pass

def p_decl(p):
    'decl : type DOSP id_lst'
    pass

def p_id_lst(p):
    '''id_lst : ID COMA id_lst
              | ID'''
    pass

def p_type(p):
    '''type : INT
            | FLOAT'''
    pass

def p_stmt(p):
    '''stmt : ID ASSIG expr
            | IFELSE PARIZ expression PARDER CORIZQ opt_stmts CORDER CORIZQ opt_stmts CORDER
            | WHILE PARIZ expression PARDER CORIZQ opt_stmts CORDER
            | PRINT expr
            | READ ID'''
    pass

def p_opt_stmts(p):
    '''opt_stmts : stmt_lst
                 | empty'''
    pass

def p_stmt_lst(p):
    '''stmt_lst : stmt PYC stmt_lst
                | stmt'''
    pass

def p_expr(p):
    '''expr : expr MAS term
            | expr MENOS term
            | term'''
    pass

def p_term(p):
    '''term : term POR factor
            | term DIV factor
            | factor'''
    pass

def p_factor(p):
    '''factor : PARIZ expr PARDER
              | ID
              | NUMINT
              | NUMFLOAT'''
    pass

def p_expression(p):
    '''expression : expr LT expr
                  | expr LTEQ expr
                  | expr GT expr
                  | expr GTEQ expr
                  | expr EQ expr'''
    pass

class TokenIterator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.lineno = 1

    def token(self):
        if self.index < len(self.tokens):
            tok = self.tokens[self.index]
            self.index += 1
            return tok
        else:
            return None

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

