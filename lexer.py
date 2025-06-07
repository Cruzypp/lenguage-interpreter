
# Cruz Yael Pérez González y Elisheba Hannai Trejo Leyva

import sys
import ply.lex as lex

# palabras reservadas
reservadas = {
    'ifelse': 'IFELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'read': 'READ',
    'int': 'INT',
    'float': 'FLOAT'
}

# Lista de tokens para reconocer
tokens = [
    # Simbolos
    'EQ', 'ASSIG', 'GT', 'LT', 'GTEQ', 'LTEQ', 'MAS', 'MENOS', 'POR', 'DIV',
    'PYC', 'COMA', 'DOSP',

    
    'ID',

    # Numeros
    'NUMINT', 'NUMFLOAT',

    # Delimitadoras
    'PARIZ', 'PARDER', 'CORIZQ', 'CORDER'
] + list(reservadas.values())



# Definición de los simbolos
t_EQ = r'='
t_DOSP = r':'
t_ASSIG = r':='
t_GT = r'>'
t_LT = r'<'
t_GTEQ = r'>='
t_LTEQ = r'<='
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIV = r'/'
t_PYC = r';'
t_COMA = r','

# Def delimitadores
t_PARIZ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'


def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

# Numbers
def t_NUMFLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_NUMINT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracter ignorado
t_ignore = ' \t'

# Error si se usa un caracter que no sea reconocido
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            data = f.read()

        lexer.input(data)

        print(f"Tokens from {sys.argv[1]}:")
        for tok in lexer:
            print(tok)
    else:
        print("Please provide a file to analyze")
