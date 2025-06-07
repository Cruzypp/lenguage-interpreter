
# Cruz Yael Pérez González y Elisheba Hannai Trejo Leyva

import sys
import ply.yacc as yacc
from lexer import tokens, lexer


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

def p_empty(p):
    'empty : '
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
        print(f"Line: {p.lexer.lineno}")
    else:
        print("Syntax error at EOF")
    quit()

# Construye el parser
parser = yacc.yacc()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Por favor proporciona el archivo fuente a analizar")
        quit()

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        data = f.read()

    result = parser.parse(data, lexer=lexer)
